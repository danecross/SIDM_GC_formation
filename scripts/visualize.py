
from pprint import pprint
import yt
from matplotlib.animation import FuncAnimation
from matplotlib import rc_context
from matplotlib import pyplot as plt
import os

yt.toggle_interactivity()

data_path = "../evolutions/10Mpc_256_CDM/output/"

available_snapshots = [i for i in range(0, 110) if os.path.exists(data_path+"snapshot_%03i.hdf5"%(i))]
data_list = [data_path+"snapshot_%03i.hdf5"%(i) for i in available_snapshots]

for data in data_list:
    ds = yt.load(data)
    plot = yt.ParticlePlot(ds, 'particle_position_x', 'particle_position_y', 'particle_mass')
    plot.save("snapshot_density_plots_CDM/"+data[-8:-5])



'''
fig = plt.figure()
ts = yt.DatasetSeries(data_list)


def animate(i):
    ds = ts[i]
    plot._switch_ds(ds)

animation = FuncAnimation(fig, animate, frames=len(ts))

# Override matplotlib's defaults to get a nicer looking font
with rc_context({'mathtext.fontset': 'stix'}):
    #writergif = animation.PillowWriter(fps=30)
    animation.save('animation.gif')
'''

