from pathlib import Path
import re

import baseSet


def makeFolder(fileL):
    tempPath=Path(*fileL)
    if tempPath.is_dir()==False:
        tempPath.mkdir()
    # print(tempPath)
    return str(tempPath)


def read_tags():
    filePath=baseSet.recSave+"tags.txt"
    with open(filePath, "r", encoding='utf-8') as f_tags: 
        tag_list=f_tags.read().splitlines()
    return tag_list


def readList_inTag(tag, idx):
    filePath=baseSet.recSave+f"{tag}/"+baseSet.listName[idx]
    with open(filePath, "r", encoding='utf-8') as f_recTL:    
        picData=f_recTL.read().splitlines()
    return picData


def writePage(content, idx):
    filePath=baseSet.recSave+baseSet.pageName[idx]
    with open(filePath, "w", encoding='utf-8') as f_recP:    
        f_recP.write(content)


def writeList_inTag(content, tag, idx):
    filePath=baseSet.recSave+f"{tag}/"+baseSet.listName[idx]
    with open(filePath, "w", encoding='utf-8') as f_recTL:    
        [f_recTL.write(picData+'\n') for picData in content]


def get_picType(pic_net):
    pattern = r'\.(jpg|png|bmp)$'
    return re.search(pattern, pic_net).group()  

