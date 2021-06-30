
import sys
import numpy as np
import h5py as hpy

names_file = open(sys.argv[1],'r')
path = sys.argv[1][:-len("output_snapshot_names.txt")]

file_list = [path+"../output/"+line[:-1] for line in names_file]

for filename in file_list:
	f = hpy.File(filename, 'r+')
	try:
		h = f["Header"]

		O0 = h.attrs.get("Omega_Matter")
		h.attrs.create("Omega0", O0)

		OL = h.attrs.get("Omega_Lambda")
		h.attrs.create("OmegaLambda", OL)

		DM = f["PartType1"]

		masses = DM["Masses"]
		am = np.average(masses)

		mt = np.array([am]*6)
		h.attrs.modify("MassTable", mt)
	except KeyError:
		print("error with file" + filename)


	f.close()

names_file.close()

