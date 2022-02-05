from logic.utility import Utility
from entities.node import Node

class CompressData:
    def __init__(self):
        self.__huffman_utility = Utility()
        self.__huffman_codes = {}
        self.__original_content = None
        self.__encoded_content = ''
        self.__decoded_content = ''


    def __encode_huffamn(self, root, s, huffman_codes):
        if root is None:
            return

        if Node.is_leaf_node(root):
            huffman_codes[root.character] = s if len(s) > 0 else '1'

        self.__encode_huffamn(root.left, s+'0', huffman_codes)
        self.__encode_huffamn(root.right, s+'1', huffman_codes)
    
    def __decode_huffman(self, root, i, s):
        if root is None:
            return i

        if Node.is_leaf_node(root):
            #print(root.character, end="")
            self.__decoded_content += root.character
            return i

        i = i + 1
        if s[i] == '0':
            root = root.left
        else:
            root = root.right

        return self.__decode_huffman(root, i, s)

    def compress_huffman(self, text):
        tree_result = self.__huffman_utility.build_huffman_tree(text)
        root = self.__huffman_utility.get_root()
        self.__encode_huffamn(root, '', self.__huffman_codes)
        return tree_result

    def get_encoded_content(self, text):
        content = ''
        for c in text:
            content += self.__huffman_codes.get(c)
        return content

    def get_decoded_content(self, s):
        root = self.__huffman_utility.get_root()
        if Node.is_leaf_node(root):
             while root.freq > 0:
                print(root.ch, end='')
                root.freq = root.freq - 1
        else:
            index = -1
            while index < len(s)-1:
                index = self.__decode_huffman(root, index, s)
        return self.__decoded_content