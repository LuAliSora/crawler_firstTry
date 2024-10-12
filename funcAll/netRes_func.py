import requests  #用于向网站发送请求  
import re
from pathlib import Path

import baseSet
import localF_func


def net_picData(path, idx):
    picData=[]
    page_response = requests.get(path, headers=baseSet.headers, timeout=baseSet.timeoutL[idx])
    if(page_response.status_code!=200): 
        print(f"picData_NetWrong[{idx}]:", page_response.status_code)
        return False, picData
    content = page_response.text.replace('\n', '')
    localF_func.writePage(content,idx=idx)
    if idx==0:
        picData += re.findall(r'<a class="thumb" href="/post/show/(\d+)" >', content)
    elif idx==1:
        picData += re.findall(rf'src="{baseSet.pic_root_path}(.*?)"', content)
    # print(f"picData[{idx}]",picData)
    return True, picData


def download_pic(true_path, pic_local, idx=2):
    if Path(pic_local).is_file():
        return True, 1
    pic_response = requests.get(true_path, headers=baseSet.headers, timeout=baseSet.timeoutL[idx])  
    # print(pic_response.status_code)
    if(pic_response.status_code!=200):
        print("Download_pic_NetWrong:",pic_response.status_code)
        return False, 0
    with open(pic_local, 'wb') as f_pic:#把图片数据写入本地，wb表示二进制储存
        for pic_chunk in pic_response.iter_content(chunk_size=128):
            f_pic.write(pic_chunk)
    return True, 0