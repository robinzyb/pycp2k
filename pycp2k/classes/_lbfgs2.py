from pycp2k.inputsection import InputSection


class _lbfgs2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_h_rank = None
        self.Max_f_per_iter = None
        self.Wanted_proj_gradient = None
        self.Wanted_rel_f_error = None
        self.Trust_radius = None
        self._name = "LBFGS"
        self._keywords = {'Max_h_rank': 'MAX_H_RANK', 'Max_f_per_iter': 'MAX_F_PER_ITER', 'Wanted_proj_gradient': 'WANTED_PROJ_GRADIENT', 'Wanted_rel_f_error': 'WANTED_REL_F_ERROR', 'Trust_radius': 'TRUST_RADIUS'}

