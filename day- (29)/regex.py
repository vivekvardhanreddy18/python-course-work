import re

#  pattern = r'[0-9]'
# text = 'codegnan2026'

# res = re.match(pattern, text)
# res = re.search(pattern, text)
# res = re.findall(pattern, text)
# # print(res)
# # print(res.group() if res else "Pattern not matched")
# res = re.finditer(pattern, text)
# for i in res:
#     print(i.group(),i.start())


# pattern = r'[0-9]{10}'
# text = '9876543210'

# res = re.fullmatch(pattern,text)

# print(res.group() if res else "Pattern not matched")


# pattern = r'[!@#$]'
# text = 'java!c@python#c++$flask'

# res = re.split(pattern,text)

# print(res)


# pattern =  r'[aeiou9]'
# text = 'python 30 mysql 23 flask 20 django 80'
# res = re.sub(pattern, '*',text)
# print(res)


# pattern = r'h.t'
# pattern = r'^[a-z]$'
# pattern = r'[a-z]$'

# text = 'hand loom hot hit hat hood wood'

# res = re.findall(pattern,text)
# print(res)


# pattern = r'ab+'
# pattern = r'ab*'
# text = "a ab aaab abb aaaaaabbbbbbb"
# res = re.findall(pattern , text)
# print(res)


pattern = r'^(91|0)'
# pattern = r'ab*'
text = "910987654321"
res = re.findall(pattern , text)
print(res)
