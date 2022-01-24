from pycp2k.inputsection import InputSection
from ._each259 import _each259


class _overlap_condition1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Num1_norm = None
        self.Diagonalization = None
        self.Arnoldi = None
        self.EACH = _each259()
        self._name = "OVERLAP_CONDITION"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Num1_norm': '1-NORM', 'Diagonalization': 'DIAGONALIZATION', 'Arnoldi': 'ARNOLDI'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

