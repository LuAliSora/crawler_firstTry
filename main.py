import getPath_func
import getPic_func


if __name__=="__main__":
    mode=input("Mode:1.getPath;2.getPic;#:")
    if mode=="1":
        getPath_func.getPath_main()
    elif mode=="2":
        getPic_func.get_PicInTag()
    else :
        print("Wrong!")
        


