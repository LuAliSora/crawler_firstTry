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
        "--pSt",
        type=int,
        default=1,
        help="PageStart>=1"
    )
    parser.add_argument(
        "--pN",
        type=int,
        default=1,
        help="PageNum>=1"
    )
    # print(parser.parse_args())
    return parser.parse_args()

def main():
    args=get_args()
    if(args.pSt<1 or args.pN<1):
        raise Exception("PageStart must >=1; PageNum must >=1")
    
    ppwork=PtoP_class.PathToPic(args.imgQ)
    ppwork.pp_main(args.mode, args.pSt, args.pN)
    

if __name__=="__main__":
    main()