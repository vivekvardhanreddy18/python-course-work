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
# n = [10,5,15]
# largest=0
# second=0
# for i in range(len(n)):

#     if largest < n[i]:
#         second = largest
#         largest = n[i]
#     elif largest > second < n[i]:
#         second = n[i]
# print(second)

a=1234
def rev(n):
    b= (n%10) *10 + n//10
    return b
    

print(rev(a))






    
    


