from pycp2k.inputsection import InputSection


class _memory5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_storage = None
        self.Max_memory = None
        self.Compress = None
        self._name = "MEMORY"
        self._keywords = {'Eps_storage': 'EPS_STORAGE', 'Max_memory': 'MAX_MEMORY', 'Compress': 'COMPRESS'}

