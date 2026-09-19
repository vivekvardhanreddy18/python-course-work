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
s=0
n = [4, 9, 2, 15, 7, 3]
for i in range(len(n)):
    if n[i] < n[i+1]:
        s=n[i+1]
print(s)