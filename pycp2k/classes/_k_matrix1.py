from pycp2k.inputsection import InputSection
from ._each386 import _each386


class _k_matrix1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Atoms_list = []
        self.EACH = _each386()
        self._name = "K_MATRIX"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY'}
        self._repeated_keywords = {'Atoms_list': 'ATOMS_LIST'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

