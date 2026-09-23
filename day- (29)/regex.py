import re

pattern = r'[0-9]'
text = 'codegnan2026'

res = re.match(pattern, text)
res = re.search(pattern, text)
res = re.findall(pattern, text)
# print(res)
# print(res.group() if res else "Pattern not matched")
res = re.finditer(pattern, text)
for i in res:
    print(i.group(),i.start())
