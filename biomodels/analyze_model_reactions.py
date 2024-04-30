
import tellurium as te
import antimony
from os import listdir
from os.path import isfile, join
import glob
from copy import deepcopy
import re

directory = 'ant_files'

model_files = glob.glob(directory + '/*.ant')

for i, each in enumerate(model_files):
    try:
        model = te.loadAntimonyModel(each)
        nfs = len(model.getFloatingSpeciesIds())
        nbs = len(model.getBoundarySpeciesIds())
        each1 = each.split('\\')[1].split('.')[0]

        species = model.getFloatingSpeciesIds() + model.getBoundarySpeciesIds()
        s_out = [0 for _ in species]
        s_in = [0 for _ in species]
        rxns = False
        orders = [0, 0, 0, 0, 0, 0, 0]
        with open(each, 'r') as model_file:
            lines = model_file.readlines()
            for line in lines:
                if line.strip() == '':
                    rxns = False
                if rxns:
                    name = line.split(':')[0]
                    rxn = line.split(':')[1].split(';')[0]
                    kin = line.split(':')[1].split(';')[1]

                    reactants = deepcopy(rxn)
                    reactants = reactants.replace('=>', '->')
                    reactants = reactants.split(' -> ')[0].split(' + ')
                    reactants_order = 0
                    for react in reactants:
                        react2 = react.split()
                        if len(react2) > 1:
                            reactants_order += float(react2[0])
                            react2[1] = react2[1].replace('$', '')
                            s_out[species.index(react2[1])] += float(react2[0])
                        else:
                            react = react.strip()
                            if len(react) > 0:
                                reactants_order += 1
                                react2[0] = react2[0].replace('$', '')
                                s_out[species.index(react2[0])] += 1

                    products = deepcopy(rxn)
                    products = products.replace('=>', '->')
                    products = products.split(' -> ')[1].split(' + ')
                    products_order = 0
                    for prod in products:
                        prod2 = prod.split()
                        if len(prod2) > 1:
                            products_order += float(prod2[0])
                            prod2[1] = prod2[1].replace('$', '')
                            s_in[species.index(prod2[1])] += float(prod2[0])
                        else:
                            prod = prod.strip()
                            if len(prod) > 0:
                                products_order += 1
                                prod2[0] = prod2[0].replace('$', '')
                                s_in[species.index(prod2[0])] += 1
                                
                    if reactants_order == 0 and products_order == 1:
                        orders[0] += 1
                    elif reactants_order == 1 and products_order == 0:
                        orders[1] += 1
                    elif reactants_order == 1 and products_order == 1:
                        orders[2] += 1
                    elif reactants_order == 2 and products_order == 1:
                        orders[3] += 1
                    elif reactants_order == 1 and products_order == 2:
                        orders[4] += 1
                    elif reactants_order == 2 and products_order == 2:
                        orders[5] += 1
                    else:
                        orders[6] += 1

                    kin = kin.replace(' - ', '*')
                    kin = kin.replace(' + ', '*')
                    kin = kin.replace('(', '*')
                    kin = kin.replace(')', '*')
                    kin = kin.replace('/', '*')
                    kin = kin.replace('^', '*')
                    kin_split = kin.split('*')

                if 'Reactions:' in line:
                    rxns = True

        out_set = set(s_out)
        out_list = list(out_set)
        out_list_dist = [0 for _ in out_list]
        for item in s_out:
            out_list_dist[out_list.index(item)] += 1
        out_dict = dict()
        for j, item in enumerate(out_list):
            out_dict[item] = out_list_dist[j]
            out_list_dist[j] = str(out_list[j]) + ':' + str(out_list_dist[j])

        in_set = set(s_in)
        in_list = list(in_set)
        in_list_dist = [0 for _ in in_list]
        for item in s_in:
            in_list_dist[in_list.index(item)] += 1
        in_dict = dict()
        for j, item in enumerate(in_list):
            in_dict[item] = in_list_dist[j]
            in_list_dist[j] = str(in_list[j]) + ':' + str(in_list_dist[j])
        print(each, in_dict, out_dict)

    except:
        print(i, 'failed')
