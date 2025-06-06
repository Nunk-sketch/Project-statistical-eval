import numpy as np
import matplotlib.pyplot as plt
import sklearn.model_selection as skm
import sklearn.linear_model as sklm

import numpy as np
from sklearn.model_selection import KFold # Anbefales stærkt for robust fold-generering
from sklearn.linear_model import LinearRegression # Eksempelmodel

def Cross_validation_robust(model, x, y, k=10, random_state=None):
    """
    Performs k-fold cross-validation to estimate the model's error.

    Parameters:
    model : A scikit-learn compatible model object with 'fit' and 'predict' methods.
            E.g. LinearRegression(), DecisionTreeRegressor(), etc.
    x : array-like
        Input features.
    y : array-like
        Target values.
    k : int, optional
        Number of folds (default is 10).
    random_state : int, optional
        Seed for randomization for reproducibility.

    Returns:
    mean_error : float
        The average error across all folds.
    std_error : float
        The standard deviation of the errors across all folds.
    """
    kf = KFold(n_splits=k, shuffle=True, random_state=random_state)
    errors = []

    for train_index, val_index in kf.split(x):
        x_train, x_val = x[train_index], x[val_index]
        y_train, y_val = y[train_index], y[val_index]

        # fit model on training data
        model.fit(x_train.reshape(-1, 1) if x_train.ndim == 1 else x_train, y_train)

        # predict on validation data
        predictions = model.predict(x_val.reshape(-1, 1) if x_val.ndim == 1 else x_val)

        # compute error (mean squared error)
        error = np.mean((predictions - y_val) ** 2)
        errors.append(error)

    return np.mean(errors), np.std(errors)


#################### example #####################
if __name__ == "__main__":
    # dummy data generation
    np.random.seed(0)
    X = np.random.rand(100) * 10
    y = 2 * X + 1 + np.random.randn(100) * 2 # linear relation with noise

    # convertion to 2D array if necessary
    if X.ndim == 1:
        X = X.reshape(-1, 1)

    # choice of model
    my_model = LinearRegression()

    # performing  cross-validation
    mean_mse, std_mse = Cross_validation_robust(my_model, X, y, k=5, random_state=42)

    print(f"Gennemsnitlig MSE over 5 folds: {mean_mse:.2f}")
    print(f"Standardafvigelse af MSE: {std_mse:.2f}")

    # Example with function (for comparison, less robust)
    # Remember to reshape X and y for if X is 1D
    # X_flat = X.flatten() # Convert back to 1D 
    # mean_error_original = Cross_validation(X_flat, y, k=5)
    # print(f"Average MSE with original function (not randomized): {mean_error_original:.2f}")