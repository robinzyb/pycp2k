from pycp2k.inputsection import InputSection
from ._point17 import _point17


class _conditioned_distance1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms_distance = []
        self.Atoms_from = []
        self.Points_from = self.Atoms_from
        self.Atoms_to = []
        self.Points_to = self.Atoms_to
        self.Kinds_from = []
        self.Kinds_to = []
        self.R0 = None
        self.Nn = None
        self.Nd = None
        self.Lambda = None
        self.POINT_list = []
        self._name = "CONDITIONED_DISTANCE"
        self._keywords = {'R0': 'R0', 'Nn': 'NN', 'Nd': 'ND', 'Lambda': 'LAMBDA'}
        self._repeated_keywords = {'Atoms_distance': 'ATOMS_DISTANCE', 'Atoms_from': 'ATOMS_FROM', 'Atoms_to': 'ATOMS_TO', 'Kinds_from': 'KINDS_FROM', 'Kinds_to': 'KINDS_TO'}
        self._repeated_subsections = {'POINT': '_point17'}
        self._aliases = {'R_0': 'R0', 'Expon_numerator': 'Nn', 'Expon_denominator': 'Nd'}
        self._repeated_aliases = {'Points_from': 'Atoms_from', 'Points_to': 'Atoms_to'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point17()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section


    @property
    def R_0(self):
        """
        See documentation for R0
        """
        return self.R0

    @property
    def Expon_numerator(self):
        """
        See documentation for Nn
        """
        return self.Nn

    @property
    def Expon_denominator(self):
        """
        See documentation for Nd
        """
        return self.Nd

    @R_0.setter
    def R_0(self, value):
        self.R0 = value

    @Expon_numerator.setter
    def Expon_numerator(self, value):
        self.Nn = value

    @Expon_denominator.setter
    def Expon_denominator(self, value):
        self.Nd = value
