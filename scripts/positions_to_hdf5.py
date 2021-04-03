

import numpy as np
import h5py as hpy

def to_hdf5(particle_file, num_particles=256, output_filename="IC.hdf5"):
    
    f = open(particle_file, 'rb')
    
    IC_file = hpy.File(output_filename, 'w')
    h = IC_file.create_group("Header")
    
    #write header
    npart = np.array([0,num_particles**3, 0, 0, 0, 0])
    h.attrs['NumPart_ThisFile']=npart
    h.attrs['NumPart_Total'] = npart
    h.attrs['NumPart_Total_HighWord'] = 0*npart
    h.attrs['MassTable'] = np.zeros(6)

    h.attrs['Time'] = 0.0
    h.attrs['NumFilesPerSnapshot'] = 1
    h.attrs['Flag_DoublePrecision'] = 0

    nums = np.load(f)
    mass = np.load(f)
    pos = (np.load(f)* 1e3).astype(float)
    vel = np.load(f).astype(float)

    P = IC_file.create_group("PartType1")

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

    


