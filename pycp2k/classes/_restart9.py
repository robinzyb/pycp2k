from pycp2k.inputsection import InputSection
from ._each209 import _each209


class _restart9(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.EACH = _each209()
        self._name = "RESTART"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

