```python
# Source : https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/000000000085a152
# Author : foxfromworld
# Date  : 22/08/2021
# First attempt

from itertools import permutations
t = int(input()) # Get the first input which gives the number of test cases
for z in range(t): 
    s = input() # Get the following z test samples
    perms = list(set(permutations(s))) # Find all possible permutations
    for perm in perms:
      isAna = 1
      for i in range(len(perm)):
        if s[i] == perm[i]:
          isAna = 0
          break
      if isAna == 1:
        print("Case #{}: {}".format(z+1, ''.join(perm)))
        break
    if isAna == 0:
      print("Case #{}: {}".format(z+1, 'IMPOSSIBLE'))
```
