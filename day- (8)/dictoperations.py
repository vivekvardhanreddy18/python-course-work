Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Dictionary operations
d={}
d
{}
type(d)
<class 'dict'>
d= {1:4,2:5,3:6}
d
{1: 4, 2: 5, 3: 6}
d ={}
d
{}
d[1]=1
d[12.3]=1
d['str']=1
d[4+3j]=1
d[(1,2,3)]=1
d[True] = 1
d
{1: 1, 12.3: 1, 'str': 1, (4+3j): 1, (1, 2, 3): 1}
d[1] =1
d[2] = 12.3

d[3]='str'
d[4]=4+5j
d[5]=(1,2,3)
d[6]=[1,2,3]
d[7]={1,2,3}
d[8]=frozenset({1,2,3})
d
{1: 1, 12.3: 1, 'str': 1, (4+3j): 1, (1, 2, 3): 1, 2: 12.3, 3: 'str', 4: (4+5j), 5: (1, 2, 3), 6: [1, 2, 3], 7: {1, 2, 3}, 8: frozenset({1, 2, 3})}
d[[1,2,3]]=1
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    d[[1,2,3]]=1
TypeError: unhashable type: 'list'
d[{1:2, 3:s}]=1
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d[{1:2, 3:s}]=1
NameError: name 's' is not defined
d
{1: 1, 12.3: 1, 'str': 1, (4+3j): 1, (1, 2, 3): 1, 2: 12.3, 3: 'str', 4: (4+5j), 5: (1, 2, 3), 6: [1, 2, 3], 7: {1, 2, 3}, 8: frozenset({1, 2, 3})}
1 in d
True
12.3 in d
True
5 in d
True
frozenset({1,2,3}) in d
False
(1,2,3) in d
True
data.get('frozenset({1,2,3})')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    data.get('frozenset({1,2,3})')
NameError: name 'data' is not defined
d.get('frozenset({1,2,3})')
id(d)
1915732877952
d.get('9','key not present')
'key not present'
>>> d.popitem()
(8, frozenset({1, 2, 3}))
>>> d.pop('3')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    d.pop('3')
KeyError: '3'
>>> d.pop('str')
1
>>> d.clear()
>>> d
{}
>>> d ={1: 1, 12.3: 1, 'str': 1, (4+3j): 1, (1, 2, 3): 1, 2: 12.3, 3: 'str', 4: (4+5j), 5: (1, 2, 3), 6: [1, 2, 3], 7: {1, 2, 3}, 8: frozenset({1, 2, 3})}
>>> d
{1: 1, 12.3: 1, 'str': 1, (4+3j): 1, (1, 2, 3): 1, 2: 12.3, 3: 'str', 4: (4+5j), 5: (1, 2, 3), 6: [1, 2, 3], 7: {1, 2, 3}, 8: frozenset({1, 2, 3})}
>>> d.values()
dict_values([1, 1, 1, 1, 1, 12.3, 'str', (4+5j), (1, 2, 3), [1, 2, 3], {1, 2, 3}, frozenset({1, 2, 3})])
>>> d.items()
dict_items([(1, 1), (12.3, 1), ('str', 1), ((4+3j), 1), ((1, 2, 3), 1), (2, 12.3), (3, 'str'), (4, (4+5j)), (5, (1, 2, 3)), (6, [1, 2, 3]), (7, {1, 2, 3}), (8, frozenset({1, 2, 3}))])
>>> sorted(d)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    sorted(d)
TypeError: '<' not supported between instances of 'str' and 'float'
>>> max(d)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    max(d)
TypeError: '>' not supported between instances of 'str' and 'float'
>>> min(d)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    min(d)
TypeError: '<' not supported between instances of 'str' and 'int'
>>> d=b
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    d=b
NameError: name 'b' is not defined
>>> d
{1: 1, 12.3: 1, 'str': 1, (4+3j): 1, (1, 2, 3): 1, 2: 12.3, 3: 'str', 4: (4+5j), 5: (1, 2, 3), 6: [1, 2, 3], 7: {1, 2, 3}, 8: frozenset({1, 2, 3})}
>>> d = b
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    d = b
NameError: name 'b' is not defined
