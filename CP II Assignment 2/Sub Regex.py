import re
text = 'Hello Everyone Gathered Here'
res = re.sub('Here','',text)
print("Result = {}".format(res))