import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 1. Line plot: a sine wave
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)
plt.figure()
plt.plot(x, y)
plt.title("Line plot: sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.savefig("plot1_line.png")

# 2. Scatter plot: noisy straight line
rng = np.random.default_rng(0)
xs = rng.uniform(0, 10, 100)
ys = 2 * xs + 1 + rng.normal(0, 2, 100)
plt.figure()
plt.scatter(xs, ys, s=15)
plt.title("Scatter plot: y = 2x + 1 plus noise")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("plot2_scatter.png")

# 3. Histogram: bell-curve data
data = rng.normal(loc=50, scale=10, size=1000)
plt.figure()
plt.hist(data, bins=30)
plt.title("Histogram: 1000 random values")
plt.xlabel("value")
plt.ylabel("count")
plt.savefig("plot3_hist.png")

print("mean:", data.mean(), "std:", data.std())
print("saved 3 plots")
