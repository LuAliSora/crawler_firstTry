import baseSet
import write_func
import read_func
import netRes_func

def pages_in_tag(tag,pageStart,pageEnd):
    picID_list=[]
    for page in range(pageStart,pageEnd):
        PageAndTag_str=rf"?page={page}&tags="+tag
        # print(PageAndTag_str)
        tag_path=baseSet.web_root_path+PageAndTag_str
        flag,picID_res=netRes_func.net_picIDs(tag_path)
        # print(picID_res)
        if flag==False:
            break
        picID_list +=picID_res
    write_func.write_picIDs(picID_list) 
    return len(picID_list)


def get_picPath():
    picID_list=read_func.read_picIDs()
    picPath_list=[]
    for i,pid in enumerate(picID_list):
        post_path=baseSet.web_root_path+rf"/show/{pid}"
        flag,picPath_res=netRes_func.net_picPaths(post_path)
        # print(picPath_res)
        if flag==False:
            break
        picPath_list+=picPath_res
        if i%10==0:
            print("get_picPath_Num:",i+1)
    write_func.write_picPaths(picPath_list)
    return len(picPath_list)



def getPath_main():
    write_func.init_record()
    picSum_list=[]
    pageStart=int(input("pageStart:"))
    pageNum=int(input("pageNum:"))
    tags_list=read_func.read_tags()
    for i,tag in enumerate(tags_list):
        picIDNums=pages_in_tag(tag,pageStart,pageStart+pageNum)
        picPathNums=get_picPath()
        picSum_list.append(str(min(picIDNums,picPathNums)))
        print("picSum_list:",picSum_list)
    write_func.write_picSum(picSum_list)
    



    


            
