from pycp2k.inputsection import InputSection


class _beyn1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.N_rand = None
        self.N_rand_cc = None
        self.Svd_cutoff = None
        self.N_points_beyn = None
        self.One_circle = None
        self.Tasks_per_integration_point = None
        self._name = "BEYN"
        self._keywords = {'N_rand': 'N_RAND', 'N_rand_cc': 'N_RAND_CC', 'Svd_cutoff': 'SVD_CUTOFF', 'N_points_beyn': 'N_POINTS_BEYN', 'One_circle': 'ONE_CIRCLE', 'Tasks_per_integration_point': 'TASKS_PER_INTEGRATION_POINT'}

