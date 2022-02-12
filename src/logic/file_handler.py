import os

class FileHandler:

    def __init__(self, filename):
        self.__filename = filename
        self.__file_object = None
        self.__original_file_size = os.path.getsize(filename)


    def __open_file(self, mode):
        try:
            self.__file_object = open(self.__filename, mode)
            return True
        except FileNotFoundError:
            print("Error: File not found in your current directory!")
            print(f"your filename was: {self.__filename}")

    def __close_file(self):
        if not self.__file_object.closed:
            self.__file_object.close()

    def get_file_content(self):
        if self.__open_file('r'):
            content = self.__file_object.read()
            self.__close_file()
            return content
        else:
            return False

    def create_compressed_file(self, content):
        dot = self.__filename.index('.')
        self.__filename = self.__filename[:dot]+".xip"
        i = 0
        buffer = bytearray()
        while i < len(content):
            buffer.append( int(content[i:i+8], 2) )
            i += 8

        # now write buffer to file
        if self.__open_file('wb'):
            #write codes to file for decodig purposes
            self.__file_object.write(buffer)
            self.__close_file()
            return True
        else:
            return False

    def get_file_size(self):
        return os.path.getsize(self.__filename)
