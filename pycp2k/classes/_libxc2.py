from pycp2k.inputsection import InputSection


class _libxc2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Functional = None
        self.Scale = None
        self.Parameters = None
        self._name = "LIBXC"
        self._keywords = {'Functional': 'FUNCTIONAL', 'Scale': 'SCALE', 'Parameters': 'PARAMETERS'}
        self._attributes = ['Section_parameters']

