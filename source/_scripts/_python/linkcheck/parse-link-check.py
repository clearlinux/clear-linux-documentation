#!/usr/bin/env python

#***********************************************************
#
# parse-link-check.py
# 
# Arguments:
#     1. working directory: path to directory containing output
#        of sphinx-build linkcheck (output.txt). Output of this
#        script (broken_links.html) will also be saved in this
#        location.
#
# External file dependencies:
#     1. output.txt - the output of sphinx-build
#     2. link-whitelist.txt - broken links that should be ignored. 
#        This file should be in the same location as this script.
#
# Output:
#     1. broken_links.html - provides count of broken and whitelist 
#        matches. Also provides links to all flagged links. Will 
#        appear in the same directory as output.txt
#     2. Error code 255 if unexpected broken links are found
#
# Purpose:
#     This script supplements the built-in link checking of 
#     sphinx-build. In practice, sphinx-build link checking
#     will produce a variety of false negatives. This script,
#     using the white list, will skip known false negatives and
#     anchors, providing an HTML digest of suspected actual
#     broken links if there are any.
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
numAnchors = 0
newLines = ["<!DOCTYPE html><html><head><style>body {font-family: sans-serif;}</style></head><body>"]
whiteListLines = []
anchorLines = []

for line in lines:
    if "[broken]" in line:
        strings = line.split(" ")
        link = strings[2][:-1]
        link = link.strip()
        if link in whitelist:
            whiteListLines.append("<b>" + strings[0] + "</b>\n<blockquote><a href=\"" + link + "\">[whitelist] " + link + "</a></blockquote>\n")
            numWhiteListMatches += 1
            print("[White list match] " + link)
        elif "Anchor '" in line:
            anchorLines.append("<b>" + strings[0] + "</b>\n<blockquote><a href=\"" + link + "\">[anchor] " + link + "</a></blockquote>\n")
            numAnchors += 1
            print("[Anchor not found] " + link)
        else: 
            newLines.append("<b>" + strings[0] + "</b>\n<blockquote><a href=\"" + link + "\">[broken] " + link + "</a></blockquote>\n")
            numBrokenLinks += 1
            print("[broken link] " + link)

newLines.insert(0,"<h1>" + str(numBrokenLinks + numWhiteListMatches) + " broken links found in Sphinx link check</h1>\n")
newLines.insert(1,"<h2>" + str(numBrokenLinks) + " unmatched broken links</h2>\n")
newLines.append("<h2>" + str(numAnchors) + " links did not find anchors</h2>\n")
for line in anchorLines:
    newLines.append(line)

newLines.append("<h2>" + str(numWhiteListMatches) + " links matched whitelist</h2>\n")
for line in whiteListLines:
	newLines.append(line)
newLines.append("</body></html>")

with open (outFilePath, "w") as outF:
    for line in newLines:
        outF.write(line)

print("See ./" + outFilePath + " for a detailed breakdown of broken links.")

if numBrokenLinks != 0:
    print (str(numBrokenLinks) + " detected. Exiting with error code 255.")
    sys.exit(-1) 
else:
    print ("No unexpected broken links detected.")
