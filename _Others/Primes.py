import time

lower = 0
upper = 10 # * 1000 * 1000 * 1000 * 1000

print(time.localtime())
print(time.ctime())

print("Prime numbers between", lower, "and", upper, "are:")
seconds = time.time()
local_time = time.ctime(seconds)
print("Local time:", local_time)

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
seconds = time.time()
local_time = time.ctime(seconds)
print("Local time:", local_time)
