import numpy as np
import matplotlib.pyplot as plt

# NOTE: np(start, end, num)
# start:    the first digit
# stop:      the last digit
# num:      number of digits in between
x = np.linspace(start=-2 * np.pi, stop=2 * np.pi, num=50)

# NOTE: plot([x], [y], fmt, data=None, **kwargs)
# fmt:  [color][line][marker] in any order

# plt.plot(x, np.sin(x), '.-r')
plt.plot(x, np.cos(x), '.--b')

plt.title("plt.plot(x, np.cos(x), '.--b')")

plt.xlabel("x", loc="center")
plt.ylabel('y', loc="center")

plt.show()

# plt.minorticks_on()
# plt.grid(visible=True, which='major', axis='both')
# plt.grid(visible=True, which='both', axis='both', color='r', linestyle=':', linewidth=1)

# 'best' (Axes only) 0
# 'upper right' 1
# 'upper left' 2
# 'lower left' 3
# 'lower right' 4
# 'right' 5
# 'center left' 6
# 'center right' 7
# 'lower center' 8
# 'upper center' 9
# 'center' 10

# plt.legend(('sine', 'cosine'), loc=0)

# plt.title("Sine-Cosine")
# plt.title("Sine-Cosine", fontsize=10, fontweight='bold')

# plt.savefig('testplot.jpg', format="jpg")

plt.show()
