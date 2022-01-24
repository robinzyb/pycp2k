from pycp2k.inputsection import InputSection
from ._libxc5 import _libxc5


class _xc_functional5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.LIBXC_list = []
        self._name = "XC_FUNCTIONAL"
        self._repeated_subsections = {'LIBXC': '_libxc5'}
        self._attributes = ['Section_parameters', 'LIBXC_list']

    def LIBXC_add(self, section_parameters=None):
        new_section = _libxc5()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LIBXC_list.append(new_section)
        return new_section

