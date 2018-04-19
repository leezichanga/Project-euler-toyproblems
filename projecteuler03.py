#Solution 1
import math

number= 13195
#root = math.sqrt(number)

def get_prime(number):
    number_list=[num for num in range(1,number+1)]
    prime = []

    while True:
        if len(number_list)>0:

            # Get prime numbers
            round_prime = number_list[0]

            # append to prime array
            if round_prime >1:
                prime.append(round_prime)

            # remove divisible numbers
            for num in number_list:
                if num % number_list[0] == 0:
                    number_list.remove(num)
        else:
            break
    return prime


#Another solution 2
def get_prime_list(prime_list,number):

    prime_divisible_list=[]

    start = 0

    while True:
        if number > 0 and start<len(prime_list):
            if number % prime_list[start]==0:
                number = number // prime_list[start]
                prime_divisible_list.append(prime_list[start])
            else:
                start += 1
        else:
            break
    return prime_divisible_list

prime=get_prime(number)
prime_list = get_prime_list(prime,number)

print(max(prime_list))
