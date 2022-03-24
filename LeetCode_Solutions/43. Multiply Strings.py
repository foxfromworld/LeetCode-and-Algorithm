# Source : https://leetcode.com/problems/multiply-strings/
# Author : foxfromworld
# Date   : 24/03/2022
# First attempt

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        str2Int = {"0": 0, "1": 1, "2": 2, "3": 3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        int2Str = {0: "0", 1: "1", 2: "2", 3: "3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
        n1, n2 = 0, 0
        for i in range(len(num1)):
            n1 += str2Int[num1[::-1][i]] * pow(10, i)
        for i in range(len(num2)):
            n2 += str2Int[num2[::-1][i]] * pow(10, i)
        product  = n1 * n2
        ret = ''
        if product == 0:
            return "0"        
        while product > 0:
            ret = int2Str[product  % 10] + ret
            product  = product // 10
        return ret
