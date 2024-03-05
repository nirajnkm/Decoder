#!/usr/bin/python3

import argparse
import sys
import base64

parse = argparse.ArgumentParser(description="Python script to decript base64 and base32",usage = '%(prog)s -b32/b64 ciper',epilog = "Example - %(prog)s -b64 NBSWY3DP")

parse.add_argument("-b32",help="decode base32 encoding",metavar="base32",dest='b32',nargs="+")

parse.add_argument("-b64",help="decode base64 encoding",metavar="base64",dest="b64",nargs="+")

parse.add_argument("-v",help="print version",action="version",version="%(prog)s 1.0")

args = parse.parse_args()

if len(sys.argv) == 1:
    parse.print_help(sys.stderr)
    sys.exit(1)

b64 = args.b64

b32 = args.b32


if b64:
    for i in b64:
        print((base64.b64decode(i)).decode())

if b32:
    for i in b32:
        print((base64.b32decode(i)).decode())