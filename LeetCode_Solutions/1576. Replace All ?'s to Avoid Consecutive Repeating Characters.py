# Source : https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
# Author : foxfromworld
# Date  : 16/02/2021
# First attempt 

class Solution:
  def modifyString(self, s: str) -> str:
    if len(s)==1 and s=="?":  return 'a'
    if len(s)==1: return s

    s = list(s)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(s)):
      if s[i] == '?':
        if i == 0:
          for ch in alphabet:
            if ch != s[i+1]: 
              s[i] = ch 
              break
        elif i == len(s)-1:
          for ch in alphabet:
            if ch != s[i-1]: 
              s[i] = ch 
              break
        else:
          for ch in alphabet:
            if ch != s[i+1] and ch != s[i-1]: 
              s[i] = ch 
              break          
    return "".join(s)
