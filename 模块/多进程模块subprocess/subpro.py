# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 22:14
# @Author   : 高冷
# @FileName  : subprocess.py

import subprocess

a = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE)
print(a)

print(str(a.stdout.read(), "Gbk"))
