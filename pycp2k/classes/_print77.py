from pycp2k.inputsection import InputSection
from ._dos3 import _dos3
from ._transmission1 import _transmission1


class _print77(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DOS = _dos3()
        self.TRANSMISSION = _transmission1()
        self._name = "PRINT"
        self._subsections = {'DOS': 'DOS', 'TRANSMISSION': 'TRANSMISSION'}

