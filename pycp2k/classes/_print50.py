from pycp2k.inputsection import InputSection
from ._program_run_info34 import _program_run_info34
from ._restart12 import _restart12


class _print50(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info34()
        self.RESTART = _restart12()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'RESTART': 'RESTART'}

