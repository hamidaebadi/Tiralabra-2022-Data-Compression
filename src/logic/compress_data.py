from logic.utility import Utility
from entities.node import Node

class CompressData:
    def __init__(self):
        self.__huffman_utility = Utility()
        self.__huffman_codes = {}
        self.__original_content = None
        self.__encoded_content = ''


    def encode_huffamn(self, root, s, huffman_codes):
        if root is None:
            return

        if Node.is_leaf_node(root):
            huffman_codes[root.character] = s if len(s) > 0 else '1'

        self.encode_huffamn(root.left, s+'0', huffman_codes)
        self.encode_huffamn(root.right, s+'1', huffman_codes)

    def compress_huffman(self, text):
        tree_result = self.__huffman_utility.build_huffman_tree(text)
        root = self.__huffman_utility.get_root()
        self.encode_huffamn(root, '', self.__huffman_codes)
        return tree_result

    #getters and setters
    def get_encodec_content(self, text):
        content = ''
        for c in text:
            content += self.__huffman_codes.get(c)
        return content
