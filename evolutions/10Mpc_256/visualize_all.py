import numpy as np
import yt

num_snapshots = 2
base = 'output/'
ss_files = [base+f for f in os.listdir(base) if f[:8]=='snapshot'] 

print(ss_files)

unit_base = {'UnitLength_in_cm'         : 3.085680e+21,
             'UnitMass_in_g'            : 1.9889225e33,
             'UnitVelocity_in_cm_per_s' :      100000}

bbox_lim = 10000 #kpc

bbox = [[0,bbox_lim],
        [0,bbox_lim],
        [0,bbox_lim]]


ds = yt.load(fname,unit_base=unit_base,bounding_box=bbox)
ds.index
ad= ds.all_data()

print(sorted(ds.field_list))

px = yt.ParticlePlot(ds, ('PartType1', 'particle_position_x'), ('PartType1', 'particle_position_y'))
px.save("ex.png")





