from pycp2k.inputsection import InputSection
from ._each374 import _each374


class _molecular_moments4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Order = None
        self.EACH = _each374()
        self._name = "MOLECULAR_MOMENTS"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Order': 'ORDER'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

