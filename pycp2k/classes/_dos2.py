from pycp2k.inputsection import InputSection
from ._each452 import _each452


class _dos2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.From_energy = None
        self.Till_energy = None
        self.N_gridpoints = None
        self.EACH = _each452()
        self._name = "DOS"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'From_energy': 'FROM_ENERGY', 'Till_energy': 'TILL_ENERGY', 'N_gridpoints': 'N_GRIDPOINTS'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

