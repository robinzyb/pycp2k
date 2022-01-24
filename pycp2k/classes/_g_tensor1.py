from pycp2k.inputsection import InputSection
from ._each389 import _each389
from ._xc5 import _xc5


class _g_tensor1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Gapw_max_alpha = None
        self.Soo_rho_hard = None
        self.EACH = _each389()
        self.XC = _xc5()
        self._name = "G_TENSOR"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Gapw_max_alpha': 'GAPW_MAX_ALPHA', 'Soo_rho_hard': 'SOO_RHO_HARD'}
        self._subsections = {'EACH': 'EACH', 'XC': 'XC'}
        self._attributes = ['Section_parameters']

