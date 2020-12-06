# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 23:14
# @Author   : 高冷
# @FileName  : os系统模块.py


import os

# 获取当前目录绝对路径
# 1.
dir_path = os.path.dirname(os.path.abspath(__file__))
print('当前目录绝对路径:', dir_path)
# 2.
print(__file__)

# 获取上级目录绝对路径 os.path.dirname
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('上级目录绝对路径:', dir_path)

# 获取上上级目录绝对路径
dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print('上级目录绝对路径:', dir_path)
