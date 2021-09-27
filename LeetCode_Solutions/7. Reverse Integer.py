```python
# Source : https://leetcode.com/problems/reverse-integer/
# Author : foxfromworld
# Date  : 26/09/2021
# Fourth attempt

class Solution:
  def reverse(self, x: int) -> int:
    if x < 0: 
        isNegative = True
    else:
        isNegative = False
    x = str(abs(x))
    ret = int(x[::-1])
    if isNegative: 
        ret = 0 - ret
    return ret if ret <= 2147483647 and ret > -2147483648 else 0  

# Date  : 26/09/2021
# Third attempt

class Solution:
  def reverse(self, x: int) -> int:
    x = str(x)
    #ret = int('-' + x[1:][::-1]) if x[0] == '-' else int(x[::-1])
    ret = int('-' + x[:0:-1]) if x[0] == '-' else int(x[::-1])
    return ret if ret <= 2147483647 and ret > -2147483648 else 0      

# Date  : 26/09/2021
# Second attempt

class Solution:
  def reverse(self, x: int) -> int:
    ret = 0
    x = str(x)
    if x == 0: return 0
    ret = x[::-1]
    if ret[-1] == '-':
        ret = '-' + ret[:-1]
    return 0 if int(ret) > 2147483647 or int(ret) < -2147483647 else int(ret)
  
# Date  : 26/09/2021
# First attempt

class Solution:
  def reverse(self, x: int) -> int:
    ret = 0
    x = str(x)
    if x == 0: return 0
    if x[0] == '-':
      ret = x[0] + (x[1:]) [::-1]
    else:
      ret = x[::-1]
    return 0 if int(ret) > 2147483647 or int(ret) < -2147483647 else int(ret)
```
