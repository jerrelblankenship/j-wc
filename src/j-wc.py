#!/usr/bin/env python3

from os import path, remove
import sys
import argparse
from random import randint

def main():
    parser = argparse.ArgumentParser(description="This script processes command line arguments.")

    # Define the arguments for the tool
    parser.add_argument('--ch', action='store_true', help='Special command')
    parser.add_argument('-c', nargs='?', const=sys.stdin, type=argparse.FileType('r'))


    args = parser.parse_args()

    if args.c:
        if args.c.name != "<stdin>":
            print(f"    {count_file_bytes(args.c.name)} {path.basename(args.c.name)}")
        else:
            print(f"    {count_file_bytes(args.c)}")
    elif args.ch:
        print("C is awesome!!!")
    else:
        print("No arguments were passed in")

def count_file_bytes(file_name):
    return path.getsize(file_name)



if __name__ == "__main__":
    main()
