
import write_func
import read_func
import netRes_func
import baseSet

class PathToPic:
    def __init__(self):
        self.tag_list=read_func.read_tags()
        self.picID_list=[]
        self.picPath_list=[]
        write_func.init_record()
    
    def pages_in_tag(self,tag,pageStart,pageEnd):
        picID_tag=[]
        for page in range(pageStart,pageEnd):
            PageAndTag_str=rf"?page={page}&tags="+tag
            print(PageAndTag_str)
            tag_path=baseSet.web_root_path+PageAndTag_str
            flag,picID_res=netRes_func.net_picIDs(tag_path)
            # print(picID_res)
            if flag==False:
                break
            picID_tag +=picID_res
        # write_func.write_picIDs(picID_tag) 
        self.picID_list.append(picID_tag)

    def get_picPath(self,tagIndex):
        picPath_tag=[]
        for i,pid in enumerate(self.picID_list[tagIndex]):
            post_path=baseSet.web_root_path+rf"/show/{pid}"
            flag,picPath_res=netRes_func.net_picPaths(post_path)
            # print(picPath_res)
            if flag==False:
                break
            picPath_tag+=picPath_res
            if i%10==0:
                print("get_picPath_Num:",i+1)
        # write_func.write_picPaths(picPath__tag)
        self.picPath_list.append(picPath_tag)

    def get_PicInTag(self,tagIndex):
        childFile=write_func.make_tagFile(self.tag_list[tagIndex])
        pair_inTag=zip(self.picID_list[tagIndex],self.picPath_list[tagIndex])
        for i,data in enumerate(pair_inTag):
            id,path=data[0],data[1]
            pic_local=childFile+id+r'.jpg'
            true_path=baseSet.pic_root_path+rf"{path}"
            pic_falg=netRes_func.download_pic(true_path,pic_local)
            if i%10==0:
                print("download_pic_Num:",i+1)
            if pic_falg==False:
                break


    def pp_main(self):
        pageStart=int(input("pageStart:"))
        pageNum=int(input("pageNum:"))
        for i,tag in enumerate(self.tag_list):
            self.pages_in_tag(tag,pageStart,pageStart+pageNum)
            self.get_picPath(i)
            self.get_PicInTag(i)




    
