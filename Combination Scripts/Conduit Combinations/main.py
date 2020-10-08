import networkx as nx
from itertools import combinations
import csv
#----------------------------------------------------------------------------
#Hit run at the top of the page. Follow on-screen instructions bottom right
#Output will be found in output.simc on the left after program has finished
#----------------------------------------------------------------------------
#For any class conversions simply change values in the spec, finesse
#potency and endurance lists
#----------------------------------------------------------------------------
#spec lookup dict
specs = {'1': 'arcane', '2': 'fire', '3': 'frost'}
#covenant lookup dict
covenants = {'1': 'kyrian', '2': 'night_fae', '3': 'necrolord', '4': 'venthyr'}
#kyrian soulbind lookup dict
kyrianSoulbinds = {
    '1': 'Pelagos',
    '2': 'Kleia',
    '3': 'Forgelite Prime Mikanikos'
}
#kyrian soulbind lookup dict
faeSoulbinds = {'1': 'Niya', '2': 'Dreamweaver', '3': 'Korayn'}
#kyrian soulbind lookup dict
necroSoulbinds = {
    '1': 'Plague Deviser Marileth',
    '2': 'Emeni',
    '3': 'Bonesmith Heirmir'
}
#kyrian soulbind lookup dict
venthyrSoulbinds = {
    '1': 'Nadjia the Mistblade',
    '2': 'Theotar the Mad Duke',
    '3': 'General Draven'
}
#dps relevant conduits - id|category (0 generic, 1 arcane, 2 fire, 3 frost, 4 kyrian, 5 nf, 6 necro, 7 ven) tuples
finesse = [['29', '0']]  #grounding surge
potency = [
    ['40', '4'],  #ire of the ascended
    ['43', '7'],  #siphoned malice
    ['39', '6'],  #gift of the lich
    ['38', '5'],  #discipline of the grove
    ['34', '1'],  #arcane prodigy
    ['55', '1'],  #artifice of the archmage
    ['51', '1'],  #magi's brand
    ['36', '1'],  #nether precision
    ['249', '2'],  #controlled destruction
    ['53', '2'],  #flame accretion
    ['32', '2'],  #master flame
    ['30', '2'],  #infernal cascade
    ['18', '3'],  #shivering core
    ['17', '3'],  #unrelenting cold
    ['20', '3'],  #icy propulsion
    ['21', '3'],  #ice bite
]
endurance = [['', '0']]  #dummy to just make dealing with it later easier


def countConduits(path):
    potencyCount = 0
    finesseCount = 0
    enduranceCount = 0
    for value in path:
        if 'potency' in value:
            potencyCount += 1
        elif 'finesse' in value:
            finesseCount += 1
        elif 'endurance' in value:
            enduranceCount += 1
    return [potencyCount, finesseCount, enduranceCount]


def conduitCombinatorics(condCount, conduitArray):
    if condCount[0] > len(conduitArray[0]):
        condCount[0] = len(conduitArray[0])
    if condCount[1] > len(conduitArray[1]):
        condCount[1] = len(conduitArray[1])
    if condCount[2] > len(conduitArray[2]):
        condCount[2] = len(conduitArray[2])
    return combinations(conduitArray[0], condCount[0]), combinations(
        conduitArray[1], condCount[1]), combinations(conduitArray[2],
                                                     condCount[2])


def filterConduitArray(conduitArray, covenant, spec):
    numbersToRemove = []
    if covenant == covenants['1']:  #remove 5/6/7
        numbersToRemove.extend(['5', '6', '7'])
    elif covenant == covenants['2']:  #remove 4/6/7
        numbersToRemove.extend(['4', '6', '7'])
    elif covenant == covenants['3']:  #remove 4/5/7
        numbersToRemove.extend(['4', '5', '7'])
    elif covenant == covenants['4']:  #remove 4/5/6
        numbersToRemove.extend(['4', '5', '6'])
    if spec == specs['1']:  #remove 2/3
        numbersToRemove.extend(['2', '3'])
    elif spec == specs['2']:  #remove 1/3
        numbersToRemove.extend(['1', '3'])
    elif spec == specs['3']:  #remove 1/2
        numbersToRemove.extend(['1', '2'])
    for value in potency[:]:
        if value[1] in numbersToRemove:
            potency.remove(value)
    for value in finesse[:]:
        if value[1] in numbersToRemove:
            finesse.remove(value)
    for value in endurance[:]:
        if value[1] in numbersToRemove:
            endurance.remove(value)
    [r.pop(1) for r in potency]
    [r.pop(1) for r in finesse]
    [r.pop(1) for r in endurance]


