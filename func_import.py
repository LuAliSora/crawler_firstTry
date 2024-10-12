from pathlib import Path
import sys

partL=['funcAll']

def addPart(partList)->None:
    tempDir=Path.cwd()
    while 1:
        if tempDir.name=='crawler_firstTry':
            break
        if tempDir==tempDir.parent:
            raise Exception("root_path: Lose!")
        tempDir=tempDir.parent
    # print("root_path:",tempDir)
    [sys.path.append(str(tempDir/part)) for part in partList]

addPart(partL)

if __name__=="__main__":
    # addPart(partL)
    print(sys.path)
    # import types
    # # 列出已导入的模块
    # imported_modules = [name for name, obj in globals().items() if isinstance(obj, types.ModuleType)]
    # for module in imported_modules:
    #     print(module)