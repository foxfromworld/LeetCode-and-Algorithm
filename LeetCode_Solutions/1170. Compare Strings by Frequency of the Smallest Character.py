# Source : https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
# Author : foxfromworld
# Date  : 06/01/2021
# First attempt (Really slow...)

class Solution:
  def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
    def f(target):
      return(target.count(min(target)))
    w_count = []
    for str in words:
      w_count.append(f(str))
    ans = [0]*len(queries)
    for idx, str in enumerate(queries):
      for ct in w_count:
        if f(str) < ct:
          ans[idx]+=1
    return ans
