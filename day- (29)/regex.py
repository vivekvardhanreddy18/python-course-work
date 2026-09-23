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


# pattern = r'^(91|0)'
# text = "91987654321"
# res = re.findall(pattern , text)
# print(res)



# pattern = r'[A-Za-z0-9]'
# text = r'ehuhujhujJ9098HHYKOREHrj'
# res = re.findall(pattern , text)
# print(res)



# pattern = r'(ae)'
# text = 'lekhsbrglsfnv a,nk flkaejbaesdkljbl'
# res = re.findall(pattern,text)
# print(res)


# pattern = r'[0-9]{2}'
# pattern  = r'\w'
# pattern  = r'\W'
# pattern  = r'\d'
# pattern  = r'\D'
# pattern  = r'\s'
# pattern  = r'\S'
# text = 'lskdjfgbi3y4t07230lsi734kjhit'
# res = re.findall(pattern,text)
# print(res)

# name = input("Enter the name: ")
# pattern = r'^[a-zA-Z]{2,25}( [a-zA-Z]{2,25}$)'
# res = re.fullmatch(pattern, name)
# print("Valid" if res else "Invalid")


# email = input("Enter the email: ")
# pattern = r'^[a-zA-Z._0-9]+@[a-zA-Z._0-9]+\.[A-Za-z]{2,}$'
# res = re.fullmatch(pattern, email)
# print("Valid" if res else "Invalid")



phone = input("Enter the phone: ")
pattern = r'^[6-9]\d'
res = re.fullmatch(pattern, phone)
print("Valid" if res else "Invalid")




