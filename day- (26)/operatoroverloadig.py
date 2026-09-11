class num:
    def __init__(x,n):
        x.n = n

    def __add__(x,o):
        return x.n + x.o
    def __sub__(x,o):
        return x.n -x.o
    def __mul__(x,o):
        return x.n * x.o
    def __truediv__(x,o):
        return x.n / x.o
    def __floordiv__(x,o):
        return x.n // x.o
    def __pow__(x,o):
        return x.n ** x.o

a = num(5)
b=num(10)

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)