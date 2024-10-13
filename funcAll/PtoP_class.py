import baseSet
import localF_func
import netRes_func


class PathToPic:
    def __init__(self):
        self.tag_list= localF_func.read_tags()
        self.picID_list=[]
        self.picPath_list=[]
        self.picQ_idx=0
        # write_func.init_record()
    
    def clearList(self):
        self.picID_list=[]
        self.picPath_list=[]

    def get_tagPicID(self, tag, pageStart, pageEnd):
        picID_list=[]
        modeIdx=0
        for page in range(pageStart,pageEnd):
            tagPage_str=f"?page={page}&tags="+tag
            print(tagPage_str)
            tagPage_path=baseSet.web_url+tagPage_str
            flag, picID_res=netRes_func.net_picData(tagPage_path, modeIdx)
            if flag==False:
                break
            picID_list+=picID_res
        localF_func.writeList_inTag(picID_list, tag, idx=modeIdx)
        self.picID_list=picID_list

    def get_tagPicPath(self, tag):
        # picID_list=read_func.readList_inTag(tag, idx=0)
        picPath_list=[]
        modeIdx=1
        for i, pid in enumerate(self.picID_list):
            post_path= baseSet.web_url+f"/show/{pid}"
            flag, picPath_res=netRes_func.net_picData(post_path, modeIdx, self.picQ_idx)
            if flag==False:
                break
            picPath_list+=picPath_res
            if i%10==0:
                print("Get_picPath_Num:",i+1)
        localF_func.writeList_inTag(picPath_list, tag, idx=modeIdx)
        self.picPath_list=picPath_list

    def get_PicInTag(self, tag):
        if len(self.picID_list)*len(self.picPath_list)==0:
            self.picID_list=localF_func.readList_inTag(tag, idx=0)
            self.picPath_list=localF_func.readList_inTag(tag, idx=1)

        pair_inTag=zip(self.picID_list,self.picPath_list)
        tagFolder= localF_func.makeFolder([baseSet.picSave, tag])

        repeatNum=0
        for i, data in enumerate(pair_inTag):
            id, pic_net=data[0], data[1]
            pic_local=tagFolder+f"/{id}"+localF_func.get_picType(pic_net)
            # print(pic_local)
            res=netRes_func.download_pic(pic_net, pic_local, self.picQ_idx)
            if res[0]==False:
                break
            repeatNum+=res[1]
            if i%10==0:
                print("Download, Repeat (Num):", i+1-repeatNum, repeatNum)


    def pp_main(self):
        self.picQ_idx=int(input("picQuality(0 < 1):"))
        state=int(input("Mode(0->GetPath&&LoadPic; 1->LoadPic;):"))
        pageStart=int(input("PageStart:"))
        pageNum=int(input("PageNum:"))

        localF_func.makeFolder([baseSet.picSave])
        
        for i,tag in enumerate(self.tag_list):
            print(f"[{i}]: {tag}")
            self.clearList()
            if state==0:
                localF_func.makeFolder([baseSet.recSave, tag])
                self.get_tagPicID(tag, pageStart, pageStart+pageNum)
                self.get_tagPicPath(tag)
            self.get_PicInTag(tag)




    
