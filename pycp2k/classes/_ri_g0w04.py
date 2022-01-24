from pycp2k.inputsection import InputSection
from ._periodic12 import _periodic12
from ._bse4 import _bse4
from ._ic4 import _ic4


class _ri_g0w04(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Corr_mos_occ = None
        self.Corr_mos_virt = None
        self.Numb_poles = None
        self.Omega_max_fit = None
        self.Print_fit_error = None
        self.Max_iter_fit = None
        self.Check_fit = None
        self.Crossing_search = None
        self.Fermi_level_offset = None
        self.Ev_sc_iter = None
        self.Eps_ev_sc_iter = None
        self.Hf_like_ev_start = None
        self.Ev_sc_gw_remove_neg_virt_energies = None
        self.Print_gw_details = None
        self.Print_exx = None
        self.Ri_sigma_x = None
        self.Ic_corr_list = None
        self.Ic_corr_list_beta = None
        self.Periodic = None
        self.Bse = None
        self.Image_charge_model = None
        self.Analytic_continuation = None
        self.Nparam_pade = None
        self.Gamma_only_sigma = None
        self.PERIODIC = _periodic12()
        self.BSE = _bse4()
        self.IC = _ic4()
        self._name = "RI_G0W0"
        self._keywords = {'Corr_mos_occ': 'CORR_MOS_OCC', 'Corr_mos_virt': 'CORR_MOS_VIRT', 'Numb_poles': 'NUMB_POLES', 'Omega_max_fit': 'OMEGA_MAX_FIT', 'Print_fit_error': 'PRINT_FIT_ERROR', 'Max_iter_fit': 'MAX_ITER_FIT', 'Check_fit': 'CHECK_FIT', 'Crossing_search': 'CROSSING_SEARCH', 'Fermi_level_offset': 'FERMI_LEVEL_OFFSET', 'Ev_sc_iter': 'EV_SC_ITER', 'Eps_ev_sc_iter': 'EPS_EV_SC_ITER', 'Hf_like_ev_start': 'HF_LIKE_EV_START', 'Ev_sc_gw_remove_neg_virt_energies': 'EV_SC_GW_REMOVE_NEG_VIRT_ENERGIES', 'Print_gw_details': 'PRINT_GW_DETAILS', 'Print_exx': 'PRINT_EXX', 'Ri_sigma_x': 'RI_SIGMA_X', 'Ic_corr_list': 'IC_CORR_LIST', 'Ic_corr_list_beta': 'IC_CORR_LIST_BETA', 'Periodic': 'PERIODIC', 'Bse': 'BSE', 'Image_charge_model': 'IMAGE_CHARGE_MODEL', 'Analytic_continuation': 'ANALYTIC_CONTINUATION', 'Nparam_pade': 'NPARAM_PADE', 'Gamma_only_sigma': 'GAMMA_ONLY_SIGMA'}
        self._subsections = {'PERIODIC': 'PERIODIC', 'BSE': 'BSE', 'IC': 'IC'}
        self._aliases = {'Corr_occ': 'Corr_mos_occ', 'Corr_virt': 'Corr_mos_virt', 'Fit_error': 'Print_fit_error', 'Remove_neg': 'Ev_sc_gw_remove_neg_virt_energies', 'Ic': 'Image_charge_model', 'Gamma': 'Gamma_only_sigma'}


    @property
    def Corr_occ(self):
        """
        See documentation for Corr_mos_occ
        """
        return self.Corr_mos_occ

    @property
    def Corr_virt(self):
        """
        See documentation for Corr_mos_virt
        """
        return self.Corr_mos_virt

    @property
    def Fit_error(self):
        """
        See documentation for Print_fit_error
        """
        return self.Print_fit_error

    @property
    def Remove_neg(self):
        """
        See documentation for Ev_sc_gw_remove_neg_virt_energies
        """
        return self.Ev_sc_gw_remove_neg_virt_energies

    @property
    def Ic(self):
        """
        See documentation for Image_charge_model
        """
        return self.Image_charge_model

    @property
    def Gamma(self):
        """
        See documentation for Gamma_only_sigma
        """
        return self.Gamma_only_sigma

    @Corr_occ.setter
    def Corr_occ(self, value):
        self.Corr_mos_occ = value

    @Corr_virt.setter
    def Corr_virt(self, value):
        self.Corr_mos_virt = value

    @Fit_error.setter
    def Fit_error(self, value):
        self.Print_fit_error = value

    @Remove_neg.setter
    def Remove_neg(self, value):
        self.Ev_sc_gw_remove_neg_virt_energies = value

    @Ic.setter
    def Ic(self, value):
        self.Image_charge_model = value

    @Gamma.setter
    def Gamma(self, value):
        self.Gamma_only_sigma = value
