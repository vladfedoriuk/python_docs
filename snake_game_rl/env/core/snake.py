import numpy as np

from snake_game_rl.settings.constants import DIRECTIONS, SNAKE_BLOCK
from operator import mul


class Snake:
    def __init__(self, head_position, direction_index, length):
        """
        :param head_position: tuple
        :param direction_index: int
        :param length: int
        """
        self.snake_block = SNAKE_BLOCK
        self.current_direction_index = direction_index
        self.alive = True
        self.blocks = [head_position]
        current_position = np.array(head_position)
        for i in range(1, length):
            current_position = current_position - DIRECTIONS[self.current_direction_index]
            self.blocks.append(tuple(current_position))

    def step(self, action):
        # Execute one-time step within the environment
        curr_dir = DIRECTIONS[self.current_direction_index]
        action_dir = np.array(DIRECTIONS[action])
        if not any(map(mul, action_dir, curr_dir)):
            self.current_direction_index = action
        tail = self.blocks.pop(len(self.blocks) - 1)
        new_head = tuple(np.array(self.blocks[0]) - DIRECTIONS[action])
        self.blocks = [new_head] + self.blocks
        return new_head, tail
