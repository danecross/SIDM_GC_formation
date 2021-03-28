

import numpy as np
import h5py as hpy

particle_file = "particles_dmonly_256.dat"


def to_hdf5(particle_file, output_filename="IC.hdf5"):
    
    f = open(particle_file, 'rb')
    dm_nums = np.load(f)
    dm_mass = np.load(f)
    dm_pos = (np.load(f)* 1e3).astype(float)
    dm_vel = np.load(f).astype(float)
    f.close()

    num_particles = [0] + list(dm_nums)

    mass_header = [0] + [mass*1e-10 for mass in dm_mass]

    IC_file = hpy.File(output_filename, 'w')
    DM = IC_file.create_group("DM_Particle")

    DM.create_dataset("Coordinates", data=dm_pos)
    DM.create_dataset("Velocities", data=dm_vel)
    DM.create_dataset("Masses", data=dm_mass)

    IC_file.close()

    


