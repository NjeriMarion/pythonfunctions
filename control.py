def even_numbers():
    x = range(10)
    for i in x:
        if i % 2 == 0:
            print(i)

def even_two():
    b = range(20)
    for i in b:
        if i % 2 == 0:
            print(i)   
        else:
            print(f"{i}is an odd number")   

def odd_numbers():
    r = range(20)
    for x in r:
        if x % 2 != 0:
            print(x) 

def divisible_by_five():
    y = range(50)
    for i in y :
        if i % 5 ==0:
            print(f"{i} is divisible by 5")
        else:
            print(f"{i} is not divisible by 5")  


def multiple_comparison():
    y = range(50)
    for i in y :
        if i % 5 ==0:
            print(f"{i} is divisible by 5")
        elif i % 7 ==0:
            print(f"{i} is divisible by 7")
        elif i % 9 ==0:
            print(f"{i} is divisible by 9")
        else:
            print(f"{i} is not disible by 5, 7 or 9")


def odd_or_even():
    z = range(20)
    for i in z :
        if i % 2 ==0 and i % 3 ==0:
            print(f"{i} is divisible by both 2 and 3")
        elif i % 2 ==0 or i %3 ==0:
            print(f"{i} is divisible by either 2 or 3")
        else :
            print(f"{i} is nether divisible by 2 nor 3 ")


def while_loop():
    x = 1
    while x < 10 :
        print("Hello Mar")
        x+=1


def break_statement():
    x = 1
    while x < 10 :
        print(f"{x} Hello")
        x+=1     
        if x == 5:
            break

def continue_statement():
    x = 1
    while x < 20:
        x+=1
        if x % 2 != 0:
            continue
        print(x)


#  CONTROL FLOW ASSIGNMENT

# Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50. 

def even_upto_50():
    x = 0
    while x <= 50:
        x+=1
        if x %2 != 0:
            continue
        print(f"{x} is an even number")


# Write a function that takes an integer argument and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.

def prime_numbers(number):
    p = range(2, number)
    if number <= 1:
        print(f"{number} is not a prime number")
    else:
        for i in p:
            if number % i == 0:
                print(f"{number} is not a prime number")
                break
            else:
                print(f"{number} is a prime number")


# Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.

def sum_of_even(list_of_nums):
    sum = 0
    for i in list_of_nums:
        if i % 2 == 0:
            sum += i
    return sum

# Write a function that takes any two integers as input, and prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3
def sum_in_range(a,b):
    y = range(a,b+1)
    sum_all = 0
    for i in y :
        if i % 3 == 0:
            sum_all += i
    return sum_all
