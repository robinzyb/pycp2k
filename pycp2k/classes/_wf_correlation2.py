from pycp2k.inputsection import InputSection
from ._mp2_info2 import _mp2_info2
from ._direct_canonical2 import _direct_canonical2
from ._wfc_gpw2 import _wfc_gpw2
from ._ri_mp22 import _ri_mp22
from ._opt_ri_basis2 import _opt_ri_basis2
from ._ri_rpa2 import _ri_rpa2
from ._ri_laplace2 import _ri_laplace2
from ._im_time6 import _im_time6
from ._cphf2 import _cphf2
from ._interaction_potential6 import _interaction_potential6
from ._eri_mme3 import _eri_mme3


class _wf_correlation2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method = None
        self.Memory = None
        self.Scale_s = None
        self.Scale_t = None
        self.Group_size = None
        self.Row_block = None
        self.Col_block = None
        self.Calc_cond_num = None
        self.Ri_metric = None
        self.Omega_metric = None
        self.Cutoff_radius_metric = None
        self.Eps_range_metric = None
        self.Eri_method = None
        self.Eri_blksize = None
        self.Im_time = None
        self.Do_svd = None
        self.Eps_svd = None
        self.MP2_INFO = _mp2_info2()
        self.DIRECT_CANONICAL = _direct_canonical2()
        self.WFC_GPW = _wfc_gpw2()
        self.RI_MP2 = _ri_mp22()
        self.OPT_RI_BASIS = _opt_ri_basis2()
        self.RI_RPA = _ri_rpa2()
        self.RI_LAPLACE = _ri_laplace2()
        self.IM_TIME = _im_time6()
        self.CPHF = _cphf2()
        self.INTERACTION_POTENTIAL = _interaction_potential6()
        self.ERI_MME = _eri_mme3()
        self._name = "WF_CORRELATION"
        self._keywords = {'Method': 'METHOD', 'Memory': 'MEMORY', 'Scale_s': 'SCALE_S', 'Scale_t': 'SCALE_T', 'Group_size': 'GROUP_SIZE', 'Row_block': 'ROW_BLOCK', 'Col_block': 'COL_BLOCK', 'Calc_cond_num': 'CALC_COND_NUM', 'Ri_metric': 'RI_METRIC', 'Omega_metric': 'OMEGA_METRIC', 'Cutoff_radius_metric': 'CUTOFF_RADIUS_METRIC', 'Eps_range_metric': 'EPS_RANGE_METRIC', 'Eri_method': 'ERI_METHOD', 'Eri_blksize': 'ERI_BLKSIZE', 'Im_time': 'IM_TIME', 'Do_svd': 'DO_SVD', 'Eps_svd': 'EPS_SVD'}
        self._subsections = {'MP2_INFO': 'MP2_INFO', 'DIRECT_CANONICAL': 'DIRECT_CANONICAL', 'WFC_GPW': 'WFC_GPW', 'RI_MP2': 'RI_MP2', 'OPT_RI_BASIS': 'OPT_RI_BASIS', 'RI_RPA': 'RI_RPA', 'RI_LAPLACE': 'RI_LAPLACE', 'IM_TIME': 'IM_TIME', 'CPHF': 'CPHF', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'ERI_MME': 'ERI_MME'}
        self._aliases = {'Number_proc': 'Group_size', 'Row_block_size': 'Row_block', 'Col_block_size': 'Col_block', 'Calc_condition_number': 'Calc_cond_num', 'Ri': 'Ri_metric', 'Imag_time': 'Im_time'}


    @property
    def Number_proc(self):
        """
        See documentation for Group_size
        """
        return self.Group_size

    @property
    def Row_block_size(self):
        """
        See documentation for Row_block
        """
        return self.Row_block

    @property
    def Col_block_size(self):
        """
        See documentation for Col_block
        """
        return self.Col_block

    @property
    def Calc_condition_number(self):
        """
        See documentation for Calc_cond_num
        """
        return self.Calc_cond_num

    @property
    def Ri(self):
        """
        See documentation for Ri_metric
        """
        return self.Ri_metric

    @property
    def Imag_time(self):
        """
        See documentation for Im_time
        """
        return self.Im_time

    @Number_proc.setter
    def Number_proc(self, value):
        self.Group_size = value

    @Row_block_size.setter
    def Row_block_size(self, value):
        self.Row_block = value

    @Col_block_size.setter
    def Col_block_size(self, value):
        self.Col_block = value

    @Calc_condition_number.setter
    def Calc_condition_number(self, value):
        self.Calc_cond_num = value

    @Ri.setter
    def Ri(self, value):
        self.Ri_metric = value

    @Imag_time.setter
    def Imag_time(self, value):
        self.Im_time = value
