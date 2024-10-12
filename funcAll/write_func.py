import baseSet
from pathlib import Path


def makeFolder(fileL):
    tempPath=Path(*fileL)
    if tempPath.is_dir()==False:
        tempPath.mkdir()
    print(tempPath)
    return str(tempPath)

def writePage(content, idx):
    filePath=baseSet.recSave+baseSet.pageName[idx]
    with open(filePath, "w", encoding='utf-8') as f_recP:    
        f_recP.write(content)


def writeList_inTag(content, tag, idx):
    filePath=baseSet.recSave+f"{tag}/"+baseSet.listName[idx]
    with open(filePath, "w", encoding='utf-8') as f_recTL:    
        [f_recTL.write(picData+'\n') for picData in content]

