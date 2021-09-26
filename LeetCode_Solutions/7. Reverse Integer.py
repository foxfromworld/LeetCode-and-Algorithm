```python
# Source : https://leetcode.com/problems/reverse-integer/
# Author : foxfromworld
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
