from pycp2k.inputsection import InputSection


class _aa_cuboidal3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.V_d = None
        self.Oscillating_fraction = None
        self.Frequency = None
        self.Phase = None
        self.X_xtnt = None
        self.Y_xtnt = None
        self.Z_xtnt = None
        self.N_prtn = None
        self.Smoothing_width = None
        self.Periodic_region = None
        self._name = "AA_CUBOIDAL"
        self._keywords = {'V_d': 'V_D', 'Oscillating_fraction': 'OSCILLATING_FRACTION', 'Frequency': 'FREQUENCY', 'Phase': 'PHASE', 'X_xtnt': 'X_XTNT', 'Y_xtnt': 'Y_XTNT', 'Z_xtnt': 'Z_XTNT', 'N_prtn': 'N_PRTN', 'Smoothing_width': 'SMOOTHING_WIDTH', 'Periodic_region': 'PERIODIC_REGION'}
        self._aliases = {'Sigma': 'Smoothing_width'}


    @property
    def Sigma(self):
        """
        See documentation for Smoothing_width
        """
        return self.Smoothing_width

    @Sigma.setter
    def Sigma(self, value):
        self.Smoothing_width = value
