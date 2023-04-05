### Setting a standard style for matplotlib for your notebook

```
import matplotlib.pyplot as plt

# You can check for the available styles and use them
print(plt.style.available)

plt.style.use('ggplot')


# You can customize the style custom_style.mplstyle

axes.titlesize : 24
axes.labelsize : 20
lines.linewidth : 2
lines.markersize : 10
xtick.labelsize : 16
ytick.labelsize : 16
legend.fontsize : 14
figure.figsize : [8, 6]

# And safe it in a path so you do not have to set it in every notebook again
plt.style.use('/path/to/your/custom_style.mplstyle')

# Make sure to use the correct path to your safed style



```