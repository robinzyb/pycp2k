from pycp2k.inputsection import InputSection
from ._each148 import _each148
from ._weight_function1 import _weight_function1


class _program_run_info16(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.EACH = _each148()
        self.WEIGHT_FUNCTION = _weight_function1()
        self._name = "PROGRAM_RUN_INFO"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY'}
        self._subsections = {'EACH': 'EACH', 'WEIGHT_FUNCTION': 'WEIGHT_FUNCTION'}
        self._attributes = ['Section_parameters']

