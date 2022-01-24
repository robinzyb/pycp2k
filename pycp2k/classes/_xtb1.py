from pycp2k.inputsection import InputSection
from ._parameter2 import _parameter2
from ._atom_parameter1 import _atom_parameter1


class _xtb1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Do_ewald = None
        self.Sto_ng = None
        self.Hydrogen_sto_ng = None
        self.Use_halogen_correction = None
        self.Coulomb_interaction = None
        self.Tb3_interaction = None
        self.Check_atomic_charges = None
        self.PARAMETER = _parameter2()
        self.ATOM_PARAMETER_list = []
        self._name = "XTB"
        self._keywords = {'Do_ewald': 'DO_EWALD', 'Sto_ng': 'STO_NG', 'Hydrogen_sto_ng': 'HYDROGEN_STO_NG', 'Use_halogen_correction': 'USE_HALOGEN_CORRECTION', 'Coulomb_interaction': 'COULOMB_INTERACTION', 'Tb3_interaction': 'TB3_INTERACTION', 'Check_atomic_charges': 'CHECK_ATOMIC_CHARGES'}
        self._subsections = {'PARAMETER': 'PARAMETER'}
        self._repeated_subsections = {'ATOM_PARAMETER': '_atom_parameter1'}
        self._attributes = ['ATOM_PARAMETER_list']

    def ATOM_PARAMETER_add(self, section_parameters=None):
        new_section = _atom_parameter1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.ATOM_PARAMETER_list.append(new_section)
        return new_section

