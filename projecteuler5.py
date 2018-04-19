def smallest_m():
	start=1
	while True:
		if start%2==0 and start%3==0 and start%4==0 and start%5==0 and start%5==0 and start%6==0 and start%7==0 and start%8==0 and start%9==0 and start%10==0 and start%11==0 and start%12==0 and start%13==0 and start%14==0 and start%15==0 and start%16==0 and start%17==0 and start%18==0 and start%19==0 and start%20==0:
			print(start)
			break
		else:
			start+=1
start_point =1
input_number = 10

def range_generator(input):

    range_list=list(range(1,input+1))
    return range_list

def increment_start():
    global start_point

    start_point+=1

def is_divisible(number1,number2):
    if number1 % number2 == 0:
        return True
    else:
        return False

range_list = range_generator(input_number)
index_counter = 0

while index_counter < len(range_list):

    print(index_counter)

    if is_divisible(start_point,range_list[index_counter]):
         index_counter +=1
         continue
    else:
        index_counter = 0
        increment_start()

print(start_point)
