# Source : https://leetcode.com/problems/find-center-of-star-graph/
# Author : foxfromworld
# Date  : 16/12/2021
# Third attempt

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()

# Date  : 16/12/2021
# Second attempt

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][1] if edges[0][1] in edges[1] else edges[0][0]

# Date  : 16/12/2021
# First attempt

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = set()
        for eg1, eg2 in edges:
            if eg1 in seen:
                return eg1
            if eg2 in seen:
                return eg2
            seen.add(eg1)
            seen.add(eg2)      
