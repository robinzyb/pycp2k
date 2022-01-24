from pycp2k.inputsection import InputSection
from ._dos2 import _dos2


class _print76(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DOS = _dos2()
        self._name = "PRINT"
        self._subsections = {'DOS': 'DOS'}

