# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import gym
from keras_models.neural_network import NeuralNetwork


class CartPoleAgent(NeuralNetwork):
    def __init__(self, env, decay_rate=0.5, epsilon=1.0, learning_rate=0.01):
        # build model
        super.__init__(self, 4, 2, number_of_nodes=128)
        self.env = env
        self.memory = []
        self.epsilon = epsilon
        self.decay_rate = decay_rate
        self.learning_rate = learning_rate


if __name__ == "__main__":
    pass
