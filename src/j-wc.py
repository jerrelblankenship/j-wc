#!/usr/bin/env python3

from os import path, remove
import sys
import argparse
from random import randint

def main():
    parser = argparse.ArgumentParser(description="This script processes command line arguments.")

    # Define the arguments for the tool
    parser.add_argument('--ch', action='store_true', help='Special command')
    parser.add_argument('-c', nargs='?', type=argparse.FileType('r'), const=sys.stdin)
    parser.add_argument('-l', nargs='?', type=argparse.FileType('r'), const=sys.stdin)
    parser.add_argument('-w', nargs='?', type=argparse.FileType('r'), const=sys.stdin)
    parser.add_argument('-m', nargs='?', type=argparse.FileType('r'), const=sys.stdin)
    parser.add_argument('filename', nargs='?')

    args = parser.parse_args()
    if args.ch == False and all(arg is None or (arg == sys.stdin and sys.stdin not in sys.argv) for arg in [args.c, args.l, args.w, args.m]):
        print(f"  {count_file_lines(args.filename)}(lines) {count_file_words(args.filename)}(words) {count_file_bytes(args.filename)}(bytes) {path.basename(args.filename)}")
    elif args.c:
        if args.c.name != "<stdin>":
            print(f"  {count_file_bytes(args.c.name)} {path.basename(args.c.name)}")
        else:
            print(f"  {count_file_bytes(args.c)}")
    elif args.l:
        print(f"  {count_file_lines(args.l.name)} {path.basename(args.l.name)}")
    elif args.w:
        print(f"  {count_file_words(args.w.name)} {path.basename(args.w.name)}")
    elif args.m:
        print(f"  {count_file_characters(args.m.name)} {path.basename(args.m.name)}")
    elif args.ch:
        print("C is awesome!!!")
    else:
        print("No arguments were passed in")

def count_file_bytes(file_name):
    return path.getsize(file_name)

def count_file_lines(file_name):
    with open(file_name, "r") as file:
        return sum(1 for line in file)

def count_file_words(file_name):
    word_count = 0
    with open(file_name, "r") as file:
        for line in file:
            words = line.split()
            word_count += len(words)
    return word_count

def count_file_characters(file_name):
    character_count = 0
    with open(file_name, "r", encoding="utf-8") as file:
        for chunk in iter(lambda: file.read(1024), ''):
            character_count += len(chunk)
    return character_count

if __name__ == "__main__":
    main()
