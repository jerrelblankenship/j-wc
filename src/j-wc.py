#!/usr/bin/env python3

from os import path, remove
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="This script processes command line arguments.")

    # Define the arguments for the tool
    parser.add_argument('--ch', action='store_true', help='Special command')
    parser.add_argument('-c', action='store_true', help='Count the number of bytes in the file or stdin')
    parser.add_argument('-l', action='store_true', help='Count the number of lines in the file or stdin')
    parser.add_argument('-w', action='store_true', help='Count the number of words in the file or stdin')
    parser.add_argument('-m', action='store_true', help='Count the number of characters in the file or stdin')
    parser.add_argument('filename', nargs='?', type=argparse.FileType('r'), default=sys.stdin)

    args = parser.parse_args()

    # We need to determine if no arguments were passed in. If there were none, then execute the script as `-clw` has been passed in.
    if not any([args.c, args.l, args.w, args.m, args.ch]):
        args.c, args.l, args.w = True, True, True

    source = args.filename
    source_input = path.basename(source.name) if source != sys.stdin else "<stdin>"

    if args.ch:
        print(f"C is awesome!!!")
    if args.c:
        print(f"  {count_file_bytes(source)} {source_input}")
        source.seek(0)
    if args.l:
        print(f"  {count_file_lines(source)} {source_input}")
        source.seek(0)
    if args.w:
        print(f"  {count_file_words(source)} {source_input}")
        source.seek(0)
    if args.m:
        print(f"  {count_file_characters(source)} {source_input}")

def count_file_bytes(source):
    if (source.name != "<stdin>"):
        return path.getsize(source.name)
    else:
        content = read_source_content(source)
        return len(content.encode('utf-8'))

def count_file_lines(source):
    return sum(1 for _ in source)

def count_file_words(source):
    return sum(len(line.split()) for line in source)

def count_file_characters(source):
    return sum(len(chunk) for chunk in iter(lambda: source.read(1024), ''))

def read_source_content(source):
    source.seek(0)  # Reset file pointer to the start
    return source.read()

if __name__ == "__main__":
    main()
