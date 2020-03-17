# from access_limited import Student
#
# stu = Student('Bob', '20', '18')
# stu.shuchu()

movie = '大侦探'
count = 5
ticket = 14.9
total = count * ticket



message = '''
电影；{0}
人数：{2}
单价：{1}
总价：{3}
'''.format(movie, count, ticket, total)

print(message)