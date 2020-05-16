#!/usr/bin/env python3
# !/bin/sh
# Author: Arkadiy Garber
from collections import defaultdict
import textwrap
import argparse


def replace(stringOrlist, list, item):
    emptyList = []
    for i in stringOrlist:
        if i not in list:
            emptyList.append(i)
        else:
            emptyList.append(item)
    outString = "".join(emptyList)
    return outString


parser = argparse.ArgumentParser(
    prog="KO-convert.py",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''
    Developed by Arkadiy Garber; University of Delaware, Geological Sciences
    Please send comments and inquiries to arkg@udel.edu
    '''))

parser.add_argument('-db', help='KO Orthology database file')
parser.add_argument('-ko', help="ko output from Ghostkoala")
parser.add_argument('-out', help="base name output file (default = out)", default="out")
parser.add_argument('-taxa', help="optional taxonomy file from GhostKOALA", default="NA")

args = parser.parse_args()


koFile = open(args.ko, "r")
KO = defaultdict(lambda: defaultdict(lambda: 'EMPTY'))
for i in koFile:
    ls = (i.rstrip().split("\t"))
    if len(ls) > 1:
        ko = ls[1]
        orf = ls[0]
        if ko != "" and orf != "":
            KO[orf]["ko"] = ko


db = open(args.db, "r")
dbDict = defaultdict(lambda: defaultdict(lambda: 'EMPTY'))
for i in db:
    ls = i.rstrip().split("\t")
    ko = (ls[3].split("  ")[0])
    name = (ls[3].split("  ")[1])
    dbDict[ko]["system"] = ls[0]
    dbDict[ko]["family"] = ls[1]
    dbDict[ko]["path"] = ls[2]
    dbDict[ko]["name"] = name


taxaDict = defaultdict(lambda: defaultdict(lambda: 'EMPTY'))
if args.taxa != "NA":
    taxa = open(args.taxa)
    for i in taxa:
        ls = i.rstrip().split("\t")
        orf = ls[0]
        orf = orf.split(":")[1]
        taxa1 = ls[2]
        taxa2 = ls[3]
        taxa3 = ls[4]
        taxaDict[orf]["taxa1"] = taxa1
        taxaDict[orf]["taxa2"] = taxa2
        taxaDict[orf]["taxa3"] = taxa3


out = open(args.out, "w")
if args.taxa != "NA":
    out.write("ORF" + "," + "KO" + "," + "KEGG category" + "," + "KEGG family" + "," + "KEGG system" + "," + "gene" + "," + "taxa1" + "," + "taxa2" + "," + "taxa3" + "," + "\n")
else:
    out.write(
        "ORF" + "," + "KO" + "," + "KEGG category" + "," + "KEGG family" + "," + "KEGG system" + "," + "gene" + "," + "\n")

Dictionary = defaultdict(list)
Dictionary2 = defaultdict(list)
Dictionary3 = defaultdict(list)
for i in sorted(KO.keys()):
    orf = i
    ko = (KO[i]["ko"])
    annotation = (KO[i]["name"])
    if args.taxa != "NA":
        out.write(
            orf + "," + ko + "," + replace(dbDict[ko]["path"], [","], ";") + "," + replace(dbDict[ko]["family"], [","],
                                                                                           ";") + "," + replace(
                dbDict[ko]["system"], [","], ";") + ","
            + replace(dbDict[ko]["name"], [","], ";") + "," + taxaDict[orf]["taxa1"] + "," + taxaDict[orf]["taxa2"] + "," + taxaDict[orf]["taxa3"] + "\n")
    else:
        out.write(orf + "," + ko + "," + replace(dbDict[ko]["path"], [","], ";") + "," + replace(dbDict[ko]["family"], [","], ";") + "," + replace(dbDict[ko]["system"], [","], ";") + ","
                  + replace(dbDict[ko]["name"], [","], ";") + "\n")
out.close()

