import numpy as np

a = np.array([1, 2, 3, 4, 5])
print("a:", a, "shape:", a.shape)

b = np.arange(12).reshape(3, 4)
print("b:\n", b)
print("shape:", b.shape)
print("row 1:", b[1])
print("column 2:", b[:, 2])
print("top-left 2x2:\n", b[:2, :2])

print("a * 2:", a * 2)
print("a squared:", a ** 2)
print("sum:", a.sum(), "mean:", a.mean())

print("column means:", b.mean(axis=0))
print("row sums:", b.sum(axis=1))
print("b minus column means:\n", b - b.mean(axis=0))

print("even numbers in b:", b[b % 2 == 0])
