```python
# Source : https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Author : foxfromworld
# Date  : 31/08/2021
# First attempt

def countingValleys(steps, path):
    # Write your code here
    level, result, index = 0, 0, 0
    for step in path:
        if step == 'D':
            level -= 1
        if step == 'U':
            level += 1
        if level == 0 and step =='U':
            result += 1
    return result
```
