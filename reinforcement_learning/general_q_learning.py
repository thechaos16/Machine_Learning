# -*- coding: utf-8 -*-

import numpy as np


class QLearner:
    def __init__(self, initial_state, action_space, learning_rate=0.1, discount_rate=0.9, epsilon=0.1):
        self.action_space = action_space
        self.learning_rate = learning_rate  # alpha
        self.discount_rate = discount_rate  # gamma
        self.epsilon = epsilon
        self.q_table = dict({})
        self.state_hash_map = []
        self._initialize_q_table(initial_state)

    def _add_new_state(self, state):
        self.state_hash_map.append(state)

    def _state_approximation(self, state):
        for key in range(len(self.state_hash_map)):
            if self.state_hash_map[key] == state:
                return key
        return -1

    def _initialize_q_table(self, initial_state):
        self._add_new_state(initial_state)

    def _update_q_table(self, state, action, reward, next_state):
        state_key = self._state_approximation(state)
        # new_state
        if state_key == -1:
            # TODO: add new state, action tuple and update it with reward and future value)
            self._add_new_state(state)
        else:
            # reference: Q(s,a) = Q(s,a) + alpha * (reward + gamma * future_value - Q(s,a))
            pass

    def train(self, state, action, reward, next_state):
        pass

    def action(self, state):
        # epsilon-greedy
        if np.random.random() <= self.epsilon:
            return self.env.action_space.sample()


if __name__ == 'main':
    pass
