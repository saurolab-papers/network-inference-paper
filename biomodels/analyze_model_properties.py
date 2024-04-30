
import tellurium as te
import antimony
from os import listdir
from os.path import isfile, join
import glob
from copy import deepcopy

directory = 'ant_files'

model_files = glob.glob(directory + '/*.ant')

for i, each in enumerate(model_files):
    try:
        print(i, each)
        model = te.loadAntimonyModel(each)
        nfs = len(model.getFloatingSpeciesIds())
        nbs = len(model.getBoundarySpeciesIds())
        each0 = each.split('\\')[1].split('_')[0]

        print(i, each0, nbs, nfs, nfs + nbs, model.getNumReactions())
    except:
        print(i, 'failed')
