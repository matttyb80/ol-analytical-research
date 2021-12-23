# from matplotlib import animation
# import random
# import networkx as nx
# import matplotlib.pyplot as plt

# # plt.rcParams["figure.figsize"] = [7.50, 3.50]
# # plt.rcParams["figure.autolayout"] = True

# # fig = plt.figure()

# # G = nx.DiGraph()
# # G.add_nodes_from([0, 1, 2, 3, 4])

# # nx.draw(G, with_labels=True)

# # def animate(frame):
# #    fig.clear()
# #    num1 = random.randint(0, 4)
# #    num2 = random.randint(0, 4)
# #    G.add_edges_from([(num1, num2)])
# #    nx.draw(G, with_labels=True)

# # ani = animation.FuncAnimation(fig, animate, frames=range(0,6), interval=10, repeat=True)

# # plt.show()
# # animated_line_plot.py

# from random import randint

# # create empty lists for the x and y data
# x = []
# y = []

# # create the figure and axes objects
# fig, ax = plt.subplots()
# def animate(i):
#     pt = randint(1,9) # grab a random integer to be the next y-value in the animation
#     x.append(i)
#     y.append(pt)

#     ax.clear()
#     ax.plot(x, y)
#     ax.set_xlim([0,20])
#     ax.set_ylim([0,10])

# # run the animation
# ani =animation.FuncAnimation(fig, animate, frames=20, interval=500, repeat=False, blit=False)

# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def create_video(n):
    global X
    X = np.random.binomial(1, 0.3, size = (n, n))

    fig = plt.figure()
    im = plt.imshow(X, cmap = plt.cm.gray)

    def animate(t):
        global X
        X = np.roll(X, +1, axis = 0)
        im.set_array(X)
        return im, 

    anim = FuncAnimation(
        fig,
        animate,
        frames = 100,
        interval = 1000/30,
        blit = True
    )

    plt.show()

    return anim

anim = create_video(10)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def create_video(n):
    global X
    X = np.random.binomial(1, 0.3, size = (n, n))

    fig = plt.figure()
    im = plt.imshow(X, cmap = plt.cm.gray)

    def animate(t):
        global X
        X = np.roll(X, +1, axis = 0)
        im.set_array(X)
        return im, 

    anim = FuncAnimation(
        fig,
        animate,
        frames = 100,
        interval = 1000/30,
        blit = True
    )

    plt.show()

    return anim

anim = create_video(10)

from matplotlib import animation
import random

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()

G = nx.DiGraph()
G.add_nodes_from([0, 1, 2, 3, 4])

nx.draw(G, with_labels=True)

def animate(frame):
   fig.clear()
   num1 = random.randint(0, 4)
   num2 = random.randint(0, 4)
   G.add_edges_from([(num1, num2)])
   nx.draw(G, with_labels=True)

ani = animation.FuncAnimation(fig, animate, frames=range(0,6), interval=10, repeat=True)

plt.show()