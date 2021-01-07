# Source : https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
# Author : foxfromworld
# Date  : 07/01/2021
# Second attempt (Really slow...)

class Solution:
  def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
    # 1 <= queries[i].length, words[i].length <= 10
    frequency = [0]*12 # 0 1 2 3 4 5 6 7 8 9 11 1-10 to memorize, 11 is the buffer for the index, "query.count(min(query)) + 1"
    for word in words:
      frequency[word.count(min(word))]+=1 # use this list to memorise the frequency of the smallest character of words
    for i in range(len(frequency)-2, -1, -1):
      frequency[i] += frequency[i+1] # To make a cumulative frequency table
    ans = [0]*len(queries)
    print(len(frequency))
    for idx,query in enumerate(queries):
      ans[idx] = frequency[query.count(min(query)) + 1] 
    return ans   

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
