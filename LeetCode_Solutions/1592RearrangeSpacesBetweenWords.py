
# Source : https://leetcode.com/problems/rearrange-spaces-between-words/
# Author : foxfromworld
# Date  : 16/12/2020
# First attempt 

class Solution:
  def reorderSpaces(self, text: str) -> str:
    if len(text) == 1:
      return text
    space = 0
    string = ""
    collection = []
    for ch in text:
      if ch == " ":
        space+=1
        if string!="":
          collection.append(string)
          string = ""
      else:
        string+=ch
    if string!="":
      collection.append(string)
    if len(collection)-1 <=0:
      return "".join(collection)+(" "*space)
    a,b = divmod(space,len(collection)-1)
    return (" "*a).join(collection) + (" "*b)
