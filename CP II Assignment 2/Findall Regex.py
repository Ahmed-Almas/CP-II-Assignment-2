import re
text = 'Hello Everyone Gathered Here'
res = re.findall('Here',text)
print("Result = {}".format(res))