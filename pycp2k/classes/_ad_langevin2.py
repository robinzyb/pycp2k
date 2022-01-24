from pycp2k.inputsection import InputSection
from ._chi2 import _chi2
from ._mass5 import _mass5


class _ad_langevin2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Timecon_nh = None
        self.Timecon_langevin = None
        self.CHI = _chi2()
        self.MASS = _mass5()
        self._name = "AD_LANGEVIN"
        self._keywords = {'Timecon_nh': 'TIMECON_NH', 'Timecon_langevin': 'TIMECON_LANGEVIN'}
        self._subsections = {'CHI': 'CHI', 'MASS': 'MASS'}