def replaceConduitText(path):
    tempPath = []
    for node in path:
        if 'endurance' not in node and 'finesse' not in node and 'potency' not in node:
            tempPath.append(node)
    return tempPath


def flattenList(l):
    return [item for sublist in l for item in sublist]

def replaceNames(nameString):
  with open("lookup.txt", mode='r') as csvLookup:
    csvReader = csv.reader(csvLookup)
    for row in csvReader:
      if int(row[0]) >=  1000: #soulbind IDs should be safe enough to not occur as substr 
        nameString = nameString.replace(row[0], row[1])
      else: #conduit IDs could be substr so check we have a rank delim (:) as well
        nameString = nameString.replace(row[0]+":", row[1]+":")
  return nameString

def getUserInputs():
    print('Please enter number for spec:')
    for spec in specs:
        print(spec, specs[spec])
    selection = input()
    spec = specs.get(selection, None)
    if spec == None:
        print('Invalid spec selected.')
        quit()
    print('Please enter number for covenant:')
    for covenant in covenants:
        print(covenant, covenants[covenant])
    selection = input()
    covenant = covenants.get(selection, None)
    if covenant == covenants['1']:
        print('Please enter number for soulbind:')
        for soulbind in kyrianSoulbinds:
            print(soulbind, kyrianSoulbinds[soulbind])
        selection = input()
        soulbind = kyrianSoulbinds.get(selection, None)
        if soulbind == None:
            print('Invalid soulbind selected.')
            quit()
    elif covenant == covenants['2']:
        print('Please enter number for soulbind:')
        for soulbind in faeSoulbinds:
            print(soulbind, faeSoulbinds[soulbind])
        selection = input()
        soulbind = faeSoulbinds.get(selection, None)
        if soulbind == None:
            print('Invalid soulbind selected.')
            quit()
    elif covenant == covenants['3']:
        print('Please enter number for soulbind:')
        for soulbind in necroSoulbinds:
            print(soulbind, necroSoulbinds[soulbind])
        selection = input()
        soulbind = necroSoulbinds.get(selection, None)
        if soulbind == None:
            print('Invalid soulbind selected.')
            quit()
    elif covenant == covenants['4']:
        print('Please enter number for soulbind:')
        for soulbind in venthyrSoulbinds:
            print(soulbind, venthyrSoulbinds[soulbind])
        selection = input()
        soulbind = venthyrSoulbinds.get(selection, None)
        if soulbind == None:
            print('Invalid soulbind selected.')
            quit()
    else:
        print('Invalid covenant selected.')
        quit()
    rank = input('Please enter desired conduit rank [1-15]\n')
    if int(rank) < 1 or int(rank) > 15:
        print('Invalid rank selected.')
        quit()
    return spec, covenant, soulbind, rank


