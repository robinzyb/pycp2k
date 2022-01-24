from pycp2k.inputsection import InputSection
from ._parameter1 import _parameter1


class _dftb1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Self_consistent = None
        self.Orthogonal_basis = None
        self.Do_ewald = None
        self.Dispersion = None
        self.Diagonal_dftb3 = None
        self.Hb_sr_gamma = None
        self.Eps_disp = None
        self.PARAMETER = _parameter1()
        self._name = "DFTB"
        self._keywords = {'Self_consistent': 'SELF_CONSISTENT', 'Orthogonal_basis': 'ORTHOGONAL_BASIS', 'Do_ewald': 'DO_EWALD', 'Dispersion': 'DISPERSION', 'Diagonal_dftb3': 'DIAGONAL_DFTB3', 'Hb_sr_gamma': 'HB_SR_GAMMA', 'Eps_disp': 'EPS_DISP'}
        self._subsections = {'PARAMETER': 'PARAMETER'}

