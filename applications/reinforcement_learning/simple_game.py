# -*- coding: utf-8 -*-
import numpy as np


class SimpleGame:
    def __init__(self, grid, goal_loc=None, doom_loc=None):
        self.grid = grid
        self.board = np.zeros([self.grid, self.grid])
        if goal_loc is None:
            self.goal_loc = [np.random.randint(0, self.grid), np.random.randint(0, self.grid)]
        else:
            self.goal_loc = goal_loc
        if doom_loc is None:
            self.doom_loc = [np.random.randint(0, self.grid), np.random.randint(0, self.grid)]
        else:
            self.doom_loc = doom_loc
        # corner case
        while self.doom_loc == self.goal_loc:
            self.doom_loc = [np.random.randint(0, self.grid), np.random.randint(0, self.grid)]
        self.agent_point = None

    def _display_board(self, agent_loc):
        for row_idx in range(self.grid):
            for col_idx in range(self.grid):
                print(self.board[row_idx][col_idx])

    def _result_checker(self, agent_loc):
        if agent_loc == self.goal_loc:
            return 1
        elif agent_loc == self.doom_loc:
            return -1
        else:
            return 0

    def game_initialization(self, start_point=None):
        if start_point is None:
            self.agent_point = [0, 0]
        self.agent_point = start_point

    def _move(self, action, agent_loc):
        action = action.lower()
        if action == "up":
            if agent_loc[0] == 0:
                raise NotImplementedError("Agent cannot move up!")
            return [agent_loc[0]-1, agent_loc[1]]
        elif action == "down":
            if agent_loc[0] == self.grid-1:
                raise NotImplementedError("Agent cannot move up!")
            return [agent_loc[0]+1, agent_loc[1]]
        elif action == "left":
            if agent_loc[1] == 0:
                raise NotImplementedError("Agent cannot move up!")
            return [agent_loc[0], agent_loc[1]-1]
        elif action == "right":
            if agent_loc[1] == self.grid-1:
                raise NotImplementedError("Agent cannot move up!")
            return [agent_loc[0], agent_loc[1]+1]
        else:
            raise NotImplementedError()

    def game_player(self, move):
        if self.agent_point is None:
            self.game_initialization()
        try:
            new_loc = self._move(move)
        except NotImplementedError as e:
            raise NotImplementedError(e)
        self.agent_point = new_loc
        result = self._result_checker(self.agent_point)
        if result == 1:
            print("Win!")
        elif result == -1:
            print("Lose!")


if __name__ == "__main__":
    pass
