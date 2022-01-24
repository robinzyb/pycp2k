from pycp2k.inputsection import InputSection
from ._each125 import _each125


class _restart7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Backup_copies = None
        self.Write_cycles = None
        self.EACH = _each125()
        self._name = "RESTART"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Backup_copies': 'BACKUP_COPIES', 'Write_cycles': 'WRITE_CYCLES'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

