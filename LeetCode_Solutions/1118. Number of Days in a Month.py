# Source : https://leetcode.com/problems/number-of-days-in-a-month/submissions/
# Author : foxfromworld
# Date  : 08/11/2021
# First attempt

class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        days = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if month in days:
            return days[month]
        else:
            if year % 4 != 0: # if (year is not divisible by 4) then (it is a common year)
                return 28
            elif year % 100 != 0: # else if (year is not divisible by 100) then (it is a leap year)
                return 29
            elif year % 400 != 0: # else if (year is not divisible by 400) then (it is a common year)
                return 28
            else: #else (it is a leap year)
                return 29
             
