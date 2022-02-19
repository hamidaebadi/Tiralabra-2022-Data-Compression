import argparse
from logic.huffman import HuffmanCoding
from logic.compressor import Compressor
from logic.decompressor import Decompressor
from logic.file_handler import FileHandler

program_description = """
xip is a tool for compressing textfiles data into
less size files for transmitting them
"""
parser = argparse.ArgumentParser(description=program_description)

parser.add_argument('-c', "--compress", help="-c will compress files' data", action="store_true")
parser.add_argument('-d', "--decode", help="Decode the compressed files into original files", action="store_true")
parser.add_argument('-f', "--filename", help="file to compress")
parser.add_argument("-a", "--algo", choices=["HUFFMAN", "LEMPEL_ZIV", "H_L"], help="Chose algorithm to use for compressing data")
parser.add_argument("-s", "--statistics", default="OFF", 
help="When statistics is ON, it will show some data related to compressed file",
choices=["OFF", "ON"])

parser.add_argument('-t', "--text", help="Text to be compressed", default=None)
args = parser.parse_args()

huffman_algo = HuffmanCoding()
if args.text is not None and args.compress and args.algo == "HUFFMAN":
    compressorApp = Compressor(file=None, text=args.text, comp_algo=huffman_algo)
    compressorApp.compress()
    print("Text is compressed")
    print("encoded content: ", end="")
    enc_content = compressorApp.encoded_content()
    print(enc_content)

    #creating decompressor object
    print("Decoded immediately: ", end="")
    decompressorApp = Decompressor(file=None, encoded_content=enc_content, decomp_algo=huffman_algo)
    decoded_content = decompressorApp.decode()
    print(decoded_content)


elif args.filename is not None and args.compress and args.algo == "HUFFMAN":
    file_obj = FileHandler(args.filename)
    original_file_size = file_obj.get_file_size()
    compressorApp = Compressor(file=file_obj, text=None, comp_algo=huffman_algo)
    compressorApp.compress()
    encoded_content = compressorApp.encoded_content()
    #write compressed data into a new file and save file
    if file_obj.create_compressed_file(encoded_content):
        comp_file_size = file_obj.get_file_size()
        print("compressed file has been created")
        print(f"original file size: {original_file_size} bytes")
        print(f"compressed file size: {comp_file_size} bytes")
    