def buildGraph(soulbind):
    soulbindGraph = nx.DiGraph()
    if soulbind == kyrianSoulbinds['1']: #Pelagos
        soulbindGraph.add_edges_from([('328257', 'endurance1'),
                                      ('328257', 'finesse1'),
                                      ('endurance1', 'potency1'),
                                      ('finesse1', 'potency1'),
                                      ('potency1', '329777'),
                                      ('potency1', '329786'),
                                      ('potency1', '328261'),
                                      ('329777', 'finesse2'),
                                      ('329786', 'endurance2'),
                                      ('328261', 'potency2'),
                                      ('finesse2', 'endurance3'),
                                      ('endurance2', 'endurance3'),
                                      ('potency2', 'endurance3'),
                                      ('endurance3', '328265'),
                                      ('endurance3', '328263'),
                                      ('328265', '328266'),
                                      ('328263', '328266')])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '328257', '328266', cutoff=None))
    elif soulbind == kyrianSoulbinds['2']: # Kleia 
        soulbindGraph.add_edges_from([('329776', 'endurance1'),
                                      ('334066', 'potency1'),
                                      ('endurance1', 'finesse1'),
                                      ('potency1', 'finesse1'),
                                      ('finesse1', '329781'),
                                      ('finesse1', '329779'),
                                      ('finesse1', '329778'),
                                      ('329781', 'potency2'),
                                      ('329779', 'endurance2'),
                                      ('329778', 'finesse2'),
                                      ('potency2', 'endurance3'),
                                      ('finesse2', 'endurance3'),
                                      ('endurance2', 'endurance3'),
                                      ('endurance3', '329784'),
                                      ('endurance3', '328258'),
                                      ('329784', '329791'), ('328258',
                                                             '329791')])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '329776', '329791', cutoff=None))
        paths += list(
            nx.all_simple_paths(
                soulbindGraph, '334066', '329791', cutoff=None))
    elif soulbind == kyrianSoulbinds['3']: #Forgelite
        soulbindGraph.add_edges_from([('331610', 'endurance1'),
                                      ('331609', 'potency1'),
                                      ('endurance1', 'finesse1'),
                                      ('potency1', 'finesse1'),
                                      ('finesse1', '333935'),
                                      ('finesse1', '331612'),
                                      ('finesse1', '331611'),
                                      ('333935', 'endurance2'),
                                      ('331612', 'finesse2'),
                                      ('331611', 'potency2'),
                                      ('endurance2', 'endurance3'),
                                      ('finesse2', 'endurance3'),
                                      ('potency2', 'endurance3'),
                                      ('endurance3', '331726'),
                                      ('endurance3', '331725'),
                                      ('331726', '333950'), ('331725',
                                                             '333950')])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '331610', '333950', cutoff=None))
        paths += list(
            nx.all_simple_paths(
                soulbindGraph, '331609', '333950', cutoff=None))
    elif soulbind == faeSoulbinds['1']: #Niya
        soulbindGraph.add_edges_from([('342270', 'potency1'),
                                      ('320658', 'endurance1'),
                                      ('potency1', 'finesse1'),
                                      ('endurance1', 'finesse1'),
                                      ('finesse1', '320659'),
                                      ('finesse1', '320660'),
                                      ('finesse1', '320662'),
                                      ('320659', 'endurance2'),
                                      ('320660', 'potency2'),
                                      ('320662', 'finesse2'),
                                      ('endurance2', 'endurance3'),
                                      ('potency2', 'endurance3'),
                                      ('finesse2', 'endurance3'),
                                      ('endurance3', '320668'),
                                      ('endurance3', '320687'),
                                      ('320668', '322721'), ('320687',
                                                             '322721')])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '342270', '322721', cutoff=None))
        paths += list(
            nx.all_simple_paths(
                soulbindGraph, '320658', '322721', cutoff=None))
    elif soulbind == faeSoulbinds['2']: #Dream
        soulbindGraph.add_edges_from([('319191', 'finesse1'),
                                      ('319191', 'endurance1'),
                                      ('finesse1', 'potency1'),
                                      ('endurance1', 'potency1'),
                                      ('potency1', '319210'),
                                      ('potency1', '319211'),
                                      ('potency1', '319213'),
                                      ('319210', 'endurance2'),
                                      ('319211', 'potency2'),
                                      ('319213', 'finesse2'),
                                      ('endurance2', 'endurance3'),
                                      ('potency2', 'endurance3'),
                                      ('finesse2', 'endurance3'),
                                      ('endurance3', '319214'),
                                      ('endurance3', '319216'),
                                      ('319214', '319217'), ('319216',
                                                             '319217')])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '319191', '319217', cutoff=None))
    elif soulbind == faeSoulbinds['3']: #Korayn
        soulbindGraph.add_edges_from([('325067', 'potency1'),
                                      ('325065', 'finesse1'),
                                      ('potency1', 'endurance1'),
                                      ('finesse1', 'endurance1'),
                                      ('endurance1', '325068'),
                                      ('endurance1', '325069'),
                                      ('endurance1', '325601'),
                                      ('325068', 'potency2'),
                                      ('325069', 'endurance2'),
                                      ('325601', 'finesse2'),
                                      ('potency2', 'endurance3'),
                                      ('endurance2', 'endurance3'),
                                      ('finesse2', 'endurance3'),
                                      ('endurance3', '325072'),
                                      ('endurance3', '325073'),
                                      ('325072', '325066'), ('325073',
                                                             '325066')])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '325067', '325066', cutoff=None))
        paths += list(
            nx.all_simple_paths(
                soulbindGraph, '325065', '325066', cutoff=None))
    elif soulbind == necroSoulbinds['1']: #Marileth
        soulbindGraph.add_edges_from([('323074', 'endurance1'),
                                      ('323074', 'finesse1'),
                                      ('endurance1', 'potency1'),
                                      ('finesse1', 'potency1'),
                                      ('potency1', '323089'),
                                      ('potency1', '323091'),
                                      ('potency1', '323090'),
                                      ('323089', 'endurance2'),
                                      ('323091', 'potency2'),
                                      ('323090', 'finesse2'),
                                      ('endurance2', 'endurance3'),
                                      ('potency2', 'endurance3'),
                                      ('finesse2', 'endurance3'),
                                      ('endurance3', '323079'),
                                      ('endurance3', '323081'),
                                      ('323079', '323095'),
                                      ('323081', '323095')])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '323074', '323095', cutoff=None))
    elif soulbind == necroSoulbinds['2']: #Emeni
        soulbindGraph.add_edges_from([('323921', 'potency1'),
                                      ('341650', 'endurance1'),
                                      ('potency1', 'finesse1'),
                                      ('endurance1', 'finesse1'),
                                      ('finesse1', '323918'),
                                      ('finesse1', '323919'),
                                      ('finesse1', '323916'),
                                      ('323918', 'potency2'),
                                      ('323919', 'endurance2'),
                                      ('323916', 'finesse2'),
                                      ('potency2', 'endurance3'),
                                      ('endurance2', 'endurance3'),
                                      ('finesse2', 'endurance3'),
                                      ('endurance3', '324440'),
                                      ('endurance3', '324441'),
                                      ('324440', '342156'),
                                      ('324441', '342156')])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '323921', '342156', cutoff=None))
        paths += list(
            nx.all_simple_paths(
                soulbindGraph, '341650', '342156', cutoff=None))
    elif soulbind == necroSoulbinds['3']: #Heirmir
        soulbindGraph.add_edges_from([('326504', 'endurance1'),
                                      ('326507', 'potency1'),
                                      ('endurance1', 'finesse1'),
                                      ('potency1', 'finesse1'),
                                      ('finesse1', '326509'),
                                      ('finesse1', '326511'),
                                      ('finesse1', '326572'),
                                      ('326509', 'finesse2'),
                                      ('326511', 'potency2'),
                                      ('326572', 'endurance2'),
                                      ('finesse2', 'endurance3'),
                                      ('potency2', 'endurance3'),
                                      ('endurance2', 'endurance3'),
                                      ('endurance3', '326512'),
                                      ('endurance3', '326513'),
                                      ('326512', '326514'), ('326513',
                                                             '326514')])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '326504', '326514', cutoff=None))
        paths += list(
            nx.all_simple_paths(
                soulbindGraph, '326507', '326514', cutoff=None))
    elif soulbind == venthyrSoulbinds['1']: #Nadjia
        soulbindGraph.add_edges_from([('331576', 'potency1'),
                                      ('331577', 'endurance1'),
                                      ('potency1', 'finesse1'),
                                      ('endurance1', 'finesse1'),
                                      ('finesse1', '331579'),
                                      ('331579', 'endurance2'),
                                      ('331579', 'potency2'),
                                      ('331579', 'finesse2'),
                                      ('endurance2', '331580'),
                                      ('potency2', '331582'),
                                      ('finesse2', '331584'),
                                      ('331580', 'endurance3'),
                                      ('331582', 'endurance3'),
                                      ('331584', 'endurance3'),
                                      ('endurance3', '331586')])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '331576', '331586', cutoff=None))
        paths += list(
            nx.all_simple_paths(
                soulbindGraph, '331577', '331586', cutoff=None))
    elif soulbind == venthyrSoulbinds['2']: #Theotar
        soulbindGraph.add_edges_from([('336140', 'endurance1'),
                                      ('336147', 'finesse1'),
                                      ('endurance1', 'potency1'),
                                      ('finesse1', 'potency1'),
                                      ('potency1', '336243'),
                                      ('potency1', '336239'),
                                      ('potency1', '336245'),
                                      ('336243', 'endurance2'),
                                      ('336239', 'finesse2'),
                                      ('336245', 'potency2'),
                                      ('endurance2', 'endurance3'),
                                      ('finesse2', 'endurance3'),
                                      ('potency2', 'endurance3'),
                                      ('endurance3', '336247'),
                                      ('endurance3', '336184'),
                                      ('336247', '319983'), ('336184',
                                                             '319983')])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '336140', '319983', cutoff=None))
        paths += list(
            nx.all_simple_paths(
                soulbindGraph, '336147', '319983', cutoff=None))
    elif soulbind == venthyrSoulbinds['3']: #Draven
        soulbindGraph.add_edges_from([('332755', 'endurance1'),
                                      ('332756', 'endurance1'),
                                      ('endurance1', '319973'),
                                      ('endurance1', '332753'),
                                      ('endurance1', '332754'),
                                      ('319973', 'finesse1'),
                                      ('332753', 'endurance2'),
                                      ('332754', 'potency1'),
                                      ('finesse1', 'potency2'),
                                      ('endurance2', 'potency2'),
                                      ('potency1', 'potency2'),
                                      ('potency2', '319978'),
                                      ('potency2', '319982'),
                                      ('319978', 'finesse2'),
                                      ('319982', 'endurance3'),
                                      ('finesse2', '340159'),
                                      ('endurance3', '340159')])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '332755', '340159', cutoff=None))
        paths += list(
            nx.all_simple_paths(
                soulbindGraph, '332756', '340159', cutoff=None))
    return soulbindGraph, paths


