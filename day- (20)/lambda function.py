# var =  lambda a: a+10
# print(var(5))

# gst = lambda price:price + price*0.18
# print(gst(1000))
# print(gst(5000))

# wish = lambda name: f"Hello {name}, Good Morning"
# print(wish("John")) 
# print(wish("Vinith"))
# print(wish("Vivek"))

# largest = lambda a,b,c: a if (a>b and a>c) else (b if b>c else c)
# print(largest(10,20,30))

# isvowel = lambda a : True if a in "aeiouAEIOU" else False
# print(isvowel("a")) 



# l = [1,2,3,4,5,6,7,8,9]
# update = lambda l: [i+10 for i in l]
# print(update(l))
# print(l)
# print(list(map(lambda i:i+10, l)))


# t = (31,45,456,346)
# discount = lambda t: tuple(i - i*0.1 for i in t)
# print(discount(t))
# discount = list(map(lambda i:i - i*0.1, t))
# print(discount)



# l = [1,2,3,4,5,6,7,8,9]
# u = list(filter(lambda i:i%2==0, l))
# print(u)

# p = list(filter(lambda i:i>5, l))
# print(p)


# l = ["sowmya@codegnan.com","sowmya@gmail.com","sowmya@yahoo.com","sowmya@outlook.com"]
# domain =list(map( lambda i: i.split("@")[1],l))
# name =list(map( lambda i: i.split("@")[0],l))
# print(domain)
# print(name)


# from functools import reduce

# l = [1,2,3,4,5,6,7,8,9]
# res = reduce(lambda a,b:a+b, l)
# print(res)


# prod = reduce(lambda a,b:a*b, l)
# print(prod)


# a = {'s1': True, 's2': False, 's3': True, 's4': False, 's5': True, 's6': False, 's7': True, 's8': False}
# seat = list(filter(lambda i:a[i]==True, a))
# print(seat)


# b= {'egg': 20, 'milk': 30, 'bread': 40, 'butter': 50, 'cheese': 60, 'yogurt': 70, 'cream': 80}
# # prod = list(filter(lambda i:b[i]>50, b))
# # print(prod)

# hightolow = list(sorted(b.items(), key=lambda i:i[1], reverse=True))
# print(hightolow)

# lowtohigh = list(sorted(b.items(), key=lambda i:i[1]))
# print(lowtohigh)


# add line sync test