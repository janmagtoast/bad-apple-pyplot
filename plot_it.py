import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

# Import prerendered data to speed up loading time and allow for longer animations
import pickle
with open('already_computed_data.pkl', 'rb') as f:
    already_computed_data = pickle.load(f)

width, height, hor_res, line_amount, x, y = already_computed_data

offset = 1/hor_res

fig, ax = plt.subplots()
ax.set_xlim(-offset, hor_res-offset)
ax.set_ylim(0, height)
ax.set_aspect(hor_res/height, adjustable='box')

lines = [ax.plot(x, y[0][l], '-o', lw=0.1, ms=4)[0] for l in range(line_amount)]

def update(frame):
    for i in range(line_amount):
        lines[i].set_ydata(y[frame][i])
    return lines


# All the music bits
import vlc
p = vlc.MediaPlayer('music.mp3')
p.play()


# Start animation
fps = 30
anim = FuncAnimation(plt.gcf(), update, frames=len(y), interval=1000/fps, blit=True)

plt.show()
