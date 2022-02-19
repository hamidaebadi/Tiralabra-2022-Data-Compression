import heapq
from heapq import heapify, heappush, heappop
from entities.node import Node

class HuffmanCoding:
    def __init__(self):
        self.__char_freq = {}
        self.__priority_queue = []
        self.__root_to_tree = None
        self.__decoded_content = ''
        self.__huffman_codes = {}


    def compress_data(self, text):
        self.__build_huffman_tree(text)
        root = self.__root_to_tree
        self.__create_huffman_codes(root, '')
    
    def get_encoded_content(self, original_content):
        content = ''
        for c in original_content:
            content += self.__huffman_codes.get(c)
        return content

    def decode_content(self, encoded_content):
        root = self.__root_to_tree
        if Node.is_leaf_node(root):
             while root.freq > 0:
                print(root.character, end='')
                root.freq = root.freq - 1
        else:
            index = -1
            while index < len(encoded_content)-1:
                index = self.__huffman_decode(root, index, encoded_content)
        return self.__decoded_content

    def get_decoded_text(self):
        return self.__decoded_content
    
    #private methods
    def __build_huffman_tree(self, text):
        if len(text) == 0:
            return False

        #count frequencies of each character
        self.__count_freq(text)

        #use minheap to create huffman tree
        self.__create_priority_queue()

        while len(self.__priority_queue) != 1:
            left_node = heappop(self.__priority_queue)
            right_node = heappop(self.__priority_queue)

            #create a parrent node with left and right node
            #parrent's node frequenciy is equal to the sum of both left and right
            #nodes' frequencies
            total = left_node.freq + right_node.freq
            heappush(self.__priority_queue, Node(None, total, left_node, right_node))

        self.__root_to_tree = self.__priority_queue[0]

    def __count_freq(self, text):
        for c in text:
            if c in self.__char_freq:
                self.__char_freq[c] = self.__char_freq[c]+1
            else:
                self.__char_freq[c] = 1

    def __create_priority_queue(self):
        for k, v in self.__char_freq.items():
            heappush(self.__priority_queue, Node(k, v))
        heapify(self.__priority_queue)

    def __create_huffman_codes(self, root, s):
        if root is None:
            return

        if Node.is_leaf_node(root):
            self.__huffman_codes[root.character] = s if len(s) > 0 else '1'

        self.__create_huffman_codes(root.left, s+'0')
        self.__create_huffman_codes(root.right, s+'1')

    def __huffman_decode(self, root, i, s):
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

        return self.__huffman_decode(root, i, s)

    