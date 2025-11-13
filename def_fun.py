
import def_function
k = def_function.add_code(23,45,56)
print(k)

from  def_function import add_code

k =add_code (34,45,78)
print(k)
from def_function import add_code as i 

k= i(34,56,90)
print(k)
