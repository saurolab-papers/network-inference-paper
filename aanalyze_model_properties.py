
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
        # print()
        # print(i, each)
        model = te.loadAntimonyModel(each)
        # odes = te.getODEsFromModel(model)
        # odes = odes.splitlines()
        # print(len(odes))
        # for item in odes:
        #     print(item)
        nfs = len(model.getFloatingSpeciesIds())
        nbs = len(model.getBoundarySpeciesIds())
        # print('number of floating:  ', nfs)
        # print('number of boundary:  ', nbs)
        # print('number of species:   ', nfs + nbs)
        # print('number of reactions: ', model.getNumReactions())
        each0 = each.split('\\')[1].split('.')[0]
        # each1 = each.split('\\')[1].split('_')[1].split('.')[0]

        # rxns = False
        # with open(each, 'r') as model_file:
        #     lines = model_file.readlines()
        #     for line in lines:
        #         if line.strip() == '':
        #             rxns = False
        #         if rxns:
        #             print(line.split(':')[1].split(';')[0])
        #         if 'Reactions:' in line:
        #             rxns = True
        #             print(line[:-1])

        print(i, each0, nbs, nfs, nfs + nbs, model.getNumReactions())
    except:
        print(i, each.split('\\')[1].split('.')[0], 'failed')
