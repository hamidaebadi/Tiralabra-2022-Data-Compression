class Decompressor:
    def __init__(self, file, encoded_content, decomp_algo):
        self.__encoded_content = file.get_content() if file else encoded_content
        self.__decompressor = decomp_algo

    def decode(self):
        return self.__decompressor.decode_content(self.__encoded_content)
        