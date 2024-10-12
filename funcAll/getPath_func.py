import baseSet
import write_func
import read_func
import netRes_func

def get_tagPicID(tag,pageStart,pageEnd):
    picID_list=[]
    stateIdx=0
    for page in range(pageStart,pageEnd):
        tagPage_str=f"?page={page}&tags="+tag
        print(tagPage_str)
        tagPage_path=baseSet.web_root_path+tagPage_str
        flag, picID_res=netRes_func.net_picData(tagPage_path, idx=stateIdx)
        if flag==False:
            break
        picID_list +=picID_res
    write_func.writeList_inTag(picID_list, tag, idx=stateIdx)
    return len(picID_list)


def get_tagPicPath(tag):
    picID_list=read_func.read_picIDs()
    picPath_list=[]
    stateIdx=1
    for i,pid in enumerate(picID_list):
        post_path=baseSet.web_root_path+f"/show/{pid}"
        flag, picPath_res=netRes_func.net_picData(post_path, idx=stateIdx)
        if flag==False:
            break
        picPath_list+=picPath_res
        if i%10==0:
            print("get_picPath_Num:",i+1)
    write_func.writeList_inTag(picID_list, tag, idx=stateIdx)
    return len(picPath_list)


def getPath_main():
    # write_func.init_record()
    pageStart=int(input("pageStart:"))
    pageNum=int(input("pageNum:"))
    tags_list=read_func.read_tags()
    for i,tag in enumerate(tags_list):
        print(i,":",tag)
        write_func.makeFolder([baseSet.recSave, tag])
        picIDNum=get_tagPicID(tag, pageStart, pageStart+pageNum)
        picPathNum=get_tagPicPath()
        picSum=min(picIDNum,picPathNum)
        write_func.writeList_inTag([str(picSum)], tag, idx=2)
    



    


            
