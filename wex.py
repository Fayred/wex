#coding:utf-8

import argparse
from termcolor import cprint

def xor(keyFilename, inputFilename, outputFilename):
    key = bytearray(open(keyFilename, "rb").read()).strip()

    inputFile = open(inputFilename, "rb").read()

    outputFile = bytearray([])
    for i,byte in enumerate(inputFile):
        outputFile.append(byte ^ key[i%len(key)])

    open(outputFilename, "wb").write(outputFile)
    
    cprint("[+] Finish", "green")
    cprint(f"[*] Input : '{inputFilename}'", "cyan")
    cprint(f"[*] Ouput : '{outputFilename}'", "cyan")

parser = argparse.ArgumentParser()
parser.add_argument("-f", metavar="inputFilename", help="file which is in input")
parser.add_argument("-o", metavar="outputFilename", help="file which is in output")
parser.add_argument("-k", metavar="keyFilename", help="file with key to encrypt/decrypt file")
args = parser.parse_args()

if args.f and args.o and args.k:
    xor(args.k, args.f, args.o)
else:
    parser.print_help()