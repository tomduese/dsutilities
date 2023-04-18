# Defining function which calculates residuals and plots them
def get_residuals(dataset, color):
    pass
    # # store true y values
    # obs_values = anscombe[anscombe.dataset == dataset].y
    # # store predicted y values
    # pred_values = (
    #     get_summarystats(dataset)[0] * anscombe[anscombe.dataset == dataset].x
    #     + get_summarystats(dataset)[1]
    # )
    # # calculate residuals
    # residuals = obs_values - pred_values
    # # plot residuals
    # fig, ax = plt.subplots(figsize=(8, 4))
    # ax.scatter(anscombe[anscombe.dataset == dataset].x, residuals, color=color)
    # ax.set_ylabel("Residuals")
    # ax.set_xlabel("x")
    # fig.suptitle("Residual Scatter Plot")
    # plt.show()


# Define function for calculating adjusted r-squared
def adjusted_r_squared(r_squared, X):
    adjusted_r2 = 1 - ((1 - r_squared) * (len(X) - 1) / (len(X) - X.shape[1] - 1))
    return adjusted_r2
