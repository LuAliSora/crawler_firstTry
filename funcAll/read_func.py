import baseSet

def read_picIDs():
    with open(baseSet.file_save+"picIDs.txt", "r", encoding='utf-8') as f_pid_r: 
        picID_list =f_pid_r.read().splitlines()
    return picID_list

def read_tags():
    with open(baseSet.file_save+"tags.txt", "r", encoding='utf-8') as f_tags: 
        tag_list=f_tags.read().splitlines()
    return tag_list

def read_picPath():
    with open(baseSet.file_save+"picPaths.txt", "r", encoding='utf-8') as f_pPath_r:
        picPath_list =f_pPath_r.read().splitlines()
    return picPath_list

def read_picSum():
    with open(baseSet.file_save+"picSum.txt", "r", encoding='utf-8') as f_picSum: 
        picSum_list=f_picSum.read().splitlines()
    return picSum_list