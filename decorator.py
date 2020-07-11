import time


# def func1(func):
# 	def func2():
# 		print('begin call')
# 		return func()
# 	return func2

# @func1	
# def p():
# 	print("This is p")

# p()

def get_time(func):
	def wrapper():
		t1 = time.time()
		res = func()
		t2 = time.time()
		print(t2 - t1)
		print(res)
	return wrapper

def is_prime(num):
	if num < 3:
		return True
	for i in range(2, num):
		if num % i == 0:
			return False
	return True

@get_time
def get_prime():
	count = 0
	for i in range(1,10000):
		if is_prime(i):
			count += 1
			print(i)
	return count

get_prime()