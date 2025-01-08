import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 50)

# fig, axs = plt.subplots(2, sharex=True)
#
# axs[0].plot(x, np.sin(x))
# axs[0].set_title("Sine")
# axs[1].plot(x, np.cos(x))
# axs[1].set_title("Cosine")

# fig, axs = plt.subplots(2, 2)
# axs[0][0].plot(x, np.sin(x))
# axs[0][0].set_title("Sine")
# axs[0][1].plot(x, np.cos(x))
# axs[0][1].set_title("Cosine")
# axs[1][0].plot(x, np.sqrt(x))
# axs[1][0].set_title("Square root")
# axs[1][1].plot(x, x - 1)
# axs[1][1].plot("Stright line")

# axs[0][0].grid(True)

# ax1 = plt.subplot(221)
# ax2 = plt.subplot(2, 2, 2)
#
# ax1.plot(x, np.sinh(x))
# ax2.plot(x, np.tanh(x))

plt.show()
