from sklearn.metrics import roc_curve


# Create a line plot with Matplotlib and the given parameters: x, y, xlabel, ylabel, title
def line_plot(x, y, xlabel="X", ylabel="Y", title="Line Plot"):
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid()
    plt.show()


# Create a scatter plot with Matplotlib and the given parameters: x, y, xlabel, ylabel, title
import matplotlib.pyplot as plt


def scatter_plot(x, y, xlabel="X", ylabel="Y", title="Scatter Plot"):
    plt.scatter(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid()
    plt.show()


# Create a bar plot with Matplotlib and the given parameters: categories, values, xlabel, ylabel, title
import matplotlib.pyplot as plt


def bar_plot(
    categories, values, xlabel="Categories", ylabel="Values", title="Bar Plot"
):
    plt.bar(categories, values)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(axis="y")
    plt.show()


def plot_roc(actual_values, model_values):
    fpr, tpr, thresholds_RF = roc_curve(actual_values, model_values)
    plt.plot(fpr, tpr, "r-", label="RF")
    plt.plot([0, 1], [0, 1], "k-", label="random")
    plt.plot([0, 0, 1, 1], [0, 1, 1, 1], "g-", label="perfect")
    plt.legend()
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.show()


def error_analysis(y_test, y_pred_test):
    """Generated true vs. predicted values and residual scatter plot for models

    Args:
        y_test (array): true values for y_test
        y_pred_test (array): predicted values of model for y_test
    """
    # Calculate residuals
    residuals = y_test - y_pred_test

    # Plot real vs. predicted values
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    plt.subplots_adjust(right=1)
    plt.suptitle("Error Analysis")

    ax[0].scatter(y_pred_test, y_test, color="#FF5A36", alpha=0.7)
    ax[0].plot([-400, 350], [-400, 350], color="#193251")
    ax[0].set_title("True vs. predicted values", fontsize=16)
    ax[0].set_xlabel("predicted values")
    ax[0].set_ylabel("true values")
    ax[0].set_xlim((y_pred_test.min() - 10), (y_pred_test.max() + 10))
    ax[0].set_ylim((y_test.min() - 40), (y_test.max() + 40))

    ax[1].scatter(y_pred_test, residuals, color="#FF5A36", alpha=0.7)
    ax[1].plot([-400, 350], [0, 0], color="#193251")
    ax[1].set_title("Residual Scatter Plot", fontsize=16)
    ax[1].set_xlabel("predicted values")
    ax[1].set_ylabel("residuals")
    ax[1].set_xlim((y_pred_test.min() - 10), (y_pred_test.max() + 10))
    ax[1].set_ylim((residuals.min() - 10), (residuals.max() + 10))
