# Source : https://leetcode.com/problems/design-snake-game/
# Author : foxfromworld
# Date  : 16/02/2022
# First attempt

class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = [[0, 0]]
        self.width = width
        self.height = height
        self.food = food
        self.direction = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}
    def move(self, direction: str) -> int:
        newHead = [self.snake[0][0] + self.direction[direction][0], self.snake[0][1] + self.direction[direction][1]]
        if newHead[0] >= self.height or newHead[1] >= self.width or newHead[0] < 0 or newHead[1] < 0: # when the snake goes out of the bound
            return -1
        if newHead in self.snake and newHead != self.snake[-1]:
            return -1 # when the snake runs into itself. the last one is still in the queue before processing so we don't have to count the current tail in 
        if self.food and self.food[0] == newHead: # eat food         
            self.snake.insert(0, newHead)
            del self.food[0]
        else:
            self.snake.insert(0, newHead)
            self.snake.pop()
        return len(self.snake) - 1
                
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
