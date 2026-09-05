import re
pattern = r'[0-9]'
text = 'codegnan'

res = re.match(pattern,text)
print(res.group() if res else "pattern not found")



import re
pattern = r'[0-9]'
text = 'codegnan'

res = re.search(pattern,text)
print(res.group() if res else "pattern not found")




import re
pattern = r'[0-9]'
text = 'codegnan 2026 python version 3.14'

res = re.findall(pattern,text)
print(res.group() if res else "pattern not found")



import re
pattern = r'[0-9]'
text = 'codegnan 2026 python version 3.14'
for i in res:
    print(i.group(),i.start())


import re
pattern = r'[0-9]'
text = '9491537889'
res = re.fullmatch(pattern,text)



import re
pattern = 'r[,(#)]'
res = re.split(pattern,text)
print(res)



import re
pattern = r'[a-Z]'
text = 'pyhton version 3.14 , batch-63'
res = re.fullmatch(pattern, '*',text)
print(res)



import re
pattern = r'e.t'
text = 'e@t eaat eat eet ett ect egfgqfo ruifhosjkll'
res = re.findall(pattern,text)
print(res)




import re
pattern = r'^(91)'
text = '9704224688'
res = re.findall(pattern.text)
print(res)


import re
pattern = r'$0'
text = '9704224688'
res = re.findall(pattern,text)
print(res)



import re
pattern = r'to+'
text = 'to tdfghjk too toooo toooooooo'
res = re.findall(pattern,text)
print(res)



import re
pattern = r'ab*'
text = 'ad abbb a abbbbbbb abbb'
res = re.findall(pattern,text)
print(res)


import re
pattern = r'91.0'
text = '09876'

res = re.search(pattern,text)
print(res.group() if res else "pattern not found")