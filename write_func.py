import baseSet
import os

def init_record():
    with open(r"picfile/picIDs.txt", "w", encoding='utf-8') as f_pid_init:    
        f_pid_init.write('')
    with open(r"picfile/picPaths.txt", "w", encoding='utf-8') as f_pPath_init:      
        f_pPath_init.write('')
        
def write_tagContent(content):
    with open(r"picfile/tagContent.html", "w", encoding='utf-8') as f_tagC:    
        f_tagC.write(content)

def write_picIDs(content):
    with open(r"picfile/picIDs.txt", "a", encoding='utf-8') as f_pid_w:    
        [f_pid_w.write(pid+'\n') for pid in content]

def write_postContent(content):
    with open(r"picfile/postContent.html", "w", encoding='utf-8') as f_postC:    
        f_postC.write(content)

def write_picPaths(content):
    with open(r"picfile/picPaths.txt", "a", encoding='utf-8') as f_pPath_w:    
        [f_pPath_w.write(pPath+'\n') for pPath in content]

def write_picSum(content):
    with open(r"picfile/picSum.txt", "w", encoding='utf-8') as f_picSum: 
        [f_picSum.write(pNum+'\n') for pNum in content]

def make_tagFile(tag):
    childFile=baseSet.file_save+rf'/{tag}/'
    if not os.path.exists(childFile):
        os.mkdir(childFile)
    return childFile

