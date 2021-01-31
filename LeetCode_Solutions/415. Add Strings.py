# Source : https://leetcode.com/problems/add-strings/
# Author : foxfromworld
# Date  : 31/01/2021
# Third attempt 

class Solution:
  def addStrings(self, num1: str, num2: str) -> str:
    carry = 0
    result = [] 
    pt1 = len(num1) - 1
    pt2 = len(num2) - 1
    while pt1>=0 or pt2>=0:
      digit1 = ord(num1[pt1])-ord('0') if pt1>=0 else 0
      digit2 = ord(num2[pt2])-ord('0') if pt2>=0 else 0
      sum = (digit1 + digit2 + carry)%10
      carry = (digit1 + digit2 + carry)//10
      result.append(sum)
      pt1 -= 1
      pt2 -= 1
    if carry:
      result.append(carry)
    return ''.join(str(digit) for digit in result[::-1])

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
