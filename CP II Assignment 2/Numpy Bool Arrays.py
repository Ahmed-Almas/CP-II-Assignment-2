import numpy as np

a = np.reshape(np.arange(16), (4,4)) 
print(a)
large_values = (a > 10)
print('Large Values') 
print(large_values)
even_values = (a%2 == 0) 
print('Small Values') 
print(even_values)
b = ~(a%3 == 0)
#Operators 
print('array a:\n{}\n'.format(a))
print('array b:\n{}'.format(b))
c = (a%2 == 0) | (a%3 == 0) 
print('array c:\n{}'.format(c))
d = (a%2 == 0) & (a%3 == 0) 
print('array d:\n{}'.format(d))

