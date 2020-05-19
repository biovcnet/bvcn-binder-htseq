#!/usr/bin/env python3
from collections import defaultdict
import re
import os
import textwrap
import argparse
import sys


parser = argparse.ArgumentParser(
    prog="mmseqs-helper.py",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''
    *******************************************************
    '''))

parser.add_argument('-gff', type=str, help="GFF file used to generate the counts table", default="NA")
parser.add_argument('-id', type=str, help="attribute used from the GFF file (default = ID)", default="ID")
parser.add_argument('-counts', type=str, help="counts table output from htseq-count", default="NA")
parser.add_argument('-delim', type=str, help="delimiter for counts table (default = TAB)", default="\t")
parser.add_argument('-out', type=str, help="name output file (default is the name of your counts file appended with \'.tpm\')", default="NA")

args = parser.parse_args()

if args.gff == "NA":
    print("GFF file not provided")
    raise SystemExit

if args.counts == "NA":
    print("Counts file not provided")
    raise SystemExit

counts = open(args.counts)
gff = open(args.gff)
if args.out == "NA":
    outfilename = args.counts
    outfilename = outfilename + ".tpm"
    out = open(outfilename, "w")
else:
    out = open(args.out, "w")


gffDict = defaultdict(lambda: defaultdict(lambda: 'EMPTY'))
for i in gff:
    if not re.match(r'#', i):
        ls = i.rstrip().split("\t")
        start = float(ls[3])
        end = float(ls[4])
        length = end - start
        attributes = ls[8].split(";")
        for j in attributes:
            attribute = args.id + "="
            if re.findall(attribute, j):
                attributeList = j.split("=")
                ID = attributeList[1]
                gffDict[ID] = length
                break

totalRPK = 0
for i in counts:
    ls = i.rstrip().split(args.delim)
    if not re.match(r'#', i) and not re.match(r'__', i):
        ID = ls[0]
        count = float(ls[1])
        length = gffDict[ID]
        pk = length/1000
        rpk = count/pk
        totalRPK += rpk

denom = totalRPK/1000000


counts = open(args.counts)
for i in counts:
    ls = i.rstrip().split(args.delim)
    if not re.match(r'#', i) and not re.match(r'__', i):
        ID = ls[0]
        count = float(ls[1])
        length = gffDict[ID]
        pk = length/1000
        rpk = count/pk
        tpm = rpk/denom
        out.write(ID + args.delim + str(tpm) + "\n")
out.close()








