n=int(input("Enter a number: "))
res =[]
for i in range(1, n+1):
    if n % i == 0:
        res.append(i)
print("The factors of", n, "are:", res)

