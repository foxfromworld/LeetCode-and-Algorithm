```python
# Source : https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Author : foxfromworld
# Date  : 01/09/2021
# Second attempt

def repeatedString(s, n):
    # Write your code here
    length = len(s)
    time = n // length
    return s.count('a') * time + s[:n - (time * length)].count('a')

# Date  : 01/09/2021
# First attempt

def repeatedString(s, n):
    # Write your code here
    num = s.count('a')
    length = len(s)
    time = n // length
    last = n - (time * length) 
    return num * time + s[:last].count('a')
```
