```python
# Source : https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# Author : foxfromworld
# Date  : 04/09/2021
# First attempt

def minimumBribes(q):
    # Write your code here
    bribes = 0
    for i, p in enumerate(q):
        if p - i - 1 > 2:
            print('Too chaotic')
            return
        for j in range(max(p - 2, 0), i):
            if q[j] > p:
                bribes += 1
    print(bribes)
```
