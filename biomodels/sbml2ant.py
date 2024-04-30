
import tellurium as te
import antimony
from os import listdir
from os.path import isfile, join
import glob
from copy import deepcopy


biomod_dirs = []
for i in range(0, 1061):
    biomod_dirs.append('BIOMD' + str(i).zfill(10))

for i, each in enumerate(biomod_dirs):
    try:
        model_files = glob.glob(each + '/*.xml')

        for item in model_files:
            if item.split('\\')[1].split('.')[0] != 'manifest' and 'Figure' not in item:
                ant_file = 'ant_files_1\\' + each + '_' + item.split('\\')[1].split('.')[0] + '.ant'

                model = te.loadSBMLModel(item)
                model.exportToAntimony(ant_file)

    except:
        print(i, 'failed')
