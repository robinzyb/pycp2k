from pycp2k.inputsection import InputSection
from ._each285 import _each285


class _adjmat_write1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.EACH = _each285()
        self._name = "ADJMAT_WRITE"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

