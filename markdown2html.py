#!/usr/bin/python3
import sys
import os


if(len(sys.argv) < 3):
    print("Usage: ./markdown2html.py README.md README.html" ,file=sys.stderr)
    exit (1)
   
markdown = sys.argv[1]
markdownfile = os.path.exists(markdown)
if(markdownfile == False):
    print("missing {}".format(markdown))
    exit (1)