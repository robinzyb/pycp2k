from pycp2k.inputsection import InputSection
from ._point29 import _point29


class _xyz_diag2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atom = None
        self.Component = None
        self.Pbc = None
        self.Absolute_position = None
        self.POINT_list = []
        self._name = "XYZ_DIAG"
        self._keywords = {'Atom': 'ATOM', 'Component': 'COMPONENT', 'Pbc': 'PBC', 'Absolute_position': 'ABSOLUTE_POSITION'}
        self._repeated_subsections = {'POINT': '_point29'}
        self._aliases = {'Point': 'Atom'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point29()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section


    @property
    def Point(self):
        """
        See documentation for Atom
        """
        return self.Atom

    @Point.setter
    def Point(self, value):
        self.Atom = value
