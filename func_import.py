import os
import sys

dir0=os.path.dirname(__file__)
dir_func=os.path.join(dir0,'funcAll')
# print("dir_func:",dir_func)
sys.path.append(dir_func)

from funcAll import *

# import types
# # 列出已导入的模块
# imported_modules = [name for name, obj in globals().items() if isinstance(obj, types.ModuleType)]
# for module in imported_modules:
#     print(module)
