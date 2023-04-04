import methods.dsplotlib as dsplot
import methods.dsfunctions as dsf
import methods.gradient_descent as gd
import methods.plotlyplotlib as pqq
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("data/carseats.csv")
df = dsf.rename_columns(df)
# corr = df[["sales", "price", "shelveloc", "advertising", "age", "income", "us"]].corr()
# fig, ax = dsplot.corrplot(corr)
# plt.show()


qqplots = pqq.make_qq_plots(df[["sales", "price", "advertising", "age", "income"]])
qqplots.show()
#
