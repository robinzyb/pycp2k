from pycp2k.inputsection import InputSection
from ._each256 import _each256


class _rho0_information1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Unit = None
        self.EACH = _each256()
        self._name = "RHO0_INFORMATION"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Unit': 'UNIT'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

