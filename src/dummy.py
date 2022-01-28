from logic.compress_data import CompressData

huff = CompressData()
text = "My Text"
huff.compress_huffman(text)
encoded = huff.get_encodec_content(text)
print(encoded)
