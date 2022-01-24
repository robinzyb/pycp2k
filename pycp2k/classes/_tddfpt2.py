from pycp2k.inputsection import InputSection
from ._dipole_moments1 import _dipole_moments1
from ._xc6 import _xc6
from ._mgrid2 import _mgrid2
from ._print71 import _print71


class _tddfpt2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Nstates = None
        self.Max_iter = None
        self.Max_kv = None
        self.Nlumo = None
        self.Nproc_state = None
        self.Convergence = None
        self.Min_amplitude = None
        self.Orthogonal_eps = None
        self.Restart = None
        self.Rks_triplets = None
        self.Wfn_restart_file_name = None
        self.DIPOLE_MOMENTS = _dipole_moments1()
        self.XC = _xc6()
        self.MGRID = _mgrid2()
        self.PRINT = _print71()
        self._name = "TDDFPT"
        self._keywords = {'Nstates': 'NSTATES', 'Max_iter': 'MAX_ITER', 'Max_kv': 'MAX_KV', 'Nlumo': 'NLUMO', 'Nproc_state': 'NPROC_STATE', 'Convergence': 'CONVERGENCE', 'Min_amplitude': 'MIN_AMPLITUDE', 'Orthogonal_eps': 'ORTHOGONAL_EPS', 'Restart': 'RESTART', 'Rks_triplets': 'RKS_TRIPLETS', 'Wfn_restart_file_name': 'WFN_RESTART_FILE_NAME'}
        self._subsections = {'DIPOLE_MOMENTS': 'DIPOLE_MOMENTS', 'XC': 'XC', 'MGRID': 'MGRID', 'PRINT': 'PRINT'}
        self._aliases = {'Restart_file_name': 'Wfn_restart_file_name'}
        self._attributes = ['Section_parameters']


    @property
    def Restart_file_name(self):
        """
        See documentation for Wfn_restart_file_name
        """
        return self.Wfn_restart_file_name

    @Restart_file_name.setter
    def Restart_file_name(self, value):
        self.Wfn_restart_file_name = value
