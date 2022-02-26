from logic.lempel_ziv import LempelZiv
lz77 = LempelZiv()
s = "cabracadabrarrarrad"
lz77.compress_data(s)
cl = lz77.get_compressed_content()
for code in cl:
    print(code)