import random

# 1.random() 方法返回随机生成的一个实数，它在[0,1)范围内
print(random.random())

# 2.uniform(C, D) //产生  C 到 D 之间的随机浮点数，区间可以不是整数
print(random.uniform(1, 5))

# 3. randint(a, b) //产生 a 到 b 的一个整数型随机数(包括b)
print(random.randint(1, 10))

# 4.choice(['adbbmcz']) // 从序列中随机选取一个元素
print(random.choice('tomorrow'))


# 5.sample(['adbbmcz'],2) //从序列中随机选取两个元素(可定义)
print(random.sample('adbbmcz', 2))
print(random.sample(['123', 'abc', 52, [1, 2]], 2))
