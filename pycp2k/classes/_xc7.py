from pycp2k.inputsection import InputSection
from ._xc_grid7 import _xc_grid7
from ._xc_functional8 import _xc_functional8
from ._hf13 import _hf13
from ._wf_correlation7 import _wf_correlation7
from ._adiabatic_rescaling7 import _adiabatic_rescaling7
from ._xc_potential7 import _xc_potential7
from ._vdw_potential7 import _vdw_potential7
from ._gcp_potential7 import _gcp_potential7


class _xc7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Density_cutoff = None
        self.Gradient_cutoff = None
        self.Density_smooth_cutoff_range = None
        self.Tau_cutoff = None
        self.Functional_routine = None
        self.Num2nd_deriv_analytical = None
        self.Num3rd_deriv_analytical = None
        self.XC_GRID = _xc_grid7()
        self.XC_FUNCTIONAL = _xc_functional8()
        self.HF_list = []
        self.WF_CORRELATION_list = []
        self.ADIABATIC_RESCALING = _adiabatic_rescaling7()
        self.XC_POTENTIAL = _xc_potential7()
        self.VDW_POTENTIAL = _vdw_potential7()
        self.GCP_POTENTIAL = _gcp_potential7()
        self._name = "XC"
        self._keywords = {'Density_cutoff': 'DENSITY_CUTOFF', 'Gradient_cutoff': 'GRADIENT_CUTOFF', 'Density_smooth_cutoff_range': 'DENSITY_SMOOTH_CUTOFF_RANGE', 'Tau_cutoff': 'TAU_CUTOFF', 'Functional_routine': 'FUNCTIONAL_ROUTINE', 'Num2nd_deriv_analytical': '2ND_DERIV_ANALYTICAL', 'Num3rd_deriv_analytical': '3RD_DERIV_ANALYTICAL'}
        self._subsections = {'XC_GRID': 'XC_GRID', 'XC_FUNCTIONAL': 'XC_FUNCTIONAL', 'ADIABATIC_RESCALING': 'ADIABATIC_RESCALING', 'XC_POTENTIAL': 'XC_POTENTIAL', 'VDW_POTENTIAL': 'VDW_POTENTIAL', 'GCP_POTENTIAL': 'GCP_POTENTIAL'}
        self._repeated_subsections = {'HF': '_hf13', 'WF_CORRELATION': '_wf_correlation7'}
        self._attributes = ['HF_list', 'WF_CORRELATION_list']

    def HF_add(self, section_parameters=None):
        new_section = _hf13()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.HF_list.append(new_section)
        return new_section

    def WF_CORRELATION_add(self, section_parameters=None):
        new_section = _wf_correlation7()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.WF_CORRELATION_list.append(new_section)
        return new_section

