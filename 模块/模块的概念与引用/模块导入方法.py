# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 23:30
# @Author   : 高冷
# @FileName  : 模块导入方法.py


# 1.import 语句                       import module1[, module2[,... moduleN]
import time
print(time.time())

# 2.from…import 语句                  这个声明不会把整个modulename模块导入到当前的命名空间中，只会将它里面的name1或name2单个引入到执行这个声明的模块的全局符号表。
from text import blue
blue()

# 3.From…import* 语句                  不好 容易被覆盖
from text import *
blue()                                  # 这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。大多数情况， Python程序员不使用这种方法，因为引入的其它来源的命名，很可能覆盖了已有的定义。
