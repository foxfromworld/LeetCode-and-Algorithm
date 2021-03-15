# Source : https://leetcode.com/problems/reverse-words-in-a-string/
# Author : foxfromworld
# Date  : 15/03/2021
# Third attempt 

class Solution:
  def reverseWords(self, s: str) -> str:
    head, tail = 0, len(s)-1
    while s[head] == ' ':
      head += 1
    while s[tail] == ' ':
      tail -= 1
    word, returnL = [], []
    while head <= tail:
      if s[head] != ' ':
        word.append(s[head])
      elif s[head] == ' ' and word:
        returnL.insert(0, ''.join(word))
        word = []
      head += 1
    returnL.insert(0, ''.join(word))
    return ' '.join(returnL)

# Date  : 15/03/2021
# Second attempt 

class Solution:
  def reverseWords(self, s: str) -> str:
    def reverseString(st, ed, string):
      while st < ed:
        string[st], string[ed] = string[ed], string[st]
        st += 1
        ed -= 1
    # Trim the spaces at the beginning and the end
    head, tail = 0, len(s)-1
    while s[head] == ' ':
      head += 1
    while s[tail] == ' ':
      tail -= 1
    # Trim the spaces between words
    newList = []
    while head <= tail:
      if s[head] != ' ':
        newList.append(s[head])
      elif newList[-1] != ' ':
        newList.append(' ')
      head += 1
    reverseString(0, len(newList)-1, newList)

    head, tail = 0, 0
    for i in range(len(newList)):
      if newList[i] == ' ':
        tail = i - 1
        reverseString(head, tail, newList)
        head = i + 1
    tail = len(newList)-1
    reverseString(head, tail, newList)
    return ''.join(newList)

# Date  : 12/03/2021
# First attempt 

class Solution:
  def reverseWords(self, s: str) -> str:
    return ' '.join(s.split()[::-1])
