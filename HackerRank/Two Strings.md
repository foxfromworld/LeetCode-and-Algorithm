```python
# Source : 
# Author : foxfromworld
# Date  : 03/09/2021
# First attempt

from collections import Counter
def twoStrings(s1, s2):
    # Write your code here
    c1 = Counter(list(s1))
    c2 = Counter(list(s2))
    for key in c1:
        if key in c2:
            return 'YES'
    return 'NO'
```
