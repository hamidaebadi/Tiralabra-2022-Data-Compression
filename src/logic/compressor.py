from logic.huffman import HuffmanCoding
from logic.lempel_ziv import LempelZiv

class Compressor:
    def __init__(self, file, text, comp_algo):
        self.__org_content = file.get_content() if file else text
        self.__compressor = comp_algo
        self.__data_compressed = False

    #compress original content
    def compress(self):
        if self.__data_compressed:
            return False
        self.__compressor.compress_data(self.__org_content)
        self.__data_compressed = True
        return True

    def get_original_content(self):
        return self.__org_content

    def encoded_content(self):
        if self.__data_compressed:
            encoded = self.__compressor.get_encoded_content(self.__org_content)
            return encoded
        print("Please compress data before using this method")
        