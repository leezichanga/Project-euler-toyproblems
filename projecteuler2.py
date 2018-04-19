#Solution 1
numbers = [1, 2]
total = 0

for i in range(4000000):
    if i == numbers[-1] + numbers[-2]:
        numbers.append(i)

for n in numbers:
    if n % 2 == 0:
        total += n

print(total)


#Solution 2
#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
   fib_start =[1,2] #create the first 2 fibonnaci numbers
   total = 0 #create default total value
   n = int(input().strip())

   while True: #while loop to append the next numbers in the sequence
       fib_next = fib_start[-1] +fib_start[-2]
       if fib_next < n:
           fib_start.append(fib_next)
       else:

           break

   for number in fib_start: #for loop to add the even digits
       if number % 2 == 0:
           total += number

   print (total)
