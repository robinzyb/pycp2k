from pycp2k.inputsection import InputSection
from ._spectrum1 import _spectrum1
from ._pdos2 import _pdos2
from ._cubes3 import _cubes3
from ._restart10 import _restart10


class _print39(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.SPECTRUM = _spectrum1()
        self.PDOS = _pdos2()
        self.CUBES = _cubes3()
        self.RESTART = _restart10()
        self._name = "PRINT"
        self._subsections = {'SPECTRUM': 'SPECTRUM', 'PDOS': 'PDOS', 'CUBES': 'CUBES', 'RESTART': 'RESTART'}

