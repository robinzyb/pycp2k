from pycp2k.inputsection import InputSection
from ._response_function_cubes2 import _response_function_cubes2
from ._chi_tensor1 import _chi_tensor1
from ._shielding_tensor1 import _shielding_tensor1


class _print59(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.RESPONSE_FUNCTION_CUBES = _response_function_cubes2()
        self.CHI_TENSOR = _chi_tensor1()
        self.SHIELDING_TENSOR = _shielding_tensor1()
        self._name = "PRINT"
        self._subsections = {'RESPONSE_FUNCTION_CUBES': 'RESPONSE_FUNCTION_CUBES', 'CHI_TENSOR': 'CHI_TENSOR', 'SHIELDING_TENSOR': 'SHIELDING_TENSOR'}

