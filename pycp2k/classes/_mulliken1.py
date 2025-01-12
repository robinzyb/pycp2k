from pycp2k.inputsection import InputSection
from ._each275 import _each275


class _mulliken1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Print_gop = None
        self.Print_all = None
        self.EACH = _each275()
        self._name = "MULLIKEN"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Print_gop': 'PRINT_GOP', 'Print_all': 'PRINT_ALL'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

