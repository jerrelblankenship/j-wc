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
    parser.add_argument('-l', type=argparse.FileType('r'))


    args = parser.parse_args()

    if args.c:
        if args.c.name != "<stdin>":
            print(f"    {count_file_bytes(args.c.name)} {path.basename(args.c.name)}")
        else:
            print(f"    {count_file_bytes(args.c)}")
    elif args.l:
        print(f"    {count_file_lines(args.l.name)} {path.basename(args.l.name)}")
    elif args.ch:
        print("C is awesome!!!")
    else:
        print("No arguments were passed in")

def count_file_bytes(file_name):
    return path.getsize(file_name)

def count_file_lines(file_name):
    with open(file_name, "r") as file:
        return sum(1 for line in file)

if __name__ == "__main__":
    main()
