import argparse

from func_import import *
import PtoP_class

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--mode",
        type=int,
        default=0,
        choices=(0, 1),
        help="Mode: 0->GetPath&&LoadPic; 1->LoadPic"
    )
    parser.add_argument(
        "--imgQ",
        type=int,
        default=0,
        choices=(0, 1),
        help="Image quality: 0->Low; 1->High"
    )
    parser.add_argument(
        "--pageS",
        type=int,
        default=1,
        help="pageStart>=1"
    )
    parser.add_argument(
        "--pageN",
        type=int,
        default=1,
        help="pageNum>=1"
    )
    # print(parser.parse_args())
    return parser.parse_args()

def main():
    args=get_args()
    if(args.pageS<1 or args.pageN<1):
        raise Exception("pageStart must >=1; pageNum must >=1")
    
    ppwork=PtoP_class.PathToPic(args.imgQ)
    ppwork.pp_main(args.mode, args.pageS, args.pageN)
    

if __name__=="__main__":
    main()