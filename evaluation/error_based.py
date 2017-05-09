# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


def mse(prediction, ground_truth, normalized=False):
    prediction, ground_truth = _input_parser(prediction, ground_truth)
    number_of_features = np.shape(prediction)[0]
    mse_result = []
    for feature_idx in range(number_of_features):
        one_mse = np.sqrt(np.mean((prediction[feature_idx] - ground_truth[feature_idx])**2))
        if normalized:
            avg_mse = np.sqrt(np.mean((ground_truth[feature_idx] - np.mean(ground_truth[feature_idx]))**2))
            one_mse /= avg_mse
        mse_result.append(one_mse)
    return mse_result


def mae(prediction, ground_truth, normalized=False):
    prediction, ground_truth = _input_parser(prediction, ground_truth)
    number_of_features = np.shape(prediction)[0]
    mae_result = []
    for feature_idx in range(number_of_features):
        one_mae = np.sqrt(np.mean(np.abs(prediction[feature_idx] - ground_truth[feature_idx])))
        if normalized:
            avg_mae = np.sqrt(np.mean(np.abs(ground_truth[feature_idx] - np.mean(ground_truth[feature_idx]))))
            one_mae /= avg_mae
        mae_result.append(one_mae)
    return mae_result


def _input_parser(prediction, ground_truth):
    # if inputs are data frame, convert them into numpy list
    if type(prediction) == pd.DataFrame:
        prediction = np.array(prediction).T
    if type(ground_truth) == pd.DataFrame:
        ground_truth = np.array(ground_truth).T
    if len(np.shape(prediction)) == 1:
        prediction = prediction.reshape(1, len(prediction))
    if len(np.shape(ground_truth)) == 1:
        ground_truth = ground_truth.reshape(1, len(ground_truth))
    return prediction, ground_truth


if __name__ == "__main__":
    sample_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    real_data = np.array([1, 1, 1, 2, 2, 2, 3, 3, 3])
    print(mse(sample_data, real_data))
    print(mae(sample_data, real_data))
