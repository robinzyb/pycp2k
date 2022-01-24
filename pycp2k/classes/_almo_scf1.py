from pycp2k.inputsection import InputSection
from ._almo_optimizer_diis1 import _almo_optimizer_diis1
from ._almo_optimizer_pcg1 import _almo_optimizer_pcg1
from ._xalmo_optimizer_pcg1 import _xalmo_optimizer_pcg1
from ._penalty1 import _penalty1
from ._matrix_iterate1 import _matrix_iterate1
from ._analysis1 import _analysis1


class _almo_scf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_filter = None
        self.Almo_scf_guess = None
        self.Mo_overlap_inv_alg = None
        self.Almo_extrapolation_order = None
        self.Xalmo_extrapolation_order = None
        self.Almo_algorithm = None
        self.Xalmo_trial_wf = None
        self.Delocalize_method = None
        self.Xalmo_r_cutoff_factor = None
        self.Return_orthogonalized_mos = None
        self.ALMO_OPTIMIZER_DIIS = _almo_optimizer_diis1()
        self.ALMO_OPTIMIZER_PCG = _almo_optimizer_pcg1()
        self.XALMO_OPTIMIZER_PCG = _xalmo_optimizer_pcg1()
        self.PENALTY = _penalty1()
        self.MATRIX_ITERATE = _matrix_iterate1()
        self.ANALYSIS = _analysis1()
        self._name = "ALMO_SCF"
        self._keywords = {'Eps_filter': 'EPS_FILTER', 'Almo_scf_guess': 'ALMO_SCF_GUESS', 'Mo_overlap_inv_alg': 'MO_OVERLAP_INV_ALG', 'Almo_extrapolation_order': 'ALMO_EXTRAPOLATION_ORDER', 'Xalmo_extrapolation_order': 'XALMO_EXTRAPOLATION_ORDER', 'Almo_algorithm': 'ALMO_ALGORITHM', 'Xalmo_trial_wf': 'XALMO_TRIAL_WF', 'Delocalize_method': 'DELOCALIZE_METHOD', 'Xalmo_r_cutoff_factor': 'XALMO_R_CUTOFF_FACTOR', 'Return_orthogonalized_mos': 'RETURN_ORTHOGONALIZED_MOS'}
        self._subsections = {'ALMO_OPTIMIZER_DIIS': 'ALMO_OPTIMIZER_DIIS', 'ALMO_OPTIMIZER_PCG': 'ALMO_OPTIMIZER_PCG', 'XALMO_OPTIMIZER_PCG': 'XALMO_OPTIMIZER_PCG', 'PENALTY': 'PENALTY', 'MATRIX_ITERATE': 'MATRIX_ITERATE', 'ANALYSIS': 'ANALYSIS'}

