#
# manpages.py
#
# maintainer: intelkevinputnam
#
# usage: python3 manpages.py
#
# dependencies: 1. clone of Clear Linux documentation https://github.com/clearlinux/clear-linux-documentation
#               2. Makefile or make.bat to create directories and clone repositories (``make man`` to generate. ``make clean-man`` to clean up.)
#
# This script does 4 things:
#
# 1. Find and move reStructuredText versions of man pages (looks for manName.sectionNumber.fileExtension: mixer.1.rst) to reference/manpages directory of Clear Linux docs.
# 2. Massage markdown and reStructuredText man pages into a normalized format.
# 3. Add cross reference links wherever man pages reference each other.
# 4. Create manpages.rst in reference directory (already included in toctree of reference/index.rst)
#
#

import sys
import re
import subprocess
from os import listdir
from os.path import join, isfile
from shutil import copyfile

paths = ["clr-man-pages","clr-power-tweaks/man","clrtrust/man","micro-config-drive/docs/","mixer-tools/docs","swupd-client/docs","tallow/man","telemetrics-client/docs/man"]
pathToRefSection = "../../../reference/"
manPageRegex = '.[0-9]+.rst'
mdManPageRegex = '.[0-9]+.md'
mdBoldItalicRegex = '\\*\\*\\`[a-z-._]+\\`\\*\\*'
manFiles = []
manGroups = {}
manNamePerms = {}
seeAlsoRefs = {}
gitHubGroup = "https://github.com/clearlinux/"
TOC = "\n.. contents::\n    :local:\n"
manPageRest = """.. _man-pages:

Man pages
#########

These pages are generated from `Clear Linux\\* tool
repositories <https://github.com/clearlinux>`__. Updated |today|.


"""
manTOC = """.. toctree::
   :maxdepth: 1

"""

def getPages(paths):
    for path in paths:
        manGroups[path] = []
        files = listdir(path)
        for file in files:
            if file.endswith(".rst"):
                regex_found = re.search(manPageRegex,file)
                if regex_found:
                    filePath = join(path,file)
                    copyfile(filePath,file)
                    manFiles.append(file)
                    manGroups[path].append(file)
                    addManNamePermutations(file)
            elif file.endswith(".md"):
                regex_found = re.search(mdManPageRegex,file)
                if regex_found:
                    filePath = join(path,file)
                    rstFileName = processMDFile(file,filePath)
                    manFiles.append(rstFileName)
                    manGroups[path].append(rstFileName)
                    addManNamePermutations(rstFileName)

def processMDFile(fileName,filePath):
    manName = fileName.rstrip('.md')
    manSection = manName.split('.')[-1]
    manName = manName.rstrip('.' + manSection)
    lines = []
    headerInsert = ""
    with open(filePath,'r') as m:
        lines = m.readlines()
        if "SYNOPSIS" in lines[0]:
                header='='*len(manName)
                lines.insert(0,"# " + manName + "\n\n:Manual section: "+manSection+"\n\n")
        index = 0
        first = True
        for line in lines:
            newLine = line.replace("**`","`") #Fix some markdown formatting weirdness that doesn't translate to reST
            newLine = newLine.replace("`**","`")
            if newLine.startswith("#") and not newLine.startswith("##"): #Fix if all headers are first level
                if first:
                    first = False
                else:
                    newLine = newLine.replace("#","##")
            if "===" in newLine: #fix rst style header that is actually description in some docs
                newLine = ""
                headerInsert = manName + "\n" + '='*len(manName) + "\n\n"
            lines[index] = newLine
            index += 1
        lines.insert(0,headerInsert)

    with open(filePath,'w') as md:
        md.writelines(lines)
        rstFilePath = filePath.replace(".md",".rst")
        rstFileName = fileName.replace(".md",".rst")

    command = "pandoc " +  filePath + " -o " + rstFilePath
    subprocess.run(command, shell=True)
    if isfile(rstFilePath):
        copyfile(rstFilePath,rstFileName)
    return rstFileName

def addManNamePermutations(fileName): #Based on all the syntactical permutations of references to man pages in the documents.
    (manName,subsection) = getNameAndSubsection(fileName)
    manNames = []
    manNames.append("``" + manName + "``\\(" + subsection +")") # ``mixer.init``\(1)
    manNames.append("``" + manName + "``\\ (" + subsection +")") # ``mixer.init``\ (1)
    manNames.append("**``" + manName + "(" + subsection + ")``**")  # **`mixer.init(1)`**
    manNames.append("``" + manName + "(" + subsection + ")``") # ``mixer.init(1)``
    manNames.append("**" + manName + "(" + subsection + ")**") # **mixer.init(1)**
    manNames.append("`" + manName + "(" + subsection + ")`") # `mixer.init(1)`
    manNamePerms[(manName,subsection)] = manNames

def getNameAndSubsection(manFileName):
    manName = manFileName.rstrip('.rst')
    manSection = manName.split('.')[-1]
    manName = manName.rstrip('.'+manSection)
    return (manName,manSection)

def linkToMan(manName,manSection):
    return "`" + manName + "(" + manSection + ") <" + manName + "." + manSection + ".html>`__"
 
def buildManName(name,section):
    return name + "(" + section + ")"

def updateManPages():
    #makeSeeAlsoReplacements()
    for file in manFiles:
        manFile = ""
        with open(file,'r',encoding="utf8") as f:
            manFile = f.read()
            #manFile = addTOC(manFile,file) # Not convinced adding TOC adds value.
            #
            # Add linked cross referencing for all manpages discovered.
            # 1. the manNamePerms dictionary is created once all of the man page source files are discovered
            # 2. Each document is checked for each permutation. 
            # 3. When a permuation is found it is replaced with a normalized version
            # 4. Once normalized it is turned into a reStructuredText link (def linkToMan)
            # 
            for nameAndSection, listOfPerms in manNamePerms.items():
                for perm in listOfPerms:
                    manFile = manFile.replace(perm,buildManName(nameAndSection[0],nameAndSection[1]))
            for manName, doNotUse in manNamePerms.items():
                manFile = manFile.replace(buildManName(manName[0],manName[1]),linkToMan(manName[0],manName[1]))
        with open(file,'w',encoding="utf8") as w:
            w.write(manFile)

def addTOC(manContent,file):
# Find the first instance of the manpage Name
# Skip the underline of the header
# Add a new line
# Add contents directive with local modifier
# Add a new line
    manSectionMeta = ":Manual section:"
    manContentLines = manContent.split('\n')
    index = 0
    for line in manContentLines:
        if manSectionMeta in line:
            manContentLines.insert(index + 2,TOC)
            break
        index += 1
    output = ""
    for line in manContentLines:
        output = output + line + "\n"
    return output

def createManpagesRST():
    filePath = join(pathToRefSection,"man-pages.rst")
    with open(filePath,'w') as f:
        manGrouping = manPageRest
        for path, fileList in manGroups.items():
            repoName = path.split("/")[0]
            repoLink = gitHubGroup + repoName
            repoReST = "`" + repoName + " <" + repoLink + ">`__"
            manGrouping += repoReST + "\n"
            manGrouping += "="*len(repoReST) + "\n\n"
            manGrouping += manTOC
            for file in fileList:
                manGrouping += "   manpages/" + file + "\n"
            manGrouping += "\n"
        f.write(manGrouping)

getPages(paths)
updateManPages()
createManpagesRST()