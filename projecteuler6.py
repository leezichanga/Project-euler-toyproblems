#Solution 1
def squares(num):
    total = []
    for i in range(1,num+1):
        prod = (i*i)
        total.append(prod)
        you=sum(total)
    return you
squares(10)
def sum_squares(num):
    total = []
    for i in range(1,num+1):
        total.append(i)
        you=sum(total)
    return you**2
sum_squares(10)
def diff(a,b):
    difference = a-b
    print(difference)
diff(sum_squares(10),squares(10))


#Solution 2
def sum_of_square(limit):
    my_list = []
    start = 1
    while start<=limit:
        square = start*start
        my_list.append(square)
        start+=1
        p = sum(my_list)
        if len(my_list)==limit:
            m = sum(my_list)
    return (m)

def square_of_sum(limit):
    list = []
    for a in range(1,limit +1):
        list.append(a)
        p = sum(list)
        if len(list)==limit:
            print()
    return p*p

def difference(limit):
    num_sum = (square_of_sum(limit))-(sum_of_square(limit))
    print(num_sum)

difference(10)
