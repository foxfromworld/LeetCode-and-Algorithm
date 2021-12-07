# Source : https://leetcode.com/problems/reformat-date/
# Author : foxfromworld
# Date  : 07/12/2021
# First attempt

class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split()
        Month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
        return date[2] + '-' + Month[date[1]] + '-' + date[0][:-2] if len(date[0][:-2]) > 1 else date[2] + '-' + Month[date[1]] + '-0' + date[0][:-2]
