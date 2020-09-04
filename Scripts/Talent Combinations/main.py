import itertools
########################################################################################
#Edit this section then click run and paste the output into simc
########################################################################################
#The spec you wish to compare talents for (lower case)
spec = 'frost'
########################################################################################
########################################################################################


def getname( talent_numbers, select_spec ):
    if(select_spec == 'fire') : talent_names_gen = getname_fire(talent_numbers)
    if(select_spec == 'frost') : talent_names_gen = getname_frost(talent_numbers)
    if(select_spec == 'arcane') : talent_names_gen = getname_arcane(talent_numbers)
    return talent_names_gen

def getname_fire( talent_numbers ):
    talents = [
        ('Fstart', 'Pmaniac', 'STouch'),
        ('', '', ''),
        ('IF', 'FM', 'RoP'),
        ('FO', 'AF', 'FtA'),
        ('', '', ''),
        ('FP', 'Conf', 'LB'),
        ('Kind', 'PClasm', 'Met')
    ]
    res = [row[x-1] for (row, x) in zip(talents, talent_numbers)]
    return '_'.join(r for r in res if r != '')

def getname_frost( talent_numbers ):
    talents = [
        ('BC', 'LW', 'IN'),
        ('', '', ''),
        ('IF', 'FM', 'RoP'),
        ('FT', 'CR', 'EB'),
        ('', '', ''),
        ('FR', 'SI', 'CmS'),
        ('TV', 'RoF', 'GS')
    ]
    res = [row[x-1] for (row, x) in zip(talents, talent_numbers)]
    return '_'.join(r for r in res if r != '')

def getname_arcane( talent_numbers ):
    talents = [
        ('Amp', 'RoT', 'ArF'),
        ('', '', ''),
        ('IF', 'FM', 'ROP'),
        ('Res', 'AE', 'NT'),
        ('', '', ''),
        ('Rev', 'AO', 'SN'),
        ('OP', 'TA', 'En')
    ]
    res = [row[x-1] for (row, x) in zip(talents, talent_numbers)]
    return '_'.join(r for r in res if r != '')

print('Generating Profiles')
profile = ""
with open('output.simc', 'w') as outputfile:
  outputfile.write("#Replace this with your desired base profile /simc etc \n\n")
  options = [range(1,4), [0], range(1,4), range(1,4), [0], range(1,4), range(1,4)]
  for talents in itertools.product(*options):
      temp_names = getname( talents, spec )
      profile += "profileset." + temp_names
      profile += "+=talents=" + ''.join(map(str, talents))+"\n"

  outputfile.write(profile)
print('Finished. Please find output in output file.')