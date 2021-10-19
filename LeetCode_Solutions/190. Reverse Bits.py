# Source : https://leetcode.com/problems/reverse-bits/
# Author : foxfromworld
# Date  : 18/10/2021
# Second attempt

class Solution:
    def reverseBits(self, n: int) -> int:
        ret = ''
        while n:
            ret += str(n & 1)
            n >>= 1
        ret += (32-len(ret)) * '0'
        return int(ret, 2)

# Date  : 18/10/2021
# First attempt

class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        binary = '0' * (32-len(binary)) + binary
        return int(binary[::-1], 2)
