'''def functionname(arg1, arg2):
    stsmt
    return  [optional]


functionname(parameter)'''

# def gst(price):
#     print("Original price: ", price)
#     print("Price after GST: ", price + (price * 0.18))

# gst(1000)
# gst(2000)
# gst(3000)
# gst(4000)


# def table(n):
#     print("Table of ", n)
#     print("-------------------")
#     for i in range(1, 11):
#         print(n, "X", i, "=", n * i)

# for i in range(1, 11):
#     table(i)
#     print()


# def leapyear(year):
#     if year%400==0 or (year%4==0 and year%100!=0):
#         return "Leap Year"

#     else:
#         return "Not a Leap Year"

# print(leapyear(2020))
# print(leapyear(200))
# print(leapyear(2000))
# print(leapyear(2001))

# def isprime(num):
#     for i in range(2, num//2 + 1):
#         if num % i == 0:
#             return "Not a Prime Number"
#     return "Prime Number"

# print(isprime(11))
# print(isprime(181))
# print(isprime(1891981))


# def display(name, age):
#     print("Name: ", name)
#     print("Age: ", age)

# display("John", 25)
# display(30, "Alice")  # This will cause an error because the order of arguments is incorrect

# # this is called positional arguments, where the order of arguments matters. 


# def display(name, age):
#     print("Name: ", name)
#     print("Age: ", age)

# display(name="John", age=25)
# display(age=30, name="Alice")

# This is called keyword arguments, where the order of arguments does not matter because we are explicitly specifying the names of the parameters.


# def display(name, age=None):
#     print("Name: ", name)
#     print("Age: ", age)

# display("John")
# display("Alice", 30)

# This is called default arguments, where we can provide a default value for a parameter. 
# If the argument is not provided during the function call, the default value will be used.
# In this case, if age is not provided, it will default to None.


# def display(*name):
#     print("Name: ", name)
    

# display("John")
# display( "Alice","vivek","vinith")

# this is called variable-length arguments, where we can pass a variable number of arguments to a function.


# def display(**name):
#     print("Name: ", name)
    

# display(n1="John")
# display(n2="Alice", n3="vivek", n4="vinith")


# this is called keyword variable-length arguments, where we can pass a variable number of keyword arguments to a function.