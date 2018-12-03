#!/usr/bin/env python

import sys
import re

fileName = "output.txt"
outFile = "broken_links.html"

if len(sys.argv) < 2:
    print ("Enter a file name to parse")
    sys.exit()

outputPath = sys.argv[1]
fileNamePath = outputPath + "/" + fileName
outFilePath = outputPath + "/" + outFile

with open (fileNamePath) as f:
    lines = f.readlines()

numBrokenLinks = 0
newLines = []
for line in lines:
    if "[broken]" in line:
        strings = line.split(" ")
        newLines.append("<b>" + strings[0] + "</b>\n<blockquote><a href=\"" + strings[2][:-1] + "\">[broken] " + strings[2][:-1] + "</a></blockquote>\n")
        numBrokenLinks += 1
newLines.insert(0,"<h1>" + str(numBrokenLinks) + " broken links found in Sphinx link check.</h1>\n")

with open (outFilePath, "w") as outF:
    for line in newLines:
        outF.write(line)