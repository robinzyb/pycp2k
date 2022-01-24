from pycp2k.inputsection import InputSection


class _almo_optimizer_pcg1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_iter = None
        self.Eps_error = None
        self.Max_iter_early = None
        self.Eps_error_early = None
        self.Lin_search_eps_error = None
        self.Lin_search_step_size_guess = None
        self.Conjugator = None
        self.Precond_filter_threshold = None
        self.Max_iter_outer_loop = None
        self.Preconditioner = None
        self._name = "ALMO_OPTIMIZER_PCG"
        self._keywords = {'Max_iter': 'MAX_ITER', 'Eps_error': 'EPS_ERROR', 'Max_iter_early': 'MAX_ITER_EARLY', 'Eps_error_early': 'EPS_ERROR_EARLY', 'Lin_search_eps_error': 'LIN_SEARCH_EPS_ERROR', 'Lin_search_step_size_guess': 'LIN_SEARCH_STEP_SIZE_GUESS', 'Conjugator': 'CONJUGATOR', 'Precond_filter_threshold': 'PRECOND_FILTER_THRESHOLD', 'Max_iter_outer_loop': 'MAX_ITER_OUTER_LOOP', 'Preconditioner': 'PRECONDITIONER'}

