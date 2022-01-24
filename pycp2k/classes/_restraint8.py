from pycp2k.inputsection import InputSection


class _restraint8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Target = None
        self.Strength = None
        self.Atom_list = []
        self.Atom_coef = None
        self._name = "RESTRAINT"
        self._keywords = {'Target': 'TARGET', 'Strength': 'STRENGTH', 'Atom_coef': 'ATOM_COEF'}
        self._repeated_keywords = {'Atom_list': 'ATOM_LIST'}

