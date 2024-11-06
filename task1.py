import numpy as np
import matplotlib.pyplot as plt

def y(x):
    return 0.3 * x**2 + np.fabs(x**2)

x = np.linspace(0, 10, 51)
y = y(x)

plt.plot(y, x, "g--", label="0.3x^2+|x|")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Func")
plt.legend()
plt.savefig("funcGraph.png", format="png", dpi=300)
plt.show()
