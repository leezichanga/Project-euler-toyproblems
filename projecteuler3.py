import math

def isPrime(x):
   if (x is 2) or (x is 3):
       return True
   if (x is 1) or (x%2 is 0):
       return False
   for i in range(3,int(math.sqrt(x)+1),2):
       if (x%i is 0):
        return False
   return True

number = 600851475143
largestFactor = 1

for i in range(3,int(math.sqrt(number)),2):
    if (number%i is 0):
        print  "Factor: " + str(i)
        if isPrime(i):
            print "        ^^^^ Prime"
            if (i > largestFactor):
                largestFactor = i
        print "Factor: " + str(number/i)
        if (isPrime(number/i)):
            largestFactor = number/i
            print "        ^^^^ Prime"

print "The largest prime factor of 600,851,475,143 is " + str(largestFactor) + "."
