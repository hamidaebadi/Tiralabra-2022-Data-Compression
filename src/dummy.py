## this is a dummy file for testing program's functionality.
# this file will be removed from this project later.
s = "abcdabccdrrab"
last_index = 7
look_ahead_buffer = [s[i] for i in range(8)] # size = 8
search_buffer = [] #size = 5
#window size = 8 + 5 = 13
encoded_list = []

#initializing codes: fill look-ahead-buffer
print(look_ahead_buffer)

while len(look_ahead_buffer) != 0:
    if len(search_buffer) == 0:
        encoded_list.append((0, 0, look_ahead_buffer[0]))
        search_buffer.append(look_ahead_buffer[0])
        look_ahead_buffer.pop(0)
        last_index += 1
        if last_index < len(s):
            look_ahead_buffer.append(s[last_index])
    


