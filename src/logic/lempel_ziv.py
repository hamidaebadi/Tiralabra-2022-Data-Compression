class LempelZiv:
    def __init__(self):
        self.__MAX_SEARCH_BUFFER_SIZE = 7
        self.__MAX_LOOK_AHEAD_BUFFER_SIZE = 6
        self.__encoded_list = []
        self.__search_buffer = []
        self.__look_ahead_buffer = []

    def compress_data(self, text):
        self.__look_ahead_buffer = [text[i] for i in range(self.__MAX_LOOK_AHEAD_BUFFER_SIZE)]
        next_lb_index = self.__MAX_LOOK_AHEAD_BUFFER_SIZE
        while len(self.__look_ahead_buffer) != 0:
            substr = self.__look_ahead_buffer[0]
            if len(self.__search_buffer) == 0:
                self.__encoded_list.append((0, 0, substr))
                #shift window
                self.__search_buffer.append(substr)
                self.__look_ahead_buffer.pop(0)
                self.__look_ahead_buffer.append(text[next_lb_index])
                next_lb_index += 1

            else:
                offset = 0
                length = 0
                codeWord = self.__look_ahead_buffer[0]
                char_found = 0

                found = True
                tempString = "".join(self.__search_buffer)
                substr = self.__look_ahead_buffer[0]
                next_from_lb = 0
                owned_from_lb = 0
                while found:
                    #check if end of search buffer is reached
                    if (offset + length) >= (self.__MAX_SEARCH_BUFFER_SIZE - 1):
                        tempString += self.__look_ahead_buffer[next_from_lb]
                        next_from_lb += 1
                        owned_from_lb += 1

                    if tempString.find(substr) != -1:
                        char_found += 1
                        offset = (len(self.__search_buffer) - tempString.rfind(substr))
                        length = len(substr)
                        codeWord = self.__look_ahead_buffer[char_found]
                        #increase substring for more matches
                        substr += self.__look_ahead_buffer[char_found]
                        continue
                    else:
                        found = False
                        #shift window
                        for c in substr:
                            if len(self.__search_buffer) < self.__MAX_SEARCH_BUFFER_SIZE:
                                self.__look_ahead_buffer.pop(0)
                                self.__search_buffer.append(c)
                            else:
                                self.__search_buffer.pop(0)
                                self.__search_buffer.append(c)
                                self.__look_ahead_buffer.pop(0)

                            if next_lb_index < len(text):
                                self.__look_ahead_buffer.append(text[next_lb_index])
                                next_lb_index += 1

                    self.__encoded_list.append((offset, length, codeWord))

    def get_compressed_content(self):
        return self.__encoded_list


