import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.widgets import Slider
import math

#define constants
s = 10
p = 28
b = 8/3

#initialize variables
x0 = 0.2
y0 = 0.2
z0 = 0.2

#define ODEs

def lorenz(t,v):
    x,y,z = v
    dxdt= s*(y-x)
    dydt= x*(p-z) -y
    dzdt= x*y - b*z
    return [dxdt, dydt, dzdt]

def solve_lorenz(x0, y0, z0):
    t_eval = np.linspace(0, 50, 5000)
    solution = solve_ivp(lorenz, (0, 50), [x0, y0, z0], t_eval=t_eval)
    return solution


solution = solve_lorenz(x0, y0, z0)

# fig, axs = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# lines = []
# for i, (ax, label) in enumerate(zip(axs, ['x(t)', 'y(t)', 'z(t)'])):
#     line, = ax.plot(solution.t, solution.y[i], label=label)
#     ax.set_ylabel(label)
#     ax.set_title(f'{label} vs t')
#     ax.legend()
#     lines.append(line)
# axs[-1].set_xlabel('Time (t)')

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(solution.y[1], solution.y[2], label='x vs y')

color = 'red'

# x0_slider_ax = fig.add_axes([0.2, 0.02, 0.6, 0.03], facecolor=color)
# x0_slider = Slider(x0_slider_ax, 'x0', 0.1, 10.0, valinit=x0)

# y0_slider_ax = fig.add_axes([0.2, 0.06, 0.6, 0.03], facecolor=color)
# y0_slider = Slider(y0_slider_ax, 'y0', 0.1, 10.0, valinit=y0)

# z0_slider_ax = fig.add_axes([0.2, 0.1, 0.6, 0.03], facecolor=color)
# z0_slider = Slider(z0_slider_ax, 'z0', 0.1, 10.0, valinit=z0)

# def update(val):
#     x0_new = x0_slider.val
#     y0_new = y0_slider.val
#     z0_new = z0_slider.val
#     new_solution = solve_lorenz(x0_new, y0_new, z0_new)
#     for i, line in enumerate(lines):
#         line.set_ydata(new_solution.y[i])
#     fig.canvas.draw_idle()

# x0_slider.on_changed(update)
# y0_slider.on_changed(update)
# z0_slider.on_changed(update)

# plt.tight_layout()
plt.show()
plt.savefig("projections.png")