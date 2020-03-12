# Name:__function.py
# Author:Yasu
# Time:2020/3/12

from functools import reduce
'''
-------------------【 map函数 】--------------------------------------------
map函数 接受两个参数：Function 和 Iterable
        map函数将传入的函数依次作用到可迭代对象的每个元素，
        并将结果作为新的 Iterator返回
'''
def square(num):
    return num * num

def upper(str):
    return str.upper()

map_res1 = list(map(square, range(10)))
map_res2 = list(map(upper,'abddddf'))
print(map_res1)
print(map_res2)

'''
-------------------【 reduce函数 】--------------------------------------------
reduce函数 接受两个参数：Function 和 Sequence
        map函数将传入的函数依次作用到序列的每个元素，
        并将结果与下个元素继续作用
    注：python3中移除了reduce函数，放入了functools模块中
      使用时需导入: from functools import reduce
example:
    将[1,3,5,7,9]合并成整数 13579
'''
def fn(a,b):
    return 10 * a + b

reduce_res = reduce(fn,[1,3,5,7,9])

print(reduce_res)