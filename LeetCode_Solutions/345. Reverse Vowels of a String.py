# Source : https://leetcode.com/problems/reverse-vowels-of-a-string/
# Author : foxfromworld
# Date  : 24/02/2021
# Second attempt # still slow

class Solution:
  def reverseVowels(self, s: str) -> str:
    s = list(s)
    vowelinS = []
    index = []
    for i in range(len(s)):
      if s[i] in 'aeiouAEIOU':
        vowelinS.append(s[i])
        index.append(i)
    for i in range(len(vowelinS)):
      s[index[i]] = vowelinS[::-1][i]
    return ''.join(s)

# Date  : 24/02/2021
# First attempt # really slow

class Solution:
  def reverseVowels(self, s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s = list(s)
    vowelinS = []
    index = []
    for i in range(len(s)):
      if s[i] in vowels:
        vowelinS.append(s[i])
        s[i] = '_'
        index.append(i)
    print(index)

    for i in range(len(vowelinS)):
      s[index[i]] = vowelinS[::-1][i]
    return ''.join(s)
