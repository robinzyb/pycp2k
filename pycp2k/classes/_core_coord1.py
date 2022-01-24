from pycp2k.inputsection import InputSection


class _core_coord1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Unit = None
        self.Scaled = None
        self.Default_keyword = []
        self._name = "CORE_COORD"
        self._keywords = {'Unit': 'UNIT', 'Scaled': 'SCALED'}
        self._repeated_default_keywords = {'Default_keyword': 'DEFAULT_KEYWORD'}
        self._attributes = ['Default_keyword']

