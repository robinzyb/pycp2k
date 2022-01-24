from pycp2k.inputsection import InputSection
from ._program_run_info46 import _program_run_info46
from ._forces4 import _forces4
from ._grid_information3 import _grid_information3
from ._total_numbers1 import _total_numbers1
from ._distribution2 import _distribution2
from ._distribution2d1 import _distribution2d1
from ._distribution1d1 import _distribution1d1
from ._stress_tensor1 import _stress_tensor1
from ._grrm1 import _grrm1


class _print72(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info46()
        self.FORCES = _forces4()
        self.GRID_INFORMATION = _grid_information3()
        self.TOTAL_NUMBERS = _total_numbers1()
        self.DISTRIBUTION = _distribution2()
        self.DISTRIBUTION2D = _distribution2d1()
        self.DISTRIBUTION1D = _distribution1d1()
        self.STRESS_TENSOR = _stress_tensor1()
        self.GRRM = _grrm1()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'FORCES': 'FORCES', 'GRID_INFORMATION': 'GRID_INFORMATION', 'TOTAL_NUMBERS': 'TOTAL_NUMBERS', 'DISTRIBUTION': 'DISTRIBUTION', 'DISTRIBUTION2D': 'DISTRIBUTION2D', 'DISTRIBUTION1D': 'DISTRIBUTION1D', 'STRESS_TENSOR': 'STRESS_TENSOR', 'GRRM': 'GRRM'}

