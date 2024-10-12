import baseSet
import read_func
import write_func
import netRes_func




def get_PicInTag(tag):
    picID_list=read_func.readList_inTag(tag, idx=0)
    picPath_list=read_func.readList_inTag(tag, idx=1)
    # picSum_list=read_func.readList_inTag(tag, idx=2)

    tagFolder= write_func.makeFolder([baseSet.picSave, tag])

    pair_inTag=zip(picID_list,picPath_list)
    for i, data in enumerate(pair_inTag):
        id, path=data[0], data[1]
        pic_local=tagFolder+f"/{id}.jpg"
        true_path=baseSet.pic_root_path+path
        flag=netRes_func.download_pic(true_path, pic_local)
        if i%10==0:
            print("download_pic_Num:", i+1)
        if flag==False:
            break

def getPic_main():
    tags_list=read_func.read_tags()
    for i,tag in enumerate(tags_list):
        print(i,":",tag)
        get_PicInTag(tag)



