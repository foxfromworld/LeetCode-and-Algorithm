# Source : https://leetcode.com/problems/generate-parentheses/
# Author : foxfromworld
# Date  : 05/02/2022
# First attempt
                            # []
                             # |
                            # [(]
                        # /         \
                     # [((]         [()]
                    # /    \            \
                # [(((]    [(()]         [()(]
              # /         /     \        /     \
            # [((()]   [(()(]   [(())] [()((]  [()()]
           # /         /         /      |        |
     # [((())]   [(()()]     [(())(]  [()(()]  [()()(]
       # /         /          /         |        |
# [((()))]    [(()())]    [(())()]   [()(())]  [()()()]        


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def backtrack(comb = [], left = 0, right = 0):
            if len(comb) == 2 * n: 
                ret.append("".join(comb))
                return
            if left < n:
                comb.append("(")
                backtrack(comb, left + 1, right)
                comb.pop()                
            if left > right:
                comb.append(")")
                backtrack(comb, left, right + 1)
                comb.pop()                
        backtrack()
        return ret
