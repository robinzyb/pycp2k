from pycp2k.inputsection import InputSection
from ._cell_ref1 import _cell_ref1


class _cell3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.A = None
        self.B = None
        self.C = None
        self.Abc = None
        self.Alpha_beta_gamma = None
        self.Cell_file_name = None
        self.Cell_file_format = None
        self.Periodic = None
        self.Multiple_unit_cell = None
        self.Symmetry = None
        self.CELL_REF = _cell_ref1()
        self._name = "CELL"
        self._keywords = {'A': 'A', 'B': 'B', 'C': 'C', 'Abc': 'ABC', 'Alpha_beta_gamma': 'ALPHA_BETA_GAMMA', 'Cell_file_name': 'CELL_FILE_NAME', 'Cell_file_format': 'CELL_FILE_FORMAT', 'Periodic': 'PERIODIC', 'Multiple_unit_cell': 'MULTIPLE_UNIT_CELL', 'Symmetry': 'SYMMETRY'}
        self._subsections = {'CELL_REF': 'CELL_REF'}
        self._aliases = {'Angles': 'Alpha_beta_gamma'}


    @property
    def Angles(self):
        """
        See documentation for Alpha_beta_gamma
        """
        return self.Alpha_beta_gamma

    @Angles.setter
    def Angles(self, value):
        self.Alpha_beta_gamma = value
