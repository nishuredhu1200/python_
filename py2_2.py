#create a list 100 to 1 using loops
num=[ ]
for i in range(100,0,-1):
    num.append(i)
print(num) 

import py2_3
k = py2_3.add_code(23,45,56)
print(k)

from  py2_3 import add_code

k =add_code (34,45,78)
print(k)
from py2_3 import add_code as i 

k= i(34,56,90)
print(k)
