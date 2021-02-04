

import numpy as np

# shape 3x64x64x64
grid64 = np.load('lizard/example_scripts/box100/grids/displ_grid_64.npy')
print(type(grid64[0][0][0][0]), type(grid64[1][0][0][0]), type(grid64[2][0][0][0]))

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

import itertools
coords = list(itertools.product(range(1,65), range(1,65), range(1,65)))

x = [coords[i][0] for i in range(len(coords))]
y = [coords[i][1] for i in range(len(coords))]
z = [coords[i][2] for i in range(len(coords))]

rgba_colors = np.zeros((len(coords),4))
rgba_colors[:,0] = 1.0
rgba_colors[:,3] = [1.0+grid64[2][x-1][y-1][z-1] for x,y,z in coords]


print(np.min(rgba_colors))
ax.scatter(x, y, z, c=rgba_colors/(390*np.max(rgba_colors)),depthshade=False)

plt.savefig("visual.png")
#plt.show()



