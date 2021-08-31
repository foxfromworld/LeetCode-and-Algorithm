```python
# Source : https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Author : foxfromworld
# Date  : 31/08/2021
# First attempt

def jumpingOnClouds(c):
    # Write your code here
    index, step = 0, 0
    while index + 1 < len(c):
        if index + 2 < len(c) and c[index + 2] == 0:
            index += 2
        else:
            index += 1
        step += 1
    return step
```
