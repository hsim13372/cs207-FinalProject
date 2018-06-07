
"""Example of reversible reaction."""

import os

from chemkinlib.utils import Parser
from chemkinlib.reactions import ReactionSystems
from chemkinlib.config import DATA_DIRECTORY

# USER INPUT: reaction (xml) file
xml_filename = "rxns_reversible.xml"

parser = Parser.ReactionParser(xml_filename)

# USER INPUTS (concentrations and temperatures)
concentration = ({'H':5.0000000000000000e-01,
                 'H2':2.0000000000000000e+00,
                 'H2O':0,
                 'H2O2':0,
                 'HO2':0,
                 'O':0,
                 'O2':1.0000000000000000e+00,
                 'OH':0})
temperature = 900.


# Set up reaction system
rxnsys = ReactionSystems.ReactionSystem(parser.reaction_list,
                                  parser.NASA_poly_coefs,
                                  temperature,
                                  concentration)

# #compute the concentration change with timestep
# for i in range(20):
#     dt = 1e-15
#     print("The concentration after", i, "timestep is")
#     print(list(rxnsys.step(dt)[1]))

# Compute and sort reaction rates
rxnrates_dict = rxnsys.sort_reaction_rates()

# display reaction rates by species
for k, v in rxnrates_dict.items():
    print("d[{0}]/dt : \t {1:e}".format(k, v))
