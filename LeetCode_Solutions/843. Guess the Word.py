# Source : https://leetcode.com/problems/guess-the-word/
# Author : foxfromworld
# Date  : 31/07/2021
# First attempt 

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

# Basically, if you are unlucky, there is a chance you will fail. The rate to guess every letter wrong is 25/26 * 25/26 * 25/26 * 25/26 * 25/26 * 25/26 ~ 80%. 
class Solution(object):
  def findSecretWord(self, wordlist, master):
    """
    :type wordlist: List[Str]
    :type master: Master
    :rtype: None
    """
    def cntMatches(word, guess):
      cnt = 0
      for w, g in zip(word, guess):
        if w == g:
          cnt += 1
      return cnt
    for _ in range(10):
      guess = wordlist[random.randint(0, len(wordlist) - 1)] # Randomly choose a word and check matches
      matches = master.guess(guess)
      if matches == 6:
        break
      newWordlist = []
      for word in wordlist: # Pick words with the same amount of matches and form a new word list
        if cntMatches(word, guess) == matches:
          newWordlist.append(word)
      wordlist = newWordlist
