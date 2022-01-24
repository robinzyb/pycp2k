from pycp2k.inputsection import InputSection
from ._conv_info7 import _conv_info7


class _interpolator7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Aint_precond = None
        self.Precond = None
        self.Eps_x = None
        self.Eps_r = None
        self.Max_iter = None
        self.CONV_INFO = _conv_info7()
        self._name = "INTERPOLATOR"
        self._keywords = {'Aint_precond': 'AINT_PRECOND', 'Precond': 'PRECOND', 'Eps_x': 'EPS_X', 'Eps_r': 'EPS_R', 'Max_iter': 'MAX_ITER'}
        self._subsections = {'CONV_INFO': 'CONV_INFO'}
        self._aliases = {'Maxiter': 'Max_iter'}


    @property
    def Maxiter(self):
        """
        See documentation for Max_iter
        """
        return self.Max_iter

    @Maxiter.setter
    def Maxiter(self, value):
        self.Max_iter = value
