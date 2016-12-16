import re
re.sub('[ \r\n]','',x)
niii = '第一章：冰公主..(12p)'
zhe = re.compile(r'\d+')
mo = zhe.search(ni)
mo.group()
print(mo.group())
re.compile(r'\d+').search(ni).group()


link.name,link['href'],link.get_text()