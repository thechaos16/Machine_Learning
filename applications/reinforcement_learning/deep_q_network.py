# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from models.keras_models.neural_network import NeuralNetwork


class DeepQNetwork(NeuralNetwork):
    """
    General version of deep q network which can be adapted any environment
    """
    def __init__(self):
        pass

    def _environment_handler(self):
        pass

    def experience_replay(self):
        pass

    def fit(self):
        pass

    def predict(self):
        pass

    def experiment(self):
        pass


if __name__ == "__main__":
    pass
