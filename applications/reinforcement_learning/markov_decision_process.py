# -*- coding: utf-8 -*-
import numpy as np
from applications.reinforcement_learning.simple_game import SimpleGame


class MarkovDecisionProcess:
    def __init__(self, env=None, number_of_grid=3, action=4, discount_rate=0.1, max_iter=10, strategy="value"):
        if env is None:
            self.env = SimpleGame(number_of_grid, [2, 2], [0, 2])  # FIXME: firstly, train on fixed game
        self.goal_loc = self.env.goal_loc
        self.doom_loc = self.env.doom_loc
        self.grid_size = number_of_grid
        self.action = action
        self.discount_rate = discount_rate
        self.max_iter = max_iter
        self.strategy = strategy
        self.action_idx = ["up", "down", "left", "right"]
        self._game_initialization()
        self._policy_value_initialization()

    def _game_initialization(self):
        # FIXME: as the first draft, use [0,0]
        self.env.game_initialization(start_point=[0, 0])
        self.agent_loc = [0, 0]

    def _policy_value_initialization(self):
        self.policy = dict()
        self.value = dict()
        # state encoding: 000000 where agent, goal, and doom are all in [0, 0]
        self.state_space_size = self.grid_size**6
        for idx in range(self.state_space_size):
            new_base = np.base_repr(idx, self.grid_size)
            idx_str = str(new_base)
            idx_len = len(idx_str)
            for i in range(6-idx_len):
                idx_str = "0"+idx_str
            self.policy[idx_str] = [0.25, 0.25, 0.25, 0.25]
            self.value[idx_str] = 0.0

    def bellman(self):
        for state in self.value.keys():
            agent_loc = [int(state[0]), int(state[1])]
            actions = self.env.get_possible_actions(agent_loc)
            bellman_init = 0.0
            for action in actions:
                if action == "up":
                    next_state = [agent_loc[0]-1, agent_loc[1]]
                elif action == "down":
                    next_state = [agent_loc[0]+1, agent_loc[1]]
                elif action == "left":
                    next_state = [agent_loc[0], agent_loc[1]-1]
                elif action == "right":
                    next_state = [agent_loc[0], agent_loc[1]+1]
                cur_reward = self._get_reward(next_state)
                new_bellman = cur_reward + self.discount_rate * self.value[
                    self._state_encoder(next_state, self.goal_loc, self.doom_loc)]
                if new_bellman > bellman_init:
                    bellman_init = new_bellman
                    self.value[state] = new_bellman
                    self.policy[state] = list((np.array(self.action_idx) == action).astype(int))

    def train(self):
        for iteration in range(self.max_iter):
            if self.strategy == "value":
                # converges
                self.bellman()
            elif self.strategy == "policy":
                pass
            else:
                raise NotImplementedError

    def _get_reward(self, agent_loc):
        if agent_loc[0] == self.goal_loc[0] and agent_loc[1] == self.goal_loc[1]:
            return 10  # hit the goal
        if agent_loc[0] == self.doom_loc[0] and agent_loc[1] == self.doom_loc[1]:
            return -10  # hit the doom
        return 0

    @staticmethod
    def _state_encoder(agent_loc, goal_loc, doom_loc):
        return "".join(np.array(agent_loc + goal_loc + doom_loc).astype(str))

    def predict(self, agent_loc):
        # state encoding
        state = self._state_encoder(agent_loc, self.goal_loc, self.doom_loc)
        policy = self.policy[state]
        idx = np.argmax(policy)
        return self.action_idx[idx]

    def game_play(self):
        # first env
        self.env.display_board(self.env.agent_point)
        while self.env.game_status == 0:
            move = self.predict(self.env.agent_point)
            print(move)
            try:
                result = self.env.game_player(move)
            except NotImplementedError:
                raise Exception("Something went wrong!")
        if self.env.game_status == 1:
            print("Win!")
        else:
            print("Lose!")


if __name__ == "__main__":
    pass
