import numpy as np
import matplotlib.pyplot as plt


def cal_cost(b, X, y):
    """
    Calculates the cost for given X and y. The following shows and example of a single dimensional X
    b = Vector of parameters
    X     = Row of X's np.zeros((2,j))
    y     = Actual y's np.zeros((2,1))

    where:
        j is the # of features
    """

    n = len(y)

    predictions = X.dot(b)
    cost = 1 / (2 * n) * np.sum(np.square(predictions - y))
    return cost


def gradient_descent_batch(X, y, b, learning_rate=0.01, iterations=100):
    """
    X = Matrix of X with added bias units
    y = Vector of y
    b = Vector of parameters np.random.randn(j,1)
    learning_rate
    iterations = # of iterations

    Returns the final b vector and array of cost history over # of iterations
    """
    n = len(y)
    cost_history = np.zeros(iterations)
    b_history = np.zeros((iterations, 2))

    for it in range(iterations):
        prediction = np.dot(X, b)

        b = b - learning_rate * (1 / n) * (X.T.dot((prediction - y)))
        b_history[it, :] = b.T
        cost_history[it] = cal_cost(b, X, y)

    return b, cost_history, b_history


def plot_GD(X, y, n_iter, lr, ax, ax1=None):
    """
    n_iter = # of iterations
    lr = Learning Rate
    ax = Axis to plot the Gradient Descent
    ax1 = Axis to plot cost_history vs Iterations plot

    """

    X_b = np.c_[np.ones((len(X), 1)), X]
    _ = ax.plot(X, y, "b.")
    b = np.random.randn(2, 1)

    tr = 0.1
    cost_history = np.zeros(n_iter)
    for i in range(n_iter):
        pred_prev = X_b.dot(b)
        b, h, _ = gradient_descent(X_b, y, b, lr, 1)
        pred = X_b.dot(b)

        cost_history[i] = h[0]

        if i % 25 == 0:
            _ = ax.plot(X, pred, "r-", alpha=tr)
            if tr < 0.8:
                tr = tr + 0.2
    if not ax1 == None:
        _ = ax1.plot(range(n_iter), cost_history, "b.")


def plot_GD_with_iter(X, y):
    """
    X = 2 * np.random.rand(100,1)
    y = 4 + 3 * X + np.random.randn(100,1)

    to plot the figure simply run:
    fig = gd.plot_GD_with_iter(X,y)
    plt.show()
    """
    fig = plt.figure(figsize=(10, 8))
    fig.subplots_adjust(hspace=0.4, wspace=0.4)

    it_lr = [(2000, 0.001), (500, 0.01), (200, 0.05), (100, 0.1)]
    count = 0
    for n_iter, lr in it_lr:
        count += 1

        ax = fig.add_subplot(4, 2, count)
        count += 1

        ax1 = fig.add_subplot(4, 2, count)

        ax.set_title("lr:{}".format(lr))
        ax1.set_title("Iterations:{}".format(n_iter))
        plot_GD(X, y, n_iter, lr, ax, ax1)
    return fig


def stochastic_gradient_descent(X, y, b, learning_rate=0.01, iterations=10):
    """
    X    = Matrix of X with added bias units
    y    = Vector of y
    b    = Vector of parameters np.random.randn(j,1)
    learning_rate
    iterations = # of iterations

    Returns the final b vector and array of cost history over # of iterations
    """
    n = len(y)
    cost_history = np.zeros(iterations)

    for it in range(iterations):
        cost = 0.0
        for i in range(n):
            rand_ind = np.random.randint(0, n)
            X_i = X[rand_ind, :].reshape(1, X.shape[1])
            y_i = y[rand_ind].reshape(1, 1)
            prediction = np.dot(X_i, b)

            b = b - (1 / 1) * learning_rate * (X_i.T.dot((prediction - y_i)))
            cost += cal_cost(b, X_i, y_i)
        cost_history[it] = cost / n

    return b, cost_history


def minibatch_gradient_descent(
    X, y, b, learning_rate=0.01, iterations=10, batch_size=20
):
    """
    X    = Matrix of X without added bias units
    y    = Vector of y
    b    = Vector of parameters np.random.randn(j,1)
    learning_rate
    iterations = # of iterations

    Returns the final b vector and array of cost history over # of iterations
    """
    n = len(y)
    cost_history = np.zeros(iterations)

    for it in range(iterations):
        cost = 0.0
        indices = np.random.permutation(n)
        X = X[indices]
        y = y[indices]
        for ind, i in enumerate(range(0, n, batch_size)):
            X_i = X[i : i + batch_size]
            y_i = y[i : i + batch_size]

            X_i = np.c_[np.ones(len(X_i)), X_i]

            prediction = np.dot(X_i, b)

            b = b - (1 / batch_size) * learning_rate * (X_i.T.dot((prediction - y_i)))
            cost += cal_cost(b, X_i, y_i)
        cost_history[it] = cost / (ind + 1)  # cost/number of batches

    return b, cost_history


def gradient_descent(
    max_iterations,
    threshold,
    b_init,
    obj_func,
    grad_func,
    learning_rate=0.05,
    momentum=0.8,
):
    """
    Input:
    - max_iterations  : Maximum number of iterations to run
    - threshold       : Stop if the difference in function values between two successive iterations falls below this threshold
    - b_init          : Initial point from where to start gradient descent
    - obj_func        : Reference to the function that computes the objective function
    - grad_func       : Reference to the function that computes the gradient of the function
    - learning_rate   : Step size for gradient descent. It should be in [0,1]
    - momentum        : Momentum to use. It should be in [0,1]
    Output:
    - b_history       : All points in space, visited by gradient descent at which the objective function was evaluated
    - f_history       : Corresponding value of the objective function computed at each point
    """

    b = b_init
    b_history = b
    f_history = obj_func(b)
    delta_b = np.zeros(b.shape)
    i = 0
    diff = 1.0e10

    while i < max_iterations and diff > threshold:
        delta_b = -learning_rate * grad_func(b) + momentum * delta_b
        b = b + delta_b

        # store the history of w and f
        b_history = np.vstack((b_history, b))
        f_history = np.vstack((f_history, obj_func(b)))

        # update iteration number and diff between successive values
        # of objective function
        i += 1
        diff = np.absolute(f_history[-1] - f_history[-2])

    return b_history, f_history
