#计算1-1000000的和
big_numbers=[value for value in range(1,1000001)]#创建1-1000000的列表
sum=0
print(min(big_numbers))#确保最小数为1 
print(max(big_numbers))#确保最大数为1000000

for number in big_numbers:
    sum=sum+number

print(sum)
