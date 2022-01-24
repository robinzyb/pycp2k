from pycp2k.inputsection import InputSection
from ._lbfgs3 import _lbfgs3
from ._cg3 import _cg3
from ._bfgs3 import _bfgs3
from ._print4 import _print4


class _cell_opt1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Optimizer = None
        self.Max_iter = None
        self.Max_dr = None
        self.Max_force = None
        self.Rms_dr = None
        self.Rms_force = None
        self.Step_start_val = None
        self.Type = None
        self.External_pressure = None
        self.Keep_angles = None
        self.Keep_symmetry = None
        self.Constraint = None
        self.Pressure_tolerance = None
        self.LBFGS = _lbfgs3()
        self.CG = _cg3()
        self.BFGS = _bfgs3()
        self.PRINT_list = []
        self._name = "CELL_OPT"
        self._keywords = {'Optimizer': 'OPTIMIZER', 'Max_iter': 'MAX_ITER', 'Max_dr': 'MAX_DR', 'Max_force': 'MAX_FORCE', 'Rms_dr': 'RMS_DR', 'Rms_force': 'RMS_FORCE', 'Step_start_val': 'STEP_START_VAL', 'Type': 'TYPE', 'External_pressure': 'EXTERNAL_PRESSURE', 'Keep_angles': 'KEEP_ANGLES', 'Keep_symmetry': 'KEEP_SYMMETRY', 'Constraint': 'CONSTRAINT', 'Pressure_tolerance': 'PRESSURE_TOLERANCE'}
        self._subsections = {'LBFGS': 'LBFGS', 'CG': 'CG', 'BFGS': 'BFGS'}
        self._repeated_subsections = {'PRINT': '_print4'}
        self._aliases = {'Minimizer': 'Optimizer'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section


    @property
    def Minimizer(self):
        """
        See documentation for Optimizer
        """
        return self.Optimizer

    @Minimizer.setter
    def Minimizer(self, value):
        self.Optimizer = value
