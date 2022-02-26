## this is a dummy file for testing program's functionality.
# this file will be removed from this project later.
s = "cabracadabrarrarrad"
MAX_SEARCH_BUFFER_SIZE = 7
MAX_LOOK_AHEAD_BUFFER_SIZE = 6
next_lb_index = 6
search_buffer = []
look_ahead_buffer = [s[i] for i in range(MAX_LOOK_AHEAD_BUFFER_SIZE)]
encoded_list = []

while len(look_ahead_buffer) != 0:
    substr = look_ahead_buffer[0]
    if len(search_buffer) == 0:
        encoded_list.append((0, 0, substr))
        #shift window
        search_buffer.append(substr)
        look_ahead_buffer.pop(0)
        look_ahead_buffer.append(s[next_lb_index])
        next_lb_index += 1
        print(0, 0, substr)
    else:
        offset = 0
        length = 0
        codeWord = look_ahead_buffer[0]
        char_found = 0

        found = True
        tempString = "".join(search_buffer)
        substr = look_ahead_buffer[0]
        next_from_lb = 0
        owned_from_lb = 0
        while found:
            #check if end of search buffer is reached
            if (offset + length) >= (MAX_SEARCH_BUFFER_SIZE - 1):
                tempString += look_ahead_buffer[next_from_lb]
                next_from_lb += 1
                owned_from_lb += 1

            if tempString.find(substr) != -1:
                char_found += 1
                offset = (len(search_buffer) - tempString.rfind(substr))
                length = len(substr)
                codeWord = look_ahead_buffer[char_found]
                #increase substring for more matches
                substr += look_ahead_buffer[char_found]
                continue
            else:
                found = False
                #shift window
                for c in substr:
                    if len(search_buffer) < MAX_SEARCH_BUFFER_SIZE:
                        look_ahead_buffer.pop(0)
                        search_buffer.append(c)
                    else:
                        search_buffer.pop(0)
                        search_buffer.append(c)
                        look_ahead_buffer.pop(0)

                    if next_lb_index < len(s):
                        look_ahead_buffer.append(s[next_lb_index])
                        next_lb_index += 1


            print(offset, length, codeWord)
            