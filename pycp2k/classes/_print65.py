from pycp2k.inputsection import InputSection
from ._program_run_info40 import _program_run_info40
from ._restart13 import _restart13


class _print65(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info40()
        self.RESTART = _restart13()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'RESTART': 'RESTART'}

