# Passby value means that a copy of the variable is passed to the function. 
# Any changes made to the parameter inside the function do not affect the original variable outside the function.
# for mutable data types like lists, dictionaries, and sets, the reference to the object is passed to the function.
# for immutable data types like integers, floats, strings, and tuples, a copy of the value is passed to the function.


# int
# def display(n):
#     n += 20
#     print("Inside Function : ",n)

# n = 10
# display(n)
# print("Outside Function : ",n)

# set
# def display(n):
#     n.append(5)
#     print("Inside Function : ",n)

# n = [1, 2, 3, 4]
# display(n)
# print("Outside Function : ",n)


