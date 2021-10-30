# Source : https://leetcode.com/problems/fizz-buzz/
# Author : foxfromworld
# Date  : 30/10/2021
# Second attempt

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzBuzz = {3:'Fizz', 5:'Buzz'}
        ret = []
        for i in range(1, n+1):            
            temp = ''
            for key in fizzBuzz:
                if i % key == 0:
                    temp += fizzBuzz[key]
            if not temp:
                temp = str(i)
            ret.append(temp)
        return ret

# Date  : 30/10/2021
# First attempt

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzBuzz = {3:'Fizz', 5:'Buzz'}
        ret = []
        for i in range(1, n+1):            
            temp = ''
            for key in fizzBuzz:
                if i % key == 0:
                    temp += fizzBuzz[key]
            if temp:
                ret.append(temp)
            else:
                ret.append(str(i))
        return ret
