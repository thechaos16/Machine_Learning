# -*- coding: utf-8 -*-

import gym


class CartPoleQLearning:
    def __init__(self, env, learning_rate=0.1, discount_rate=0.9, epsilon=0.1):
        self.env = env
        self.action_space = self.env.action_space.n
        self.learning_rate = learning_rate
        self.discount_rate = discount_rate
        self.epsilon = epsilon
        self.q_table = []

    def add_memory(self, **kwargs):
        # check if state-action set is already trained
        if True:
            pass
        else:
            self.q_table.append(kwargs)

    def train(self, state, action, reward, next_state):
        pass

    def action(self, state):
        pass


def action_strategy(func):
    env = gym.make('CartPole-v0')
    env.reset()
    for iteration in range(1000):
        env.render()
        env.step(func(iteration))


def action_with_memory(func):
    env = gym.make('CartPole-v0')
    env.reset()
    memory = []
    for iteration in range(1000):
        env.render()
        action_for_cur = func(iteration, memory)
        env.step(action_for_cur)
        memory.append(action_for_cur)


def action_with_memory_and_observation(func):
    env = gym.make('CartPole-v0')
    env.reset()
    memory = {'observation': [], 'reward': [], 'action': []}
    observation = None
    reward = None
    done = None
    info = None
    for iteration in range(1000):
        env.render()
        action_for_cur = func(iteration, memory, observation, reward, done, info)
        observation, reward, done, info = env.step(action_for_cur)
        memory['action'].append(action_for_cur)
        memory['observation'].append(observation)
        memory['reward'].append(reward)
    return memory


if __name__ == 'main':
    pass
