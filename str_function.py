# Name:str_function
# Author:Yasu
# Time:2020/3/13

'''
----------------关于str类型数据的各种方法-------------------
    字符串连接  +
    查找字符    index()
    查找子字符串  find('sub-str')
    字符串格式化   's%' % (str)
    在队列中添加元素  join()
    拆分字符串      split()
    小写字母化     lower()
    字符替换     replace()
    去掉两头的空格    strip()
'''

print('-'*80)

###### 字符串连接 + ########
s1 = 'abc'
s2 = 'def'
s1 += s2
print('字符串连接结果：',s1)
print('-'*80)

###### 查找字符  #####
s3 = 'c'
print('c所在位置：',s1.find(s3))
print('-'*80)

###### 字符串格式化 #####
print('[%s] is [%s] years old !' % ('Alice',18))
print('-'*80)

##### 查找子字符串   ######
title = 'python is good'
print('python字符串最左索引为',title.find('python'))
print('good字符串最左索引为',title.find('good'))
print('-'*80)

####### 在字符串队列中添加元素 #########
seq = ['1','2','3','4','5']
sep = '+'
print('字符串连接结果：',sep.join(seq))
print('-'*80)

####### 替换字符 #########
s = 'ddddddddddddddd the  aaaaaabbbbbbb'.replace('a','c')
print('用c替换a后的结果：',s)
print('-'*80)

####### 分割字符串  #########
S = '1+2+3+4+5'.split('+')
print('字符串分割的结果：',S)
print('-'*80)


###### 取出两侧空格 #######
print('去掉两侧空格的结果','  dfd  dfsf  '.strip())
print('-'*80)