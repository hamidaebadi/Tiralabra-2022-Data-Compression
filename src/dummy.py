## this is a dummy file for testing the program's functionality.
# this file will be removed from this project later.
from logic.compress_data import CompressData

huff = CompressData()
text = "My Text"
huff.compress_huffman(text)
encoded = huff.get_encodec_content(text)
print(encoded)
