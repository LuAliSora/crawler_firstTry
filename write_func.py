import baseSet
import os

def init_record():
    with open(baseSet.file_save+"picIDs.txt", "w", encoding='utf-8') as f_pid_init:    
        f_pid_init.write('')
    with open(baseSet.file_save+"picPaths.txt", "w", encoding='utf-8') as f_pPath_init:      
        f_pPath_init.write('')
        
def write_tagContent(content):
    with open(baseSet.file_save+"tagContent.html", "w", encoding='utf-8') as f_tagC:    
        f_tagC.write(content)

def write_picIDs(content):
    with open(baseSet.file_save+"picIDs.txt", "a", encoding='utf-8') as f_pid_w:    
        [f_pid_w.write(pid+'\n') for pid in content]

def write_postContent(content):
    with open(baseSet.file_save+"postContent.html", "w", encoding='utf-8') as f_postC:    
        f_postC.write(content)

def write_picPaths(content):
    with open(baseSet.file_save+"picPaths.txt", "a", encoding='utf-8') as f_pPath_w:    
        [f_pPath_w.write(pPath+'\n') for pPath in content]

def write_picSum(content):
    with open(baseSet.file_save+"picSum.txt", "w", encoding='utf-8') as f_picSum: 
        [f_picSum.write(pNum+'\n') for pNum in content]

def make_tagFile(tag):
    childFile=baseSet.file_save+f'{tag}/'
    if not os.path.exists(childFile):
        os.mkdir(childFile)
    return childFile

