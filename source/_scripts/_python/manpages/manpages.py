import sys
import re
import subprocess
from os import listdir
from os.path import join
from shutil import copyfile

paths = ["mixer-tools/docs","swupd-client/docs","telemetrics-client/docs/man","clr-man-pages","clr-power-tweaks/man","clrtrust/man"]
manPageRegex = '.[0-9]+.rst'
mdManPageRegex = '.[0-9]+.md'
mdBoldItalicRegex = '\\*\\*\\`[a-z-._]+\\`\\*\\*'
manFiles = []
manNamePerms = {}
seeAlsoRefs = {}
TOC = "\n.. contents::\n    :local:\n"

def getPages(paths):
    for path in paths:
        files = listdir(path)
        for file in files:
            if file.endswith(".rst"):
                regex_found = re.search(manPageRegex,file)
                if regex_found:
                    filePath = join(path,file)
                    copyfile(filePath,file)
                    manFiles.append(file)
                    addManNamePermutations(file)
            elif file.endswith(".md"):
                regex_found = re.search(mdManPageRegex,file)
                if regex_found:
                    filePath = join(path,file)
                    rstFileName = processMDFile(file,filePath)
                    manFiles.append(rstFileName)
                    addManNamePermutations(rstFileName)

def processMDFile(fileName,filePath):
    manName = fileName.rstrip('.md')
    manSection = manName.split('.')[-1]
    manName = manName.rstrip('.' + manSection)
    lines = []
    with open(filePath,'r') as m:
        lines = m.readlines()
        if "SYNOPSIS" in lines[0]:
                header='='*len(manName)
                lines.insert(0,"# " + manName + "\n\n:Manual section: "+manSection+"\n\n")
        index = 0
        for line in lines:
            newLine = line.replace("**`","`")
            lines[index] = newLine.replace("`**","`")
            index += 1
    with open(filePath,'w') as md:
        md.writelines(lines)
        rstFilePath = filePath.rstrip(".md") + ".rst"
        rstFileName = fileName.rstrip(".md") + ".rst"

    command = "pandoc " +  filePath + " -o " + filePath.strip(".md") + ".rst"
    subprocess.run(command, shell=True)
    copyfile(rstFilePath,rstFileName)
    return rstFileName

def addManNamePermutations(fileName):
    (manName,subsection) = getNameAndSubsection(fileName)
    manNames = []
    manNames.append("``" + manName + "``\\(" + subsection +")") # ``mixer.init``\(1)
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
    print("`" + manName + "(" + manSection + ") <" + manName + "." + manSection + ".html>`__")
    return "`" + manName + "(" + manSection + ") <" + manName + "." + manSection + ".html>`__"
 
def buildManName(name,section):
    return name + "(" + section + ")"

def updateManPages():
    #makeSeeAlsoReplacements()
    for file in manFiles:
        manFile = ""
        with open(file,'r') as f:
            manFile = f.read()
            manFile = addTOC(manFile,file)
            for nameAndSection, listOfPerms in manNamePerms.items():
                for perm in listOfPerms:
                    manFile = manFile.replace(perm,buildManName(nameAndSection[0],nameAndSection[1]))
            for manName, doNotUse in manNamePerms.items():
                manFile = manFile.replace(buildManName(manName[0],manName[1]),linkToMan(manName[0],manName[1]))
        with open(file,'w') as w:
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

getPages(paths)
updateManPages()