

import numpy as np
import h5py as hpy

def to_hdf5(particle_file, num_particles=1, output_filename="IC.hdf5"):
    
    f = open(particle_file, 'rb')

    for i in range(num_particles):
        nums = np.load(f)
        mass = np.load(f)
        pos = (np.load(f)* 1e3).astype(float)
        vel = np.load(f).astype(float)

        IC_file = hpy.File(output_filename, 'w')
        P = IC_file.create_group("PartType"+str(i))
        header = IC_file.create_group("Header")

        P.create_dataset("ParticleIDs", data=list(range(len(pos))))
        P.create_dataset("Coordinates", data=pos)
        P.create_dataset("Velocities", data=vel)
        
        if len(nums) != 1:
            P.create_dataset("Masses", data=mass)
        else:
            m = list(mass)*pos.shape[0] 
            P.create_dataset("Masses",data=m)
   

    f.close()
    IC_file.close()

    


