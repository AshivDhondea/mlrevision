import numpy as np
import os


def run_univariate_gradient_descent(xin, y, theta, alpha):
    # TODO: Priority: medium: re-factor this method.
    # This function performs one iteration of univariate gradient descent
    # and returns an updated set of theta values
    h_theta = np.dot(theta, xin)  # Compute the estimate and find the difference between it and the true vallue of y
    difference = h_theta - y
    sum_term = np.dot(xin, difference)

    theta[0] = theta[0] - (alpha / len(y)) * sum_term[0]
    theta[1] = theta[1] - (alpha / len(y)) * sum_term[1]
    return theta


def evaluate_cost_function(xin, y, theta):
    # TODO: Priority: medium: re-factor this method.
    # This function computes the value of the cost function J(theta)
    h_theta = np.dot(theta, xin)
    difference = h_theta - y
    squared_difference = np.square(difference)
    cost = (0.5 / np.shape(y)[0]) * np.sum(squared_difference)
    return cost


def run_linear_regression_project():
    # Read data file and extract data.
    dataset_path = os.path.abspath('../mlrevision/coursera_ml/datasets/data.txt')

    if not os.path.isfile(dataset_path):
        fnf_error = f"File {dataset_path} not found."
        raise FileNotFoundError(fnf_error)

    with open(dataset_path) as f:
        content = f.readlines()

    pass

