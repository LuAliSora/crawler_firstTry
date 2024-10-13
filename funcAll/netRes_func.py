import requests  #用于向网站发送请求  
import re
from pathlib import Path

import baseSet
import localF_func


def net_picData(path, modeIdx, picQ_idx=0):
    picData=[]
    page_response = requests.get(path, headers=baseSet.headers, timeout=baseSet.timeoutL[modeIdx])
    if(page_response.status_code!=200): 
        print(f"picData_NetWrong[{modeIdx}]:", page_response.status_code)
        return False, picData
    content = page_response.text.replace('\n', '')
    # localF_func.writePage(content, idx=modeIdx)
    if modeIdx==0:
        picData += re.findall(baseSet.preName[modeIdx], content)
    elif modeIdx==1:
        picData += re.findall(baseSet.preName[modeIdx+picQ_idx], content)
    # print(f"picData[{modeIdx}]",picData)
    return True, picData


def download_pic(pic_net, pic_local, picQ_idx):
    if Path(pic_local).is_file():
        return True, 1
    modeIdx=2
    pic_response = requests.get(pic_net, headers=baseSet.headers, timeout=baseSet.timeoutL[modeIdx+picQ_idx])  
    # print(pic_response.status_code)
    if(pic_response.status_code!=200):
        print("Download_pic_NetWrong:",pic_response.status_code)
        return False, 0
    with open(pic_local, 'wb') as f_pic:#把图片数据写入本地，wb表示二进制储存
        for pic_chunk in pic_response.iter_content(chunk_size=128):
            f_pic.write(pic_chunk)
    return True, 0

