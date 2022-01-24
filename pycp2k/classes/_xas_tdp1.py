from pycp2k.inputsection import InputSection
from ._donor_states1 import _donor_states1
from ._kernel1 import _kernel1
from ._print39 import _print39


class _xas_tdp1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Check_only = None
        self.Restart_from_file = None
        self.Excitations = []
        self.Excitation = self.Excitations
        self.Eps_pgf_xas = None
        self.Eps_filter = None
        self.Dipole_form = None
        self.Quadrupole = None
        self.Spin_orbit_coupling = None
        self.Tamm_dancoff = None
        self.Grid = []
        self.Atomic_grid = self.Grid
        self.N_excited = None
        self.Energy_range = None
        self.DONOR_STATES = _donor_states1()
        self.KERNEL = _kernel1()
        self.PRINT = _print39()
        self._name = "XAS_TDP"
        self._keywords = {'Check_only': 'CHECK_ONLY', 'Restart_from_file': 'RESTART_FROM_FILE', 'Eps_pgf_xas': 'EPS_PGF_XAS', 'Eps_filter': 'EPS_FILTER', 'Dipole_form': 'DIPOLE_FORM', 'Quadrupole': 'QUADRUPOLE', 'Spin_orbit_coupling': 'SPIN_ORBIT_COUPLING', 'Tamm_dancoff': 'TAMM_DANCOFF', 'N_excited': 'N_EXCITED', 'Energy_range': 'ENERGY_RANGE'}
        self._repeated_keywords = {'Excitations': 'EXCITATIONS', 'Grid': 'GRID'}
        self._subsections = {'DONOR_STATES': 'DONOR_STATES', 'KERNEL': 'KERNEL', 'PRINT': 'PRINT'}
        self._aliases = {'Restart_filename': 'Restart_from_file', 'Rst_filename': 'Restart_from_file', 'Restart_file': 'Restart_from_file', 'Rst_file': 'Restart_from_file', 'Eps_pgf': 'Eps_pgf_xas', 'Eps_pgf_xas_tdp': 'Eps_pgf_xas', 'Eps_filter_matrix': 'Eps_filter', 'Dip_form': 'Dipole_form', 'Do_quadrupole': 'Quadrupole', 'Do_quad': 'Quadrupole', 'Quad': 'Quadrupole', 'Soc': 'Spin_orbit_coupling', 'Tda': 'Tamm_dancoff', 'N_roots': 'N_excited', 'E_range': 'Energy_range'}
        self._repeated_aliases = {'Excitation': 'Excitations', 'Atomic_grid': 'Grid'}
        self._attributes = ['Section_parameters']


    @property
    def Restart_filename(self):
        """
        See documentation for Restart_from_file
        """
        return self.Restart_from_file

    @property
    def Rst_filename(self):
        """
        See documentation for Restart_from_file
        """
        return self.Restart_from_file

    @property
    def Restart_file(self):
        """
        See documentation for Restart_from_file
        """
        return self.Restart_from_file

    @property
    def Rst_file(self):
        """
        See documentation for Restart_from_file
        """
        return self.Restart_from_file

    @property
    def Eps_pgf(self):
        """
        See documentation for Eps_pgf_xas
        """
        return self.Eps_pgf_xas

    @property
    def Eps_pgf_xas_tdp(self):
        """
        See documentation for Eps_pgf_xas
        """
        return self.Eps_pgf_xas

    @property
    def Eps_filter_matrix(self):
        """
        See documentation for Eps_filter
        """
        return self.Eps_filter

    @property
    def Dip_form(self):
        """
        See documentation for Dipole_form
        """
        return self.Dipole_form

    @property
    def Do_quadrupole(self):
        """
        See documentation for Quadrupole
        """
        return self.Quadrupole

    @property
    def Do_quad(self):
        """
        See documentation for Quadrupole
        """
        return self.Quadrupole

    @property
    def Quad(self):
        """
        See documentation for Quadrupole
        """
        return self.Quadrupole

    @property
    def Soc(self):
        """
        See documentation for Spin_orbit_coupling
        """
        return self.Spin_orbit_coupling

    @property
    def Tda(self):
        """
        See documentation for Tamm_dancoff
        """
        return self.Tamm_dancoff

    @property
    def N_roots(self):
        """
        See documentation for N_excited
        """
        return self.N_excited

    @property
    def E_range(self):
        """
        See documentation for Energy_range
        """
        return self.Energy_range

    @Restart_filename.setter
    def Restart_filename(self, value):
        self.Restart_from_file = value

    @Rst_filename.setter
    def Rst_filename(self, value):
        self.Restart_from_file = value

    @Restart_file.setter
    def Restart_file(self, value):
        self.Restart_from_file = value

    @Rst_file.setter
    def Rst_file(self, value):
        self.Restart_from_file = value

    @Eps_pgf.setter
    def Eps_pgf(self, value):
        self.Eps_pgf_xas = value

    @Eps_pgf_xas_tdp.setter
    def Eps_pgf_xas_tdp(self, value):
        self.Eps_pgf_xas = value

    @Eps_filter_matrix.setter
    def Eps_filter_matrix(self, value):
        self.Eps_filter = value

    @Dip_form.setter
    def Dip_form(self, value):
        self.Dipole_form = value

    @Do_quadrupole.setter
    def Do_quadrupole(self, value):
        self.Quadrupole = value

    @Do_quad.setter
    def Do_quad(self, value):
        self.Quadrupole = value

    @Quad.setter
    def Quad(self, value):
        self.Quadrupole = value

    @Soc.setter
    def Soc(self, value):
        self.Spin_orbit_coupling = value

    @Tda.setter
    def Tda(self, value):
        self.Tamm_dancoff = value

    @N_roots.setter
    def N_roots(self, value):
        self.N_excited = value

    @E_range.setter
    def E_range(self, value):
        self.Energy_range = value
