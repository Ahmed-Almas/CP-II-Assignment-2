import re
text = 'Hello Everyone Gathered Here'
res = re.search('Here',text)
print("Result = {}".format(res))