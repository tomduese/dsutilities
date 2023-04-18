import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def corrplot(corr):
    # draw the heatmap
    fig = plt.figure(figsize=(10, 8))
    ax = sns.heatmap(
        corr,
        linewidths=0.5,
        annot=True,
        cmap="coolwarm",
        yticklabels=corr.columns,
        xticklabels=corr.columns,
    )
    plt.title("Your title", fontsize=20)  # title with fontsize 20
    plt.xticks(rotation=90, fontsize=12)
    plt.yticks(fontsize=12)
    return fig, ax


def another_corrplot(df):
    correlations = df.corr()
    mask = np.triu(correlations)
    sns.heatmap(correlations, vmax=1, vmin=-1, annot=True, mask=mask, cmap="YlGnBu")
