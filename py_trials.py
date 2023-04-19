# Write a Python function that takes a list of integers as input and 
# returns the sum of all the even numbers in the list.

def total(*intergers):
    addition = 0
    for i in intergers:
        if i%2 == 0:
            addition += i
    return addition


# Write a Python function that takes a string 
# as input and returns a list of all the words in the string 
# that have more than three letters

def stings_list(words):
    words2 = (words.split())
    output = [word for word in words2 if len(word) > 3 ]
    return output

# Write a Python program that takes a list of numbers 
# as input and sorts the list in descending order.

# def sorting_array(**kwargs):
#     output_list = []
#     for i in kwargs.values:
#         if i in 

# checking if a number is a prime number 
def prime_numbers (numbers):
    primes = []
    l = len(numbers)
    for num in range(0,l):
        c = 0
        for x in range (2, numbers[num]):
            if numbers[num] % x == 0:
                c =1
                break
        if c == 0:
            primes.append(num)  
    return primes

        
print(prime_numbers([5,6,3,8,13,15,17,19]))

my_list = [5,6,3,8,13,15,17,19]
print(my_list)
l = len(my_list)
for i in range(0,l):
    