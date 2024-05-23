import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-o')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.set_title('Фигура Лисажу')
def update_plot(frame, a):
    frequency_x = 1
    frequency_y = frame / 100
    t = np.linspace(0, 10, 500)
    x = np.sin(2 * np.pi * frequency_x * t)
    y = np.sin(2 * np.pi * frequency_y * t)
    ln.set_data(x, y)
    return ln,

ani = animation.FuncAnimation(fig, update_plot, frames=100, fargs=(1,), interval=20, blit=True)
plt.show()