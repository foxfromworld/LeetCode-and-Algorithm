```python
# Source : https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# Author : foxfromworld
# Date  : 02/09/2021
# First attempt

def hourglassSum(arr):
    # Write your code here
    ans = float('inf')
    for row in range(4):
      for col in range(4):
        ans = max(ans, sum(arr[row][col:col+3]) + arr[row+1][col+1] + sum(arr[row+2][col:col+3]))
    return ans
```
