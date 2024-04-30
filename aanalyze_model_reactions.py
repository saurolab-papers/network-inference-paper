
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
        # each0 = each.split('\\')[1].split('_')[0]
        each1 = each.split('\\')[1].split('.')[0]
        # print(each0)
        # print(each1)

        # print('F', model.getFloatingSpeciesIds())
        # print('B', model.getBoundarySpeciesIds())
        species = model.getFloatingSpeciesIds() + model.getBoundarySpeciesIds()
        s_out = [0 for _ in species]
        s_in = [0 for _ in species]
        # print('S', species)
        # print()
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
                    # print()
                    # print(name)
                    # print(rxn)
                    # print(kin)

                    reactants = deepcopy(rxn)
                    reactants = reactants.replace('=>', '->')
                    reactants = reactants.split(' -> ')[0].split(' + ')
                    reactants_order = 0
                    # print(reactants)
                    for react in reactants:
                        # print('REACT', react)
                        react2 = react.split()
                        # print('R2', react2)
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
                        # print('PROD', prod)
                        prod2 = prod.split()
                        # print('P2', prod2)
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
                    # quit()
                    # print('reactants', reactants_order, reactants)
                    # print('products', products_order, products)
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
                    # print(kin_split)

                if 'Reactions:' in line:
                    rxns = True
                    # print()
                    # print(line[:-1])
        # print()
        # print(each.split('\\')[1].split('.')[0], sig_orders)
        # print(s_out)
        # print(s_in)

        out_set = set(s_out)
        # print(out_set)
        out_list = list(out_set)
        # print(out_list)
        out_list_dist = [0 for _ in out_list]
        for item in s_out:
            out_list_dist[out_list.index(item)] += 1
        # print(out_list, out_list_dist)
        out_dict = dict()
        for j, item in enumerate(out_list):
            out_dict[item] = out_list_dist[j]
            out_list_dist[j] = str(out_list[j]) + ':' + str(out_list_dist[j])
        # print('out_50_50', sorted(out_list_dist))
        # print('out_50_50', out_dict)
        # print(each.split('\\')[1].split('.')[0], out_dict)

        in_set = set(s_in)
        # print(in_set)
        in_list = list(in_set)
        # print(in_list)
        in_list_dist = [0 for _ in in_list]
        for item in s_in:
            in_list_dist[in_list.index(item)] += 1
        # print(in_list, in_list_dist)
        in_dict = dict()
        for j, item in enumerate(in_list):
            in_dict[item] = in_list_dist[j]
            in_list_dist[j] = str(in_list[j]) + ':' + str(in_list_dist[j])
        # print('in', sorted(in_list_dist))
        # print('in', in_dict)
        print(each.split('\\')[1].split('.')[0], in_dict)

        # print(each1, nbs, nfs, nfs + nbs, model.getNumReactions())
        # quit()
    except:
        print(each.split('\\')[1].split('.')[0], 'failed')
