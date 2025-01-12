from pycp2k.inputsection import InputSection
from ._becke887 import _becke887
from ._lyp_adiabatic7 import _lyp_adiabatic7
from ._becke88_lr_adiabatic7 import _becke88_lr_adiabatic7
from ._becke88_lr7 import _becke88_lr7
from ._lyp7 import _lyp7
from ._pade7 import _pade7
from ._hcth7 import _hcth7
from ._optx7 import _optx7
from ._libxc8 import _libxc8
from ._ke_libxc7 import _ke_libxc7
from ._cs17 import _cs17
from ._xgga7 import _xgga7
from ._ke_gga7 import _ke_gga7
from ._p86c7 import _p86c7
from ._pw927 import _pw927
from ._pz817 import _pz817
from ._tfw7 import _tfw7
from ._tf7 import _tf7
from ._vwn7 import _vwn7
from ._xalpha7 import _xalpha7
from ._tpss7 import _tpss7
from ._pbe7 import _pbe7
from ._xwpbe7 import _xwpbe7
from ._becke977 import _becke977
from ._becke_roussel7 import _becke_roussel7
from ._lda_hole_t_c_lr7 import _lda_hole_t_c_lr7
from ._pbe_hole_t_c_lr7 import _pbe_hole_t_c_lr7
from ._gv097 import _gv097
from ._beef7 import _beef7
from ._srlda7 import _srlda7


class _xc_functional8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.BECKE88 = _becke887()
        self.LYP_ADIABATIC = _lyp_adiabatic7()
        self.BECKE88_LR_ADIABATIC = _becke88_lr_adiabatic7()
        self.BECKE88_LR = _becke88_lr7()
        self.LYP = _lyp7()
        self.PADE = _pade7()
        self.HCTH = _hcth7()
        self.OPTX = _optx7()
        self.LIBXC_list = []
        self.KE_LIBXC_list = []
        self.CS1 = _cs17()
        self.XGGA = _xgga7()
        self.KE_GGA = _ke_gga7()
        self.P86C = _p86c7()
        self.PW92 = _pw927()
        self.PZ81 = _pz817()
        self.TFW = _tfw7()
        self.TF = _tf7()
        self.VWN = _vwn7()
        self.XALPHA = _xalpha7()
        self.TPSS = _tpss7()
        self.PBE = _pbe7()
        self.XWPBE = _xwpbe7()
        self.BECKE97 = _becke977()
        self.BECKE_ROUSSEL = _becke_roussel7()
        self.LDA_HOLE_T_C_LR = _lda_hole_t_c_lr7()
        self.PBE_HOLE_T_C_LR = _pbe_hole_t_c_lr7()
        self.GV09 = _gv097()
        self.BEEF = _beef7()
        self.SRLDA = _srlda7()
        self._name = "XC_FUNCTIONAL"
        self._subsections = {'BECKE88': 'BECKE88', 'LYP_ADIABATIC': 'LYP_ADIABATIC', 'BECKE88_LR_ADIABATIC': 'BECKE88_LR_ADIABATIC', 'BECKE88_LR': 'BECKE88_LR', 'LYP': 'LYP', 'PADE': 'PADE', 'HCTH': 'HCTH', 'OPTX': 'OPTX', 'CS1': 'CS1', 'XGGA': 'XGGA', 'KE_GGA': 'KE_GGA', 'P86C': 'P86C', 'PW92': 'PW92', 'PZ81': 'PZ81', 'TFW': 'TFW', 'TF': 'TF', 'VWN': 'VWN', 'XALPHA': 'XALPHA', 'TPSS': 'TPSS', 'PBE': 'PBE', 'XWPBE': 'XWPBE', 'BECKE97': 'BECKE97', 'BECKE_ROUSSEL': 'BECKE_ROUSSEL', 'LDA_HOLE_T_C_LR': 'LDA_HOLE_T_C_LR', 'PBE_HOLE_T_C_LR': 'PBE_HOLE_T_C_LR', 'GV09': 'GV09', 'BEEF': 'BEEF', 'SRLDA': 'SRLDA'}
        self._repeated_subsections = {'LIBXC': '_libxc8', 'KE_LIBXC': '_ke_libxc7'}
        self._attributes = ['Section_parameters', 'LIBXC_list', 'KE_LIBXC_list']

    def LIBXC_add(self, section_parameters=None):
        new_section = _libxc8()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LIBXC_list.append(new_section)
        return new_section

    def KE_LIBXC_add(self, section_parameters=None):
        new_section = _ke_libxc7()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KE_LIBXC_list.append(new_section)
        return new_section

