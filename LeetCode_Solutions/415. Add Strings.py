# Source : https://leetcode.com/problems/add-strings/
# Author : foxfromworld
# Date  : 30/01/2021
# Second attempt (not very fast)

class Solution:
  def addStrings(self, num1: str, num2: str) -> str:
    chars = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
    string = ''
    result = eval(num1+"+"+num2)
    if result == 0:
      return "0"
    while result > 0:
      string = chars[result%10] + string
      result //= 10
    return string     

# Date  : 29/01/2021
# First attempt (slow)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
      digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
      chars = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
      result1 = result2 = 0
      for d in num1:
        result1 = result1*10 + digits[d]
      for d in num2:
        result2 = result2*10 + digits[d]        
      result = result1 + result2
      string = ''
      if result == 0:
        return "0"
      while result > 0:
        string = chars[result%10] + string
        result //= 10
      return string
