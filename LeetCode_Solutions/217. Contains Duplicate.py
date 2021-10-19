# Source : https://leetcode.com/problems/contains-duplicate/
# Author : foxfromworld
# Date  : 19/10/2021
# Fourth attempt

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Date  : 19/10/2021
# Third attempt

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
      
# Date  : 19/10/2021
# Second attempt

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for ct in counter:
            if counter[ct] > 1:
                return True
        return False

# Date  : 19/10/2021
# First attempt

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)
