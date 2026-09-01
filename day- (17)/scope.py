# def display():
#     print("Inside Function : ",n)

# n = 10
# display()
# print("Outside Function : ",n)

# this is called global variable, where the variable is defined outside the function and can be accessed inside the function.

# def display():
#     global n
#     n = 10
#     print("Inside Function : ",n)

# display()
# print("Outside Function : ",n)

# this is called global variable, where the variable is defined inside the function and can be accessed outside the function by using the global keyword.

#when we define a variable inside the function, it is called local variable and can be accessed only inside the function.
#when global variable and local variable have the same name, then the local variable will be given preference over the global variable.
# when we use the global keyword inside the function, then we cannot give that variable as a parameter to the function, otherwise it will give an error.


# def display():
#     course = "Python"
#     def update():
#         nonlocal course
#         course = "Java"
#         print("Inside Function : ",course)
#     update()
#     print("Outside Function : ",course)

# display()

# This is called nonlocal variable, where the variable is defined inside the function and can be accessed outside the function by using the nonlocal keyword.


# l=[1,2,3,4,5]
# print(max(l))

# print = 20
# print(max)

# Here, we are trying to assign a value to the built-in function print, which will cause an error when we try to use the print function later in the code.
#  It is not recommended to use built-in function names as variable names.


