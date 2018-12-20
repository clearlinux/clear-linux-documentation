import io
import os
import re
import urllib
import jinja2
from jinja2 import Environment, FileSystemLoader, Template
import git
from operator import itemgetter
from datetime import datetime 

GITHUB_BASE = "https://github.com/clearlinux/clr-bundles/tree/master/bundles/"
PUNDLES = "https://github.com/clearlinux/clr-bundles/blob/master/packages"

PATTERN1 = re.compile(r"#\s?\[TITLE]:\w?(.*)")
PATTERN2 = re.compile(r"#\s?\[DESCRIPTION]:\w?(.*)")
PATTERN3 = re.compile(r"\(([^()]*|include)\)", re.MULTILINE)
PATTERN4 = re.compile(r"^((?:(?!#)\w+[^-\s][-])\w+|\w+[^\s-])", re.MULTILINE)
# ALT PATTERN4 = re.compile(r"^((?:(?!#)(\w+[^-\s])[-]\w+.)[^\s]{1,}[^\s]|\w+[^\s-])", re.MULTILINE)

PATTERN5 = re.compile(r"^(?!=a)\w.+\s[#]\s(\w+.*)?", re.MULTILINE)
# Previous version: PATTERN5 = re.compile(r"^[^#].*(?<=\s\-\s)(\w+.*)?", re.MULTILINE)

def extractor(lines):
    bundle_title = "title"
    data_desc = "description"
    url = "url"
    include_list = []

    for i in lines:
        title = PATTERN1.match(i)
        desc = PATTERN2.match(i)
        includes = PATTERN3.findall(i)

        if title:
            bundle_title = title.groups(0)[0].strip()
        if desc:
            data_desc = desc.groups(0)[0].strip()
        if url:
            url = os.path.join(GITHUB_BASE, bundle_title)

        if includes:
            include_text = includes[0].strip("()")
            include_list.append(include_text)
    return {"title": bundle_title, "data_desc": data_desc, "include_list": include_list, "url": url}

def pundler():
    with io.open("./cloned_repo/clr-bundles/packages") as file_obj:
        lines = file_obj.readlines()
        pundle_title = "pundle_title"
        pundle_desc = "pundle_desc"
        purl = "purl" 
        pundle_list = []
        pun_desc = []
        pundle_master = []
        
        for i in lines:
            pundle = PATTERN4.findall(i)
            pundle_plus = PATTERN5.findall(i)
            
            if pundle:
                pundle_title = pundle[0]
                pundle_list.append(pundle_title)

            if pundle_plus:
                pundle_desc = pundle_plus[0].strip("[]")
                pun_desc.append(pundle_desc)

        for pun, desc in zip(pundle_list, pun_desc): 
                pundle_master.append({"title": pun, "pun_desc": desc, "purl": PUNDLES})
    return pundle_master

def bundler():
    data = []
    try:
        git.Git("./cloned_repo/").clone("https://github.com/clearlinux/clr-bundles.git")
    except:
        pass
    for root, dirs, files in os.walk("./cloned_repo/clr-bundles/bundles", topdown=False):
        for name in files:
            with open(os.path.join(root, name)) as file_obj:
                lines = file_obj.readlines()
                data.append(extractor(lines))

    pundle_master = pundler()
    data = data + pundle_master 
    filtered = list(filter(lambda x: x.get('title'), data))
    sortedData = sorted(filtered, key=lambda x:x['title'].lower())
    #ALT sortedData2 = sorted(sortedData, key=itemgetter('title'))
    loader = jinja2.FileSystemLoader(searchpath='./')
    env = jinja2.Environment(loader=loader)
    template = env.get_template('template.html')
    template.globals['now'] = datetime.utcnow

    output = template.render(data=sortedData, now=datetime.utcnow())
    with io.open('bundles.html.txt', 'w') as file:
        file.write(output)   
          
bundler()
