#F-STRINGS

"""me = "dell"
a = "this is %s"%me
print(a)"""

import math
me = "dell"
a1 = 3
"""a = "this is {1} {0}"
b = a.format(me, a1)
print(b)"""

a = f"this is {me} {a1} {math.cos(60)}"
print(a)
