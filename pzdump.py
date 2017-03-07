#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser(description="A tool to dump timezone data.")
parser.add_argument("-V", "--version", help="output version information and exit",
                    action="store_true")
parser.add_argument("-v", "--verbose", help="print lowest and highest possible time and time discontinuities",
                    action="store_true")
parser.add_argument("-c", "--cutoff", help="cut off verbose output by the given range",
                    nargs=2, metavar=("loyear", "hiyear"))
parser.add_argument("zonename", help="time zone(s) to dump",
                    nargs="*", action="append")

args = parser.parse_args()

if args.version:
    print("pzdump 0.00")
    sys.exit()
