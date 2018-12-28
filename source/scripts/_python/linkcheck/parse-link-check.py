#!/usr/bin/env python

#***********************************************************
#
# parse-link-check.py
# 
# Arguments:
#     1. path to input file 
#
# External file dependencies:
#     1. output.txt - the output of sphinx-build
#     2. link-whitelist.txt - broken links that should be ignored
#
# Output:
#     1. broken_links.html - provides count of broken and whitelist 
#        matches. Also provides links to all flagged links. Will 
#        appear in the same directory as output.txt
#     2. Error code 255 if unexpected broken links are found
#
#***********************************************************


import sys
import re
import os

fileName = "output.txt"
outFile = "broken_links.html"
whitelistFile = "link-whitelist.txt"

if len(sys.argv) < 2:
    print ("Enter path of input directory")
    sys.exit()

scriptPath = sys.argv[0]
outputPath = sys.argv[1]
fileNamePath = outputPath + "/" + fileName
outFilePath = outputPath + "/" +  outFile

whitelistFilePath = os.path.dirname(scriptPath) + "/" + whitelistFile

with open (whitelistFilePath) as w:
	whLines = w.readlines()

whitelist = []
for line in whLines:
	link = line.rstrip()
	whitelist.append(link)

with open (fileNamePath) as f:
    lines = f.readlines()

numBrokenLinks = 0
numWhiteListMatches = 0
newLines = ["<!DOCTYPE html><html><head><style>body {font-family: sans-serif;}</style></head><body>"]
whiteListLines = []

for line in lines:
    if "[broken]" in line:
        strings = line.split(" ")
        link = strings[2][:-1]
        link = link.strip()
        if link in whitelist:
            whiteListLines.append("<b>" + strings[0] + "</b>\n<blockquote><a href=\"" + link + "\">[whitelist] " + link + "</a></blockquote>\n")
            numWhiteListMatches += 1
        else:
            newLines.append("<b>" + strings[0] + "</b>\n<blockquote><a href=\"" + link + "\">[broken] " + link + "</a></blockquote>\n")
            numBrokenLinks += 1

newLines.insert(0,"<h1>" + str(numBrokenLinks + numWhiteListMatches) + " broken links found in Sphinx link check</h1>\n")
newLines.insert(1,"<h2>" + str(numBrokenLinks) + " unmatched broken links</h2>\n")
newLines.append("<h2>" + str(numWhiteListMatches) + " links matched whitelist</h2>\n")
for line in whiteListLines:
	newLines.append(line)
newLines.append("</body></html>")

with open (outFilePath, "w") as outF:
    for line in newLines:
        outF.write(line)

print("See ./" + outFilePath + " for a detailed breakdown of broken links.")

if numBrokenLinks != 0:
    print (numBrokenLinks + " detected. Exiting with error code 255.")
    sys.exit(-1) 
else:
    print ("No unexpected broken links detected.")
