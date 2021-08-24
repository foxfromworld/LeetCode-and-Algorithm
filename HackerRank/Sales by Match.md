```python
# Source : https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Author : foxfromworld
# Date  : 24/08/2021
# First attempt

from collections import Counter
def sockMerchant(n, ar):
    # Write your code here
    return sum([value // 2 for value in Counter(ar).values()])
```
