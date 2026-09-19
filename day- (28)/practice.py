# for i in range(1,6):
#     print(i)
# s =0
# for i in range(6):
#     s+=i
# print(s)
# s = 0
# for i in range(0,11,2):
#     s+=i
# print(s)
# n = [8, 3, 12, 5, 1, 9]
# s=n[0]
# for i in range(len(n)):
#     if s > n[i]:
#         s=n[i]
# print(s)
n = [10,5,15]
largest=0
second=0
for i in range(len(n)):

    if largest < n[i]:
        largest = n[i]
    elif second > n[i] > largest:
        second = n[i]
print(second)


    
    


