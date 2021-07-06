
import os
import shutil
import numpy as np

import yt
from yt.units import parsec, Msun

yt.toggle_interactivity()

snap_data_path = "../evolutions/10Mpc_256/output/"
groups_data_path = "../evolutions/10Mpc_256/output/ROCKSTAR_groups/"

available_outputs = [i for i in range(0, 110) if os.path.exists(groups_data_path+"halos_0.%03i.bin"%(i)) \
                                             and os.path.exists(snap_data_path+"snapshot_%03i.hdf5"%(i)) \
					     and not os.path.exists("snapshot_density_plots_groups/%i_Particle_z_particle_mass.png"%(i))]

if len(available_outputs) == 0:
    print("no compatible snapshot and rockstar group files.")
    print("snapshot path: %s"%(snap_data_path))
    print("groups path: %s"%(groups_data_path))
    exit()

snap_data_list = [snap_data_path+"snapshot_%03i.hdf5"%(i) for i in available_outputs]
groups_data_list = [groups_data_path+"halos_0.%03i.bin"%(i) for i in available_outputs] 

for snap, groups, num in zip(snap_data_list, groups_data_list, available_outputs):
   
    shutil.copyfile(groups, "./halos_0.0.bin")

    # plot particle desity map
    ds = yt.load(snap)
    halos_ds = yt.load("halos_0.0.bin")
    plot = yt.ParticlePlot(ds, 'particle_position_x', 'particle_position_y', 'particle_mass')
    plot.annotate_halos(halos_ds)
    
    plot.save("snapshot_density_plots_groups/"+str(num))


