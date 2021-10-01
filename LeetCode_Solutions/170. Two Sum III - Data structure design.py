# Source : https://leetcode.com/problems/two-sum-iii-data-structure-design/
# Author : foxfromworld
# Date  : 01/10/2021
# First attempt

class TwoSum:

    def __init__(self):
        self.visited = defaultdict(int)

    def add(self, number: int) -> None:
        self.visited[number] += 1

    def find(self, value: int) -> bool:
        for num in self.visited:
            diff = value - num
            if diff != num:
                if diff in self.visited:
                    return True
            elif self.visited[num] == 2:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
