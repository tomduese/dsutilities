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
