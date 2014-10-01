#! /usr/bin/env python

from cp2kase.cp2k import CP2K
from ase import Atom, Atoms

#===============================================================================
# Create the atomic structure here
atoms = Atoms()
atoms.set_cell([5.430697500, 5.430697500, 5.430697500])
atoms.append(Atom("Si", [0.000000000, 0.000000000, 0.000000000]))
atoms.append(Atom("Si", [0.000000000, 2.715348700, 2.715348700]))
atoms.append(Atom("Si", [2.715348700, 2.715348700, 0.000000000]))
atoms.append(Atom("Si", [2.715348700, 0.000000000, 2.715348700]))
atoms.append(Atom("Si", [4.073023100, 1.357674400, 4.073023100]))
atoms.append(Atom("Si", [1.357674400, 1.357674400, 1.357674400]))
atoms.append(Atom("Si", [1.357674400, 4.073023100, 4.073023100]))
atoms.append(Atom("Si", [4.073023100, 4.073023100, 1.357674400]))

#===============================================================================
# Create input tree
calc = CP2K()

# Create shortcuts for the most used subtrees of the input
CP2K_INPUT = calc.CP2K_INPUT
GLOBAL = CP2K_INPUT.GLOBAL
FORCE_EVAL = CP2K_INPUT.FORCE_EVAL
DFT = FORCE_EVAL.DFT
SCF = DFT.SCF

# Global settings
GLOBAL._RUN_TYPE = "ENERGY_FORCE"
GLOBAL._PROJECT = "Si_bulk8"
GLOBAL._PRINT_LEVEL = "LOW"

# Force evaluation
FORCE_EVAL._METHOD = "Quickstep"
FORCE_EVAL.PRINT.FORCES._SECTION_PARAMETERS = "ON"
DFT._BASIS_SET_FILE_NAME = "BASIS_SET"
DFT._POTENTIAL_FILE_NAME = "GTH_POTENTIALS"
DFT.QS._EPS_DEFAULT = 1.0E-10
DFT.MGRID._NGRIDS = 4
DFT.MGRID._CUTOFF = 300
DFT.MGRID._REL_CUTOFF = 60
DFT.XC.XC_FUNCTIONAL._SECTION_PARAMETERS = "PADE"
SCF._SCF_GUESS = "ATOMIC"
SCF._EPS_SCF = 1.0E-7
SCF._MAX_SCF = 300
SCF.DIAGONALIZATION._SECTION_PARAMETERS = "ON"
SCF.DIAGONALIZATION._ALGORITHM = "STANDARD"
SCF.MIXING._SECTION_PARAMETERS = "T"
SCF.MIXING._METHOD = "BROYDEN_MIXING"
SCF.MIXING._ALPHA = 0.4
SCF.MIXING._NBROYDEN = 8
FORCE_EVAL.PRINT.FORCES._SECTION_PARAMETERS = "ON"

# Add basis set and potential for Si atoms
SI = FORCE_EVAL.SUBSYS.KIND
SI._SECTION_PARAMETERS = "Si"
SI._BASIS_SET = "DZVP-GTH-PADE"
SI._POTENTIAL = "GTH-PADE-q4"

#===============================================================================
# Create the coordinates and cell automatically from the Atoms object
calc.add_atoms_to_force_eval(FORCE_EVAL, atoms)

#===============================================================================
# Print the input file
calc.create_input_file()
