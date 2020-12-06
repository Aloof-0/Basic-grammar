# 1、Python time time()方法
'''
Python time time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
time()方法语法：
time.time()
举例：'''

import time
print(time.time())
# 输出：1513913514.53

# 2 、Python time localtime()方法
'''
Python time localtime() 函数类似gmtime()，作用是格式化时间戳为本地的时间。 如果sec参数未输入，则以当前时间为转换标准。 DST (Daylight Savings Time) flag (-1, 0 or 1) 是否是夏令时。
localtime()方法语法：
time.localtime([ sec ])
举例：'''

import time

print(time.localtime())
print(time.localtime(time.time()))
# 输出：
# time.struct_time(tm_year=2017, tm_mon=12, tm_mday=22, tm_hour=11, tm_min=42, tm_sec=36, tm_wday=4, tm_yday=356, tm_isdst=0)
# time.struct_time(tm_year=2017, tm_mon=12, tm_mday=22, tm_hour=11, tm_min=42, tm_sec=36, tm_wday=4, tm_yday=356, tm_isdst=0)

# 3、Python time asctime()方法
'''
Python time asctime() 函数接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串
asctime()方法语法：
time.asctime([t])  #t -- 9个元素的元组或者通过函数 gmtime() 或 localtime() 返回的时间值
举例：'''
import time

t = time.localtime()
print("time.asctime(t): %s " % time.asctime(t))
# 输出：
# time.asctime(t): Fri Dec 22 11:28:47 2017

# 4、Python time ctime()方法
'''
Python time ctime() 函数把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。 如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于 asctime(localtime(secs))。该函数没有任何返回值。
ctime()方法语法：
time.ctime([ sec ])   #sec -- 要转换为字符串时间的秒数。
举例：'''
import time
t = time.localtime()
print(time.asctime(t))
print(time.ctime())
# 输出：
# Fri Dec 22 14:19:36 2017
# Fri Dec 22 14:19:36 2017

# 5、Python time strftime()方法
'''
Python time strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定。
strftime()方法语法：
time.strftime(format[, t])
参数说明：
format -- 格式字符串。
t -- 可选的参数t是一个struct_time对象
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
举例：'''

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# 输出：
# time.struct_time(tm_year=2017, tm_mon=12, tm_mday=22, tm_hour=14, tm_min=3, tm_sec=2, tm_wday=4, tm_yday=356, tm_isdst=0)
# 2017-12-22 14:03:02
# Fri Dec 22 14:03:02 2017

#6、Python time sleep()方法
'''
Python time sleep() 函数推迟调用线程的运行，可通过参数secs指秒数，表示进程挂起的时间
sleep()方法语法：
time.sleep(t)  #t -- 推迟执行的秒数。
举例：'''

import time
print("Start : %s" % time.ctime())
time.sleep(5)
print("End : %s" % time.ctime())
# 输出：
# Start : Fri Dec 22 14:21:54 2017
# End : Fri Dec 22 14:21:59 2017