# Source : https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
# Author : foxfromworld
# Date   : 06/03/2022
# Second attempt

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        if n % k != 0:
            s += fill * (k - n % k)
        ret = []
        i = 0
        for _ in range(len(s) // k):
            ret.append(s[i:i+k])
            i += k
        return ret

# Date   : 06/03/2022
# First attempt

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        if n % k != 0:
            s += fill * (k - n % k)
        ret = []
        for i in range(0, n, k):
            ret.append(s[i:i+k])
        return ret
