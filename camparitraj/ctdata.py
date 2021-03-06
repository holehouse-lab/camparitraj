"""
ctdata contains all specific data used, and is disinct from configs, which are 
package specific global configurations, while ctdata contains information that
is unambigious as well-defined.

"""
##
##                                       _ _              _ 
##   ___ __ _ _ __ ___  _ __   __ _ _ __(_) |_ _ __ __ _ (_)
##  / __/ _` | '_ ` _ \| '_ \ / _` | '__| | __| '__/ _` || |
## | (_| (_| | | | | | | |_) | (_| | |  | | |_| | | (_| || |
##  \___\__,_|_| |_| |_| .__/ \__,_|_|  |_|\__|_|  \__,_|/ |
##                     |_|                             |__/ 
##
## Alex Holehouse (Pappu Lab and Holehouse Lab)
## Simulation analysis package
## Copyright 2014 - 2021
##



THREE_TO_ONE = {'ALA':'A', 
                'CYS':'C',
                'ASP':'D',
                'GLU':'E',
                'PHE':'F',
                'GLY':'G',
                'HIS':'H', 
                'ILE':'I',
                'LYS':'K',
                'LEU':'L',
                'MET':'M',
                'ASN':'N',
                'PRO':'P',
                'GLN':'Q',
                'ARG':'R',
                'SER':'S',
                'THR':'T',
                'VAL':'V',
                'TRP':'W',
                'TYR':'Y',
                'ACE':'<',
                'NME':'>',
                'NAC':'>'}

ONE_TO_THREE = {'A':'ALA', 
                'C':'CYS',
                'D':'ASP',
                'E':'GLU',
                'F':'PHE',
                'G':'GLY',
                'H':'HIS', 
                'I':'ILE',
                'K':'LYS',
                'L':'LEU',
                'M':'MET',
                'N':'ASN',
                'P':'PRO',
                'Q':'GLN',
                'R':'ARG',
                'S':'SER',
                'T':'THR',
                'V':'VAL',
                'W':'TRP',
                'Y':'TYR',
                '<':'ACE',
                '>':'NME'}

DEFAULT_SIDECHAIN_VECTOR_ATOMS = {'ALA': 'CB', 
                                  'CYS': 'SG',
                                  'ASP': 'CG',
                                  'GLU': 'CD',
                                  'PHE': 'CZ',
                                  'GLY': 'ERROR',
                                  'HIS': 'NE2', 
                                  'ILE': 'CD1',
                                  'LYS': 'NZ',
                                  'LEU': 'CG',
                                  'MET': 'CE',
                                  'ASN': 'CG',
                                  'PRO': 'CG',
                                  'GLN': 'CD',
                                  'ARG': 'CZ',
                                  'SER': 'OG',
                                  'THR': 'CB',
                                  'VAL': 'CB',
                                  'TRP': 'CG',
                                  'TYR': 'CZ',
                                  'ACE': 'ERROR',
                                  'NME': 'ERROR'}

# list of valid residue names as supported by CAMPARI
ALL_VALID_RESIDUE_NAMES = ['ALA','CYS','ASP','ASH','GLU','GLU','PHE','GLY','HIE','HIS','HID','HIP','ILE','LYS','LYD','MET','ASN','PRO','GLN','ARG','SER', 'THR','VAL','TRP','TYR','AIB', 'ABA','NVA','NLE', 'ORN', 'DAB','PTR','TPO','SEP', 'KAC', 'KM1', 'KM2' 'KM3', 'ACE','NME', 'FOR', 'NH2']
