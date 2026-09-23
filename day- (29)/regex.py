import re

pattern = r'[0-9]'
text = 'codegnan2026'

res = re.match(pattern, text)

print(res.group() if res else "Pattern not matched")