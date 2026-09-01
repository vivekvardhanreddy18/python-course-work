# s='python programming'
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
s='hhhhhhhhhhhhhkkkkkkkkkkhhhhhhhhhhhfffffffffuiiggggvv'
compressed = ''
count = 1
for i in range(1, len(s)):
	if s[i] == s[i - 1]:
		count += 1
	else:
		compressed += s[i - 1] + str(count)
		count = 1

compressed += s[-1] + str(count)
print(compressed)
    
