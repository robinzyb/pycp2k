from pycp2k.inputsection import InputSection


class _penalty1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Occupied_volume_penalty_method = None
        self.Occupied_volume_penalty_coeff = None
        self._name = "PENALTY"
        self._keywords = {'Occupied_volume_penalty_method': 'OCCUPIED_VOLUME_PENALTY_METHOD', 'Occupied_volume_penalty_coeff': 'OCCUPIED_VOLUME_PENALTY_COEFF'}

