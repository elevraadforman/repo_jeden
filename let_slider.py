# taken from https://matplotlib.org/stable/gallery/widgets/slider_demo.html

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


# The parametrized function to be plotted


def f(S_w, Lw, Ew, Tw):
    
    return kOrw*((S_w**Lw)/((S_w**Lw)+Ew*((1-S_w)**Tw)))

#krw = kOrw*((S_w**Lw)/((S_w**Lw)+Ew*((1-S_w)**Tw)))

t = np.linspace(0, 1, 1000)


Swir = 0.1
Sorw = 0.3
kOro = 1
kOrw = 0.6

Sw = np.linspace(Swir, 1-Sorw, 50)

S_w = (Sw - Swir)/(1- Sorw - Swir)


# Define initial parameters

init_Lw = 3
init_Ew = 3
init_Tw = 5


# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()

#ax.plot(Sw, krw, color='b')
#ax.plot(Sw, kro, color='r')

line, = plt.plot(S_w, f(Sw, init_Lw, init_Ew, init_Tw), lw=2)
ax.set_xlabel('Saturation [frac]')

# adjust the main plot to make room for the sliders
plt.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the frequency.
axLw = plt.axes([0.05, 0.25, 0.0225, 0.63])
Lw_slider = Slider(
    ax=axLw,
    label='L',
    valmin=1,
    valmax=6,
    valinit=init_Lw,
    orientation="vertical"
)
#[0.25, 0.1, 0.65, 0.03],

# Make a vertically oriented slider to control the amplitude
axEw = plt.axes([0.1, 0.25, 0.025, 0.63])
Ew_slider = Slider(
    ax=axEw,
    label="E",
    valmin=1,
    valmax=6,
    valinit=init_Ew,
    orientation="vertical"
)

# Make a vertically oriented slider to control the amplitude
axTw = plt.axes([0.15, 0.25, 0.025, 0.63])
Tw_slider = Slider(
    ax=axTw,
    label="T",
    valmin=1,
    valmax=6,
    valinit=init_Tw,
    orientation="vertical"
)


# The function to be called anytime a slider's value changes
def update(val):
    line.set_ydata(f(S_w, Lw_slider.val, Ew_slider.val, Tw_slider.val))
    fig.canvas.draw_idle()


# register the update function with each slider
Lw_slider.on_changed(update)
Ew_slider.on_changed(update)
Tw_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = plt.axes([0.8, 0.05, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    Lw_slider.reset()
    Ew_slider.reset()
    Tw_slider.reset()
button.on_clicked(reset)

plt.show()