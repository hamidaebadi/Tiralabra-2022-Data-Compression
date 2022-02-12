import argparse
from logic.compress_data import CompressData
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

#create object of type CompressData
data_compression = CompressData()

if args.text is not None and args.compress and args.algo == "HUFFMAN":
    print("Text will be compressed using Huffman algorithm")
    data_compression.compress_huffman(args.text)
    encoded_text = data_compression.get_encoded_content(args.text)
    decoded_text = data_compression.get_decoded_content(encoded_text)
    print("original text was : ", args.text)
    print("Encoded content: ", encoded_text)
    print("Decoded content is: ", decoded_text)
    
elif args.filename is not None and args.compress and args.algo == "HUFFMAN":
    file_obj = FileHandler(args.filename)
    #read file data
    original_content = file_obj.get_file_content()
    original_filesize = file_obj.get_file_size()

    #compress it 
    data_compression.compress_huffman(original_content)
    encoded_text = data_compression.get_encoded_content(original_content)


    #write compressed data into a new file and save file
    if file_obj.create_compressed_file(encoded_text):
        comp_file_size = file_obj.get_file_size()
        print("compressed file has been created")
        print(f"Original file size: {original_filesize}")
        print(f"compressed file size: {comp_file_size}")
    
