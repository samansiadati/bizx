from sklearn.linear_model import LinearRegression


def linear_regression(x, y):
    """
    Fit a linear regression model.

    Parameters
    ----------
    x : array-like
        Feature data.
    y : array-like
        Target values.

    Returns
    -------
    model : LinearRegression
        Fitted scikit-learn linear regression model.
    score : float
        R² score of the fitted model.
    coefficients : ndarray
        Regression coefficients.
    intercept : float
        Regression intercept.
    """
    model = LinearRegression().fit(x, y)

    return (
        model,
        model.score(x, y),
        model.coef_,
        model.intercept_,
    )
