# -*- coding: utf-8 -*-

import numpy as np


class QLearner:
    def __init__(self, initial_state, action_space, learning_rate=0.1, discount_rate=0.9, epsilon=0.1):
        """
        
        :param initial_state: 
        :param action_space: size of possible actions
        :param learning_rate: learning rate for update q table (alpha in Bellman equation)
        :param discount_rate: discount rate for future q value (gamma in Bellman equation)
        :param epsilon: probability for exploration
        """
        self.action_space = action_space
        self.learning_rate = learning_rate  # alpha
        self.discount_rate = discount_rate  # gamma
        self.epsilon = epsilon
        self.q_table = []
        self.state_hash_map = []
        self._initialize_q_table(initial_state)

    def _add_new_state(self, state):
        self.state_hash_map.append(state)
        action_list = np.random.random(len(self.action_space))  # arbitrary action value
        self.q_table.append(action_list)

    # NOTE: since neural network is already implemented in cart_pole_agent, in here, using other method like grid
    def _state_approximation(self, state):
        for key in range(len(self.state_hash_map)):
            if self.state_hash_map[key] == state:
                return key
        return -1

    def _initialize_q_table(self, initial_state):
        # Note: late-update q-table after seeing states
        self._add_new_state(initial_state)

    def _update_q_table(self, state, action, reward, next_state):
        state_key = self._state_approximation(state)
        # new_state
        if state_key == -1:
            # TODO: add new state, action tuple and update it with reward and future value)
            self._add_new_state(state)
        else:
            # Bellman equation: Q(s,a) = Q(s,a) + alpha * (reward + gamma * future_value - Q(s,a))
            state_key = self._state_approximation(state)
            next_state_key = self._state_approximation(next_state)
            self.q_table[state_key][action] += self.learning_rate *\
                                               (reward + self.discount_rate * np.max(self.q_table[next_state_key]) -
                                                self.q_table[state_key][action])

    def train(self, state):
        # epsilon-greedy
        if np.random.random() <= self.epsilon:
            pass
        pass

    def action(self, state):
        q_table_for_state = self.q_table[state]
        # check rewards
        max_val = -np.inf
        max_key = None
        for key in q_table_for_state:
            if q_table_for_state[key] > max_val:
                max_key = key
                max_val = q_table_for_state[key]
        return max_key


if __name__ == 'main':
    pass