def main():
    spec, covenant, soulbind, rank = getUserInputs()
    print('Generating Profiles')
    profile = ""
    with open('output.simc', 'w') as outputfile:
        outputfile.write(
            "#Replace this with your desired base profile /simc etc \n\ncovenant="
            + covenant + "\n")
        filterConduitArray([potency, finesse, endurance], covenant, spec)
        soulbindGraph, paths = buildGraph(soulbind)
        for path in paths:
            conduitCount = countConduits(path)
            newPath = replaceConduitText(path)
            potencyCombos, finesseCombos, enduranceCombos = conduitCombinatorics(
                conduitCount, [
                    flattenList(potency),
                    flattenList(finesse),
                    flattenList(endurance)
                ])
            potencyComboList = []
            finesseComboList = []
            enduranceComboList = []
            profile = ''
            for node in newPath:
                profile += node + "/"
            for potencyCombo in potencyCombos:
                potencyComboList.append(potencyCombo)
            for finesseCombo in finesseCombos:
                finesseComboList.append(finesseCombo)
            for enduranceCombo in enduranceCombos:
                enduranceComboList.append(enduranceCombo)
            for potCondTuple in potencyComboList:
                for finCondTuple in finesseComboList:
                    for endCondTuple in enduranceComboList:
                        profileToPrint = profile
                        for potCond in potCondTuple:
                            if (potCond != ''):
                                profileToPrint += potCond + ":" + rank + "/"
                        for finCond in finCondTuple:
                            if (finCond != ''):
                                profileToPrint += finCond + ":" + rank + "/"
                        for endCond in endCondTuple:
                            if (endCond != ''):
                                profileToPrint += endCond + ":" + rank + "/"
                        if (profileToPrint[-1] == '/'):
                            profileToPrint = profileToPrint[:-1]
                        nameToPrint = replaceNames(profileToPrint)
                        outputfile.write('profileset."' + nameToPrint +
                                         '"+=soulbind=')
                        outputfile.write(profileToPrint + '\n')
    print('Finished. Please find output in output file.')


if __name__ == "__main__":
    main()
