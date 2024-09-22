import requests  #用于向网站发送请求  
import re
import baseSet

def net_picIDs(tag_path):
    picID_page=[]
    tag_response = requests.get(tag_path, headers=baseSet.headers, timeout=baseSet.timeout_getID) 
    if(tag_response.status_code!=200): 
        print("Get_picID_NetWrong:",tag_response.status_code)
        return False,picID_page
    tag_content = tag_response.text.replace('\n', '')
    # write_func.write_tagContent(tag_content)
    picID_page += re.findall(r'<a class="thumb" href="/post/show/(\d+)" >', tag_content)
    return True,picID_page

def net_picPaths(post_path):
    picPath_tag=[]
    post_response = requests.get(post_path, headers=baseSet.headers, timeout=baseSet.timeout_getPath)  
    if(post_response.status_code!=200):
        print("Get_picPath_NetWrong:",post_response.status_code)
        return False,picPath_tag
    post_content = post_response.text.replace('\n', '')
    # write_func.write_postContent(post_content)
    picPath_tag += re.findall(r'src="'+baseSet.pic_root_path+r'(.*?)"', post_content)
    return True,picPath_tag

def download_pic(true_path,pic_local):
    pic_response = requests.get(true_path, headers=baseSet.headers, timeout=baseSet.timeout_getPic)  
    # print(pic_response.status_code)
    if(pic_response.status_code!=200):
        print("Download_pic_NetWrong:",pic_response.status_code)
        return False
    with open(pic_local, 'wb') as f_pic:#把图片数据写入本地，wb表示二进制储存
        for pic_chunk in pic_response.iter_content(chunk_size=128):
            f_pic.write(pic_chunk)
    return True