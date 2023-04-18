import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import scipy.stats as stats
import math


def add_qq(fig, series, row, col):
    """function to create a qq plot based on a series that is passed into it and returns it to the row/col of the subplot object
    currently can't pass datetime objects"""
    qq = stats.probplot(series)
    x, y = qq[0]
    line = [x.min(), x.max()]
    a = qq[1]

    # add qq-scatterplot
    fig.add_trace(go.Scatter(x=x, y=y, mode="markers", marker_size=5), row, col)
    # manually generate regression line
    fig.add_trace(
        go.Scatter(
            x=[line[0], line[1]],
            y=[a[1] + a[0] * line[0], a[1] + a[0] * line[1]],
            mode="lines",
            line_color="red",
            line_width=2,
        ),
        row,
        col,
    )

    fig.update_xaxes(title_text=f"{series.name}", row=row, col=col)
    # fig.update_yaxes(title_text="Ordered Values", row=row, col=col)


def make_qq_plots(dataframe, sub_cols=3):
    """function that creates a plotly subplot object with automatic rows and columns for a dataframe"""
    sub_rows = math.ceil(len(dataframe.columns) / sub_cols)
    print(sub_rows, sub_cols)
    pos = [[i + 1, j + 1] for i in range(sub_rows) for j in range(sub_cols)]
    fig_qq = make_subplots(sub_rows, sub_cols)

    for i, column in enumerate(dataframe):
        add_qq(fig_qq, dataframe[column], pos[i][0], pos[i][1])

    fig_qq.update_layout(showlegend=False, width=sub_cols * 400, height=sub_rows * 400)
    return fig_qq
