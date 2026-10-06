import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 101)

o1 = np.ones_like(n, dtype=float)
ologn = np.log2(n)
on = n
on2 = n ** 2

plt.figure(figsize=(10, 6))

plt.plot(n, o1, label="O(1)", linewidth=2)
plt.plot(n, ologn, label="O(log n)", linewidth=2)
plt.plot(n, on, label="O(n)", linewidth=2)
plt.plot(n, on2, label="O(n²)", linewidth=2)

plt.xlabel("Input size (n)")
plt.ylabel("Operations")
plt.title("Big-O Growth Rates")

plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()

