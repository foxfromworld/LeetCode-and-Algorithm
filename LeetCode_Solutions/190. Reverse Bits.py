# Source : https://leetcode.com/problems/reverse-bits/
# Author : foxfromworld
# Date  : 18/10/2021
# Second attempt


# Date  : 18/10/2021
# First attempt

class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        binary = '0' * (32-len(binary)) + binary
        return int(binary[::-1], 2)
