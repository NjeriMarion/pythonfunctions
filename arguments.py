def year_of_birth(name, age):
    year = 2023 - age
    return(f"Hello {name}, you were born in {year}")

def my_country(country = "kenya"):
    print(f"Hello,you are from {country}")

def hello(* names):
    for name in names:
        print(f"Hello {name}")

def addition(*nums):
    output = 0
    for num in nums:
        output += num
    return output    
def multiply_many(**kwargs):
    output2 = 1
    for value in kwargs.values():
        output2 *= value
    return output2

# A function named concatenate_args that takes any 
# number of string arguments in positional arguments format and concatenates them into a single string
def concatenate_args(*any_strings):
    string_output = ""
    for i in any_strings:
        string_output = string_output + i
    return string_output

# A function named concatenate_kwargs that takes any number of string arguments in keyword arguments  format 
# and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    string_output2 = ""
    for k in kwargs.values():
        string_output2 = string_output2 + k
    return string_output2