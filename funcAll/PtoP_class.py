import baseSet
import localF_func
import netRes_func


class PathToPic:
    def __init__(self):
        self.tag_list= localF_func.read_tags()
        self.picID_list=[]
        self.picPath_list=[]
        # write_func.init_record()
    
    def get_tagPicID(self, tag, pageStart, pageEnd):
        picID_list=[]
        stateIdx=0
        for page in range(pageStart,pageEnd):
            tagPage_str=f"?page={page}&tags="+tag
            print(tagPage_str)
            tagPage_path=baseSet.web_root_path+tagPage_str
            flag, picID_res=netRes_func.net_picData(tagPage_path, idx=stateIdx)
            if flag==False:
                break
            picID_list+=picID_res
        # write_func.writeList_inTag(picID_list, tag, idx=stateIdx)
        self.picID_list.append(picID_list)

    def get_tagPicPath(self, tagIndex):
        tag=self.tag_list[tagIndex]
        # picID_list=read_func.readList_inTag(tag, idx=0)
        picID_list=self.picID_list[tagIndex]
        picPath_list=[]
        stateIdx=1
        for i, pid in enumerate(picID_list):
            post_path= baseSet.web_root_path+f"/show/{pid}"
            flag, picPath_res=netRes_func.net_picData(post_path, idx=stateIdx)
            if flag==False:
                break
            picPath_list+=picPath_res
            if i%10==0:
                print("get_picPath_Num:",i+1)
        # write_func.writeList_inTag(picID_list, tag, idx=stateIdx)
        self.picPath_list.append(picPath_list)

    def get_PicInTag(self, tagIndex):
        tag=self.tag_list[tagIndex]
        tagFolder= localF_func.makeFolder([baseSet.picSave, tag])
        
        pair_inTag=zip(self.picID_list[tagIndex],self.picPath_list[tagIndex])
        for i, data in enumerate(pair_inTag):
            id, path=data[0], data[1]
            pic_local=tagFolder+f"/{id}.jpg"
            true_path=baseSet.pic_root_path+path
            flag=netRes_func.download_pic(true_path, pic_local)
            if i%10==0:
                print("download_pic_Num:", i+1)
            if flag==False:
                break


    def pp_main(self):
        pageStart=int(input("pageStart:"))
        pageNum=int(input("pageNum:"))

        localF_func.makeFolder([baseSet.picSave])
        
        for i,tag in enumerate(self.tag_list):
            localF_func.makeFolder([baseSet.recSave, tag])
            self.get_tagPicID(tag,pageStart,pageStart+pageNum)
            self.get_tagPicPath(i)
            self.get_PicInTag(i)




    
