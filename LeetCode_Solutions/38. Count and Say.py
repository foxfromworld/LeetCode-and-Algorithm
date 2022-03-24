# Source : https://leetcode.com/problems/count-and-say/
# Author : foxfromworld
# Date   : 24/03/2022
# First attempt

class Solution:
    def countAndSay(self, n: int) -> str:
        ret = ['1']
        for i in range(1, n):
            temp = ret[i-1]
            curr = temp[0]
            cnt = 0
            s = ''
            for ch in temp:             
                if ch == curr:
                    cnt += 1
                else:      
                    s += str(cnt) + curr
                    curr = ch
                    cnt = 1
            else:
                s += str(cnt) + curr
            ret.append(s)
        return ret[-1]
