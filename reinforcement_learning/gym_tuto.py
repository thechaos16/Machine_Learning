# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:54:29 2016

@author: thech
"""

import gym


def cartpole():
    env = gym.make('CartPole-v0')
    env.reset()
    for _ in range(1000):
        env.render()
        env.step(env.action_space.sample())


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
        

def simplest_q_learner(func):
    pass


if __name__ == 'main':
    pass
