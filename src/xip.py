import argparse
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

if args.text is not None and args.compress and args.algo == "HUFFMAN":
    print("Text will be compressed using Huffman algorithm")
    print(f"Text: {args.text}")
else:
    print("Shit")