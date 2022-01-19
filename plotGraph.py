# __author:Smita Nannaware
# data:12/13/2021
from copy import deepcopy

import time
import geopandas as geopandas
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import plotly.express as px
import pandas as pd

from descartes import PolygonPatch

states = None
state_colors = None
fig, ax = plt.subplots()
ax.set_axis_off()


def plotStatePatch(axes, state, color):
    st = states[states.STUSPS == state]
    st_geom = st.__geo_interface__['features']  # geopandas's geo_interface
    namig0 = {'type': st_geom[0]['geometry']['type'], \
              'coordinates': st_geom[0]['geometry']['coordinates']}
    axes.add_patch(PolygonPatch(namig0, fc=color, ec="black", alpha=0.85, zorder=2))


def animate(i):
    if len(state_colors) > 0:
        state, color = state_colors.pop(0)
        #print(state, color)
        if state not in ('AK', 'HI'):
            plotStatePatch(ax, state, color)
            ax.plot()
            if i == 0:
                time.sleep(10)


def dataplot(color_path):
    global states, state_colors, ax, fig

    path = "cb_2018_us_state_5m/"
    states = geopandas.read_file(path + 'cb_2018_us_state_5m.shp')
    states = states[states.NAME != 'District of Columbia']
    states = states[states.NAME != 'United States Virgin Islands']
    states = states[states.NAME != 'Commonwealth of the Northern Mariana Islands']
    states = states[states.NAME != 'American Samoa']
    states = states[states.NAME != 'Puerto Rico']
    states = states[states.NAME != 'Guam']
    states = states[states.NAME != 'Hawaii']
    states = states[states.NAME != 'Alaska']
    print(type(states))
    ax = states.plot(edgecolor=u'gray', color='white', ax=ax)
    state_colors = deepcopy(color_path)
    # plotStatePatch(ax2, 'NC', 'red')
    frames = len(color_path)
    ani = animation.FuncAnimation(fig, animate,
                                  frames=frames, interval=20)
    ani.save('animation.gif', writer='imagemagick', fps=100)
    plt.show()
