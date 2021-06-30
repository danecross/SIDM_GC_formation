
from subprocess import call
import sys
import shutil

names_file = open(sys.argv[1],'r')
path = sys.argv[1][:-len("output_snapshot_names.txt")]

i = 16
for file in names_file:

	file = file[:-1]
	num = file[-8:-5]

	ret_code = call(["./rockstar/rockstar", "-c", "rockstar/quickstart.cfg", path+"../output/"+file])
	print(ret_code)

	try:
		shutil.move("halos_0.0.ascii", path+"../output/ROCKSTAR_groups/halos_0."+num+".ascii") 
		shutil.move("halos_0.0.bin", path+"../output/ROCKSTAR_groups/halos_0."+num+".bin")	
	except Exception as e:
		print("error with: ", file)
		print(str(e))
	i+=1
