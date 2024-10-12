import baseSet

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
