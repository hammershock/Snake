# snake.py
import numpy as np
from collections import deque

import random


class SnakeGame:
    empty_block = 0
    snake_block = 1
    food_block = 2
    
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.board = np.zeros((height, width), dtype=int)
        self.board[3, 3] = self.food_block
        self.body = deque()
        self.body.append((height // 2, width // 2))
        self.board[height // 2, width // 2] = self.snake_block
        self.score = 0
        self.dx = 0
        self.dy = -1
    
    def move_snake(self):
        head_x, head_y = self.body[0]
        new_x = head_x + self.dx
        new_y = head_y + self.dy
        if (new_x < 0 or new_x >= self.width or
                new_y < 0 or new_y >= self.height or
                self.board[new_y, new_x] == self.snake_block):
            return False  # Game over
        if self.board[new_y, new_x] == self.food_block:
            self.score += 1
            self._place_food()
        else:
            tail_x, tail_y = self.body.pop()
            self.board[tail_y, tail_x] = self.empty_block
        self.body.appendleft((new_x, new_y))
        self.board[new_y, new_x] = self.snake_block
        return True
    
    def _place_food(self):
        empty = np.argwhere(self.board == 0)
        if len(empty) > 0:
            food_y, food_x = random.choice(empty)
            self.board[food_y, food_x] = self.food_block
    
    def change_direction(self, dx, dy):
        if (dx, dy) == (-self.dx, -self.dy):
            return  # Prevent reversing
        self.dx, self.dy = dx, dy
