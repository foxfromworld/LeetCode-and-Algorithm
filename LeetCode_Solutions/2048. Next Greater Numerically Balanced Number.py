# Source : https://leetcode.com/problems/next-greater-numerically-balanced-number/
# Author : foxfromworld
# Date  : 14/02/2022
# First attempt

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # 0 <= n <= 10^6 (1000000)
        numBalanced = set([1, 22, 333, 4444, 55555, 666666, 1224444])
        # n is less than 1000000 but any number that's larger than 666666 will have a result as "1224444"
        for num in permutations(['1', '2', '2']):
            numBalanced.add(int(''.join(num)))
        for num in permutations(['1', '2', '2', '3', '3', '3']):
            numBalanced.add(int(''.join(num)))             
        for num in permutations(['1', '3', '3', '3']):
            numBalanced.add(int(''.join(num)))             
        for num in permutations(['1', '4', '4', '4', '4']):
            numBalanced.add(int(''.join(num)))             
        for num in permutations(['1', '5', '5', '5', '5', '5']):
            numBalanced.add(int(''.join(num)))                                                
        for num in permutations(['2', '2', '3', '3', '3']):
            numBalanced.add(int(''.join(num)))  
        for num in permutations(['2', '2', '4', '4', '4', '4']):
            numBalanced.add(int(''.join(num)))
        numBalanced = sorted(numBalanced)
        return numBalanced[bisect_right(numBalanced, n)]
