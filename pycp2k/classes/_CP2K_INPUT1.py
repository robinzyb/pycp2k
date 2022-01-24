from pycp2k.inputsection import InputSection
from ._global1 import _global1
from ._test1 import _test1
from ._debug1 import _debug1
from ._motion1 import _motion1
from ._multiple_force_evals1 import _multiple_force_evals1
from ._force_eval3 import _force_eval3
from ._farming1 import _farming1
from ._optimize_input1 import _optimize_input1
from ._optimize_basis1 import _optimize_basis1
from ._swarm1 import _swarm1
from ._ext_restart1 import _ext_restart1
from ._vibrational_analysis1 import _vibrational_analysis1
from ._negf1 import _negf1
from ._atom1 import _atom1


class _CP2K_INPUT1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.GLOBAL = _global1()
        self.TEST = _test1()
        self.DEBUG = _debug1()
        self.MOTION = _motion1()
        self.MULTIPLE_FORCE_EVALS = _multiple_force_evals1()
        self.FORCE_EVAL_list = []
        self.FARMING = _farming1()
        self.OPTIMIZE_INPUT = _optimize_input1()
        self.OPTIMIZE_BASIS = _optimize_basis1()
        self.SWARM = _swarm1()
        self.EXT_RESTART = _ext_restart1()
        self.VIBRATIONAL_ANALYSIS = _vibrational_analysis1()
        self.NEGF = _negf1()
        self.ATOM = _atom1()
        self._name = "CP2K_INPUT"
        self._subsections = {'GLOBAL': 'GLOBAL', 'TEST': 'TEST', 'DEBUG': 'DEBUG', 'MOTION': 'MOTION', 'MULTIPLE_FORCE_EVALS': 'MULTIPLE_FORCE_EVALS', 'FARMING': 'FARMING', 'OPTIMIZE_INPUT': 'OPTIMIZE_INPUT', 'OPTIMIZE_BASIS': 'OPTIMIZE_BASIS', 'SWARM': 'SWARM', 'EXT_RESTART': 'EXT_RESTART', 'VIBRATIONAL_ANALYSIS': 'VIBRATIONAL_ANALYSIS', 'NEGF': 'NEGF', 'ATOM': 'ATOM'}
        self._repeated_subsections = {'FORCE_EVAL': '_force_eval3'}
        self._attributes = ['FORCE_EVAL_list']

    def FORCE_EVAL_add(self, section_parameters=None):
        new_section = _force_eval3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FORCE_EVAL_list.append(new_section)
        return new_section

