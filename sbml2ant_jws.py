
import tellurium as te
from os import listdir
from os.path import isfile, join
import glob
from copy import deepcopy


directory = 'jws_models_test'

model_files = glob.glob(directory + '/*.xml')

for i, each in enumerate(model_files):
    try:
        print(i, each)
        ant_file = deepcopy(each)
        ant_file = ant_file.replace('\\', '\\ant_files\\')
        ant_file = ant_file.split('.')[0] + '.ant'

        model = te.loadSBMLModel(each)
        model.exportToAntimony(ant_file)
    except:
        print(i, "failed")
