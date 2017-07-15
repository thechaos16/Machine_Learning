# -*- coding: utf-8 -*-
import numpy as np


class SimpleGame:
    def __init__(self, grid, goal_loc=None, doom_loc=None):
        self.grid = grid
        self.board = np.zeros([self.grid, self.grid]).astype(np.int)
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
        self.game_status = 0  # NOTE: 1 for win, -1 for lose, 0 for still playing

    def _display_board(self, agent_loc):
        for row_idx in range(self.grid):
            row_printer = []
            for col_idx in range(self.grid):
                if row_idx == self.goal_loc[0] and col_idx == self.goal_loc[1]:
                    row_printer.append("G")
                    continue
                if row_idx == self.doom_loc[0] and col_idx == self.doom_loc[1]:
                    row_printer.append("D")
                    continue
                if row_idx == agent_loc[0] and col_idx == agent_loc[1]:
                    row_printer.append("A")
                    continue
                row_printer.append(str(self.board[row_idx, col_idx]))
            print(" ".join(row_printer))

    def _result_checker(self, agent_loc):
        if agent_loc == self.goal_loc:
            return 1
        elif agent_loc == self.doom_loc:
            return -1
        else:
            return 0

    def _game_initialization(self, start_point=None):
        if start_point is None:
            self.agent_point = [0, 0]
        else:
            self.agent_point = start_point

    def _move(self, action, agent_loc):
        action = action.lower()
        if action == "up":
            if agent_loc[0] == 0:
                raise NotImplementedError("Agent cannot move UP!")
            return [agent_loc[0]-1, agent_loc[1]]
        elif action == "down":
            if agent_loc[0] == self.grid-1:
                raise NotImplementedError("Agent cannot move DOWN!")
            return [agent_loc[0]+1, agent_loc[1]]
        elif action == "left":
            if agent_loc[1] == 0:
                raise NotImplementedError("Agent cannot move LEFT!")
            return [agent_loc[0], agent_loc[1]-1]
        elif action == "right":
            if agent_loc[1] == self.grid-1:
                raise NotImplementedError("Agent cannot move RIGHT!")
            return [agent_loc[0], agent_loc[1]+1]
        else:
            raise NotImplementedError()

    def game_player(self, move):
        if self.game_status != 0:  # If game is done, block playing
            print("You {result} game".format(result="win" if self.game_status == 1 else "lose"))
            return
        if self.agent_point is None:
            self._game_initialization()
        try:
            new_loc = self._move(move, self.agent_point)
        except NotImplementedError as e:
            raise NotImplementedError(e)
        self.agent_point = new_loc
        result = self._result_checker(self.agent_point)
        if result == 1:
            print("Win!")
            self.game_status = 1
        elif result == -1:
            print("Lose!")
            self.game_status = -1
        else:
            self._display_board(self.agent_point)


if __name__ == "__main__":
    pass
