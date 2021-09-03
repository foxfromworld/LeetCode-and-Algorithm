```python
# Source : https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# Author : foxfromworld
# Date  : 03/09/2021
# First attempt

def rotLeft(a, d):
    # Write your code here
    l = len(a)
    return a[d % l:] + a[0:d % l]
```
