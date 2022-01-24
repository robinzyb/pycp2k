from pycp2k.inputsection import InputSection
from ._mao19 import _mao19


class _im_time19(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Memory_cut = None
        self.Memory_info = None
        self.Mao = None
        self.Group_size_3c = None
        self.Group_size_p = None
        self.Points_per_magnitude = None
        self.Eps_filter_im_time = None
        self.Stabilize_exp = None
        self.Do_kpoints = None
        self.Do_dbcsr_t = None
        self.Group_size_internal = None
        self.Cutoff_w = None
        self.Kpoints = None
        self.Exp_kpoints = None
        self.Max_block_size_sqrt = None
        self.MAO = _mao19()
        self._name = "IM_TIME"
        self._keywords = {'Memory_cut': 'MEMORY_CUT', 'Memory_info': 'MEMORY_INFO', 'Mao': 'MAO', 'Group_size_3c': 'GROUP_SIZE_3C', 'Group_size_p': 'GROUP_SIZE_P', 'Points_per_magnitude': 'POINTS_PER_MAGNITUDE', 'Eps_filter_im_time': 'EPS_FILTER_IM_TIME', 'Stabilize_exp': 'STABILIZE_EXP', 'Do_kpoints': 'DO_KPOINTS', 'Do_dbcsr_t': 'DO_DBCSR_T', 'Group_size_internal': 'GROUP_SIZE_INTERNAL', 'Cutoff_w': 'CUTOFF_W', 'Kpoints': 'KPOINTS', 'Exp_kpoints': 'EXP_KPOINTS', 'Max_block_size_sqrt': 'MAX_BLOCK_SIZE_SQRT'}
        self._subsections = {'MAO': 'MAO'}
        self._aliases = {'Ppm': 'Points_per_magnitude'}
        self._attributes = ['Section_parameters']


    @property
    def Ppm(self):
        """
        See documentation for Points_per_magnitude
        """
        return self.Points_per_magnitude

    @Ppm.setter
    def Ppm(self, value):
        self.Points_per_magnitude = value
