import heapq
from heapq import heapify, heappush, heappop
from entities.node import Node

class Utility:
    def __init__(self):
        self.__char_freq = {}
        self.__priority_queue = []
        self.__root_to_tree = None


    def build_huffman_tree(self, text):
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

    def get_root(self):
        return self.__root_to_tree
