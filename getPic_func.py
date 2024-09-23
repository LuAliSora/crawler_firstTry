import baseSet
import read_func
import write_func
import netRes_func




def get_PicInTag():
    tags_list=read_func.read_tags()
    picSum_list=read_func.read_picSum()

    picID_list=read_func.read_picIDs()
    picPath_list=read_func.read_picPath()

    tag_index=-1
    picBatch=0
    childFile=""

    for i,data in enumerate(zip(picID_list,picPath_list)):
        id,path=data[0],data[1]
        if i>=picBatch:
            tag_index+=1
            childFile=write_func.make_tagFile(tags_list[tag_index])
            picBatch+=int(picSum_list[tag_index])
            print(tags_list[tag_index],i,picBatch)
        pic_local=childFile+id+'.jpg'
        true_path=baseSet.pic_root_path+f"{path}"
        netRes_func.download_pic(true_path,pic_local)
        if i%10==0:
            print("download_pic_Num:",i+1)





