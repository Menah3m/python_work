# Name:access_limited
# Author:Yasu
# Time:2020/3/14

class Student(object):
    def __init__(self, name, score, age):
        self.__name = name
        self.__score = score
        self.__age = age

    def shuchu(self):
        print('%s 的分数是 %s' %(self.__name, self.__score))

if __name__ == '__main__':
    stu = Student('Alice', '80', '18')
    stu.shuchu()




