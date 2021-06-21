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
    rank = input('Please enter desired conduit rank [1-15]. Empowered Slots are +2 levels.\n')
    if int(rank) < 1 or int(rank) > 15:
        print('Invalid rank selected.')
        quit()
    return spec, covenant, soulbind, rank


def buildGraph(soulbind):
    soulbindGraph = nx.DiGraph()
    if soulbind == kyrianSoulbinds['1']: #Pelagos
        soulbindGraph.add_edges_from([
            ('328266', 'potency1'),
            ('328266', 'endurance1'),
            ('328266', 'finesse1'),
            ('potency1', '328261'),
            ('endurance1', '329786'),
            ('finesse1', '329777'),
            ('328261', 'endurance2'),
            ('329786', 'endurance2'),
            ('329777', 'endurance2'),
            ('endurance2', '328265'),
            ('endurance2', '328263'),
            ('328265', 'potency2'),
            ('328263', 'potency2'),
            ('potency2', 'endurance3'),
            ('potency2', 'finesse2'),
            ('endurance3', '328257'),
            ('finesse2', '328257'),
            ('328257', 'potency3'),
            ('potency3', '351146'),
            ('potency3', '351147'),
            ('351146', 'endurance4'),
            ('351147', 'finesse3'),
            ('endurance4', '351149'),
            ('finesse3', '351149'),
        ])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '328266', '351149', cutoff=None))
    elif soulbind == kyrianSoulbinds['2']: # Kleia 
        soulbindGraph.add_edges_from([
            ('329791', 'potency1'),
            ('329791', 'endurance1'),
            ('potency1', '334066'),
            ('endurance1', '329776'),
            ('334066', 'finesse1'),
            ('329776', 'finesse1'),
            ('finesse1', '329784'),
            ('finesse1', '328258'),
            ('329784', 'endurance2'),
            ('328258', 'endurance2'),
            ('endurance2', 'potency2'),
            ('endurance2', 'endurance3'),
            ('endurance2', 'finesse2'),
            ('potency2', '329779'),
            ('endurance3', '329778'),
            ('finesse2', '329781'),
            ('329779', 'potency3'),
            ('329778', 'potency3'),
            ('329781', 'potency3'),
            ('potency3', '351488'),
            ('potency3', '351489'),
            ('351488', 'endurance4'),
            ('351489', 'finesse3'),
            ('endurance4', '351491'),
            ('finesse3', '351491'),
        ])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '329791', '351491', cutoff=None))
    elif soulbind == kyrianSoulbinds['3']: #Forgelite
        soulbindGraph.add_edges_from([
            ('333950', 'potency1'),
            ('333950', 'endurance1'),
            ('potency1', '331609'),
            ('endurance1', '331610'),
            ('331609', 'finesse1'),
            ('331610', 'finesse1'),
            ('finesse1', '331726'),
            ('finesse1', '331725'),
            ('331726', 'endurance2'),
            ('331725', 'endurance2'),
            ('endurance2', 'potency2'),
            ('endurance2', 'endurance3'),
            ('endurance2', 'finesse2'),
            ('potency2', '331611'),
            ('endurance3', '333935'),
            ('finesse2', '331612'),
            ('331611', 'potency3'),
            ('333935', 'potency3'),
            ('331612', 'potency3'),
            ('potency3', '352186'),
            ('potency3', '352187'),
            ('352186', 'endurance4'),
            ('352187', 'finesse3'),
            ('endurance4', '352188'),
            ('finesse3', '352188'),
        ])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '333950', '352188', cutoff=None))
    elif soulbind == faeSoulbinds['1']: #Niya
        soulbindGraph.add_edges_from([
            ('322721', 'potency1'),
            ('322721', 'endurance1'),
            ('potency1', '342270'),
            ('endurance1', '320658'),
            ('342270', 'finesse1'),
            ('320658', 'finesse1'),
            ('finesse1', '320668'),
            ('finesse1', '320687'),
            ('320668', 'endurance2'),
            ('320687', 'endurance2'),
            ('endurance2', 'endurance3'),
            ('endurance2', 'potency2'),
            ('endurance2', 'finesse2'),
            ('endurance3', '320659'),
            ('potency2', '320660'),
            ('finesse2', '320662'),
            ('320659', 'potency3'),
            ('320660', 'potency3'),
            ('320662', 'potency3'),
            ('potency3', '352501'),
            ('potency3', '352502'),
            ('352501', 'endurance4'),
            ('352502', 'finesse3'),
            ('endurance4', '352503'),
            ('finesse3', '352503'),
        ])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '322721', '352503', cutoff=None))
    elif soulbind == faeSoulbinds['2']: #Dream
        soulbindGraph.add_edges_from([
            ('319217','endurance1'),
            ('319217','finesse1'),
            ('endurance1','potency1'),
            ('finesse1','potency1'),
            ('potency1','319211'),
            ('potency1','319210'),
            ('potency1','319213'),
            ('319211','potency2'),
            ('319210','endurance2'),
            ('319213','finesse2'),
            ('potency2','endurance3'),
            ('endurance2','endurance3'),
            ('finesse2','endurance3'),
            ('endurance3','319214'),
            ('endurance3','319216'),
            ('319214','319191'),
            ('319216','319191'),
            ('319191','potency3'),
            ('potency3','352782'),
            ('potency3','352779'),
            ('352782','endurance4'),
            ('352779','finesse3'),
            ('endurance4','352786'),
            ('finesse3','352786'),
        ])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '319217', '352786', cutoff=None))
    elif soulbind == faeSoulbinds['3']: #Korayn
        soulbindGraph.add_edges_from([
            ('325066', 'potency1'),
            ('325066', 'endurance1'),
            ('potency1', '325067'),
            ('endurance1', '325065'),
            ('325067', 'finesse1'),
            ('325065', 'finesse1'),
            ('finesse1', '325072'),
            ('finesse1', '325073'),
            ('325072', 'endurance2'),
            ('325073', 'endurance2'),
            ('endurance2', 'potency2'),
            ('endurance2', 'endurance3'),
            ('endurance2', 'finesse2'),
            ('potency2', '325068'),
            ('endurance3', '325069'),
            ('finesse2', '325601'),
            ('325068', 'potency3'),
            ('325069', 'potency3'),
            ('325601', 'potency3'),
            ('potency3', '352800'),
            ('potency3', '352806'),
            ('352800', 'endurance4'),
            ('352806', 'finesse3'),
            ('endurance4', '352805'),
            ('finesse3', '352805'),
        ])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '325066', '352805', cutoff=None))
    elif soulbind == necroSoulbinds['1']: #Marileth
        soulbindGraph.add_edges_from([
            ('323074','potency1'),
            ('323074','endurance1'),
            ('323074','finesse1'),
            ('potency1','323091'),
            ('endurance1','323089'),
            ('finesse1','323090'),
            ('323091','endurance2'),
            ('323089','endurance2'),
            ('323090','endurance2'),
            ('endurance2','323079'),
            ('endurance2','323081'),
            ('323079','potency2'),
            ('323081','potency2'),
            ('potency2','endurance3'),
            ('potency2','finesse2'),
            ('endurance3','323095'),
            ('finesse2','323095'),
            ('323095','potency3'),
            ('potency3','352108'),
            ('potency3','352109'),
            ('352108','endurance4'),
            ('352109','finesse3'),
            ('endurance4','352110'),
            ('finesse3','352110'),
        ])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '323074', '352110', cutoff=None))
    elif soulbind == necroSoulbinds['2']: #Emeni
        soulbindGraph.add_edges_from([
            ('342156', 'potency1'),
            ('342156', 'endurance1'),
            ('potency1', '323921'),
            ('endurance1', '341650'),
            ('323921', 'finesse1'),
            ('341650', 'finesse1'),
            ('finesse1', '324440'),
            ('finesse1', '324441'),
            ('324440', 'endurance2'),
            ('324441', 'endurance2'),
            ('endurance2', 'potency2'),
            ('endurance2', 'endurance3'),
            ('endurance2', 'finesse2'),
            ('potency2', '323918'),
            ('endurance3', '323919'),
            ('finesse2', '323916'),
            ('323918', 'potency3'),
            ('323919', 'potency3'),
            ('323916', 'potency3'),
            ('potency3', '351089'),
            ('potency3', '351093'),
            ('351089', 'endurance4'),
            ('351093', 'finesse3'),
            ('endurance4', '351094'),
            ('finesse3', '351094'),
        ])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '342156', '351094', cutoff=None))
    elif soulbind == necroSoulbinds['3']: #Heirmir
        soulbindGraph.add_edges_from([
            ('326514', 'potency1'),
            ('326514', 'endurance1'),
            ('potency1', '326507'),
            ('endurance1', '326504'),
            ('326507', 'finesse1'),
            ('326504', 'finesse1'),
            ('finesse1', '326512'),
            ('finesse1', '326513'),
            ('326512', 'endurance2'),
            ('326513', 'endurance2'),
            ('endurance2', 'potency2'),
            ('endurance2', 'endurance3'),
            ('endurance2', 'finesse2'),
            ('potency2', '326511'),
            ('endurance3', '326572'),
            ('finesse2', '326509'),
            ('326511', 'potency3'),
            ('326572', 'potency3'),
            ('326509', 'potency3'),
            ('potency3', '350899'),
            ('potency3', '350935'),
            ('350899', 'endurance4'),
            ('350935', 'finesse3'),
            ('endurance4', '350936'),
            ('finesse3', '350936'),
        ])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '326514', '350936', cutoff=None))
    elif soulbind == venthyrSoulbinds['1']: #Nadjia
        soulbindGraph.add_edges_from([
            ('331586', 'potency1'),
            ('331586', 'endurance1'),
            ('potency1', '331576'),
            ('endurance1', '331577'),
            ('331576', 'finesse1'),
            ('331577', 'finesse1'),
            ('finesse1', '331579'),
            ('331579', 'endurance2'),
            ('endurance2', 'potency2'),
            ('endurance2', 'endurance3'),
            ('endurance2', 'finesse2'),
            ('potency2', '331582'),
            ('endurance3', '331580'),
            ('finesse2', '331584'),
            ('331582', 'potency3'),
            ('331580', 'potency3'),
            ('331584', 'potency3'),
            ('potency3', '352405'),
            ('potency3', '352366'),
            ('352405', 'finesse3'),
            ('352366', 'endurance4'),
            ('finesse3', '352373'),
            ('endurance4', '352373'),
        ])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '331586', '352373', cutoff=None))
    elif soulbind == venthyrSoulbinds['2']: #Theotar
        soulbindGraph.add_edges_from([
            ('336239', 'endurance1'),
            ('336239', 'finesse1'),
            ('endurance1', '336140'),
            ('finesse1', '336147'),
            ('336140', 'potency1'),
            ('336147', 'potency1'),
            ('potency1', '336247'),
            ('potency1', '336184'),
            ('336247', 'endurance2'),
            ('336184', 'endurance2'),
            ('endurance2', 'potency2'),
            ('endurance2', 'endurance3'),
            ('endurance2', 'finesse2'),
            ('potency2', '336245'),
            ('endurance3', '336243'),
            ('finesse2', '319983'),
            ('336245', 'potency3'),
            ('336243', 'potency3'),
            ('319983', 'potency3'),
            ('potency3', '351747'),
            ('potency3', '351748'),
            ('351747', 'finesse3'),
            ('351748', 'endurance4'),
            ('finesse3', '351750'),
            ('endurance4', '351750'),
        ])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '336239', '351750', cutoff=None))
    elif soulbind == venthyrSoulbinds['3']: #Draven
        soulbindGraph.add_edges_from([
            ('340159', 'endurance1'),
            ('340159', 'finesse1'),
            ('endurance1', '319982'),
            ('finesse1', '319978'),
            ('319982', 'potency1'),
            ('319978', 'potency1'),
            ('potency1', '332755'),
            ('potency1', '332756'),
            ('332755', 'endurance2'),
            ('332756', 'endurance2'),
            ('endurance2', 'potency2'),
            ('endurance2', 'endurance3'),
            ('endurance2', 'finesse2'),
            ('potency2', '332754'),
            ('endurance3', '332753'),
            ('finesse2', '319973'),
            ('332754', 'potency3'),
            ('332753', 'potency3'),
            ('319973', 'potency3'),
            ('potency3', '352365'),
            ('potency3', '352415'),
            ('352365', 'finesse3'),
            ('352415', 'endurance4'),
            ('finesse3', '352417'),
            ('endurance4', '352417'),
        ])
        paths = list(
            nx.all_simple_paths(
                soulbindGraph, '340159', '352417', cutoff=None))
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
