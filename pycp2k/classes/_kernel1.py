from pycp2k.inputsection import InputSection
from ._xc_functional5 import _xc_functional5
from ._exact_exchange1 import _exact_exchange1


class _kernel1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nprocs_grid = None
        self.Ri_region = None
        self.XC_FUNCTIONAL = _xc_functional5()
        self.EXACT_EXCHANGE = _exact_exchange1()
        self._name = "KERNEL"
        self._keywords = {'Nprocs_grid': 'NPROCS_GRID', 'Ri_region': 'RI_REGION'}
        self._subsections = {'XC_FUNCTIONAL': 'XC_FUNCTIONAL', 'EXACT_EXCHANGE': 'EXACT_EXCHANGE'}
        self._aliases = {'Batch_size': 'Nprocs_grid', 'Nprocs_per_grid': 'Nprocs_grid', 'Ri_radius': 'Ri_region'}


    @property
    def Batch_size(self):
        """
        See documentation for Nprocs_grid
        """
        return self.Nprocs_grid

    @property
    def Nprocs_per_grid(self):
        """
        See documentation for Nprocs_grid
        """
        return self.Nprocs_grid

    @property
    def Ri_radius(self):
        """
        See documentation for Ri_region
        """
        return self.Ri_region

    @Batch_size.setter
    def Batch_size(self, value):
        self.Nprocs_grid = value

    @Nprocs_per_grid.setter
    def Nprocs_per_grid(self, value):
        self.Nprocs_grid = value

    @Ri_radius.setter
    def Ri_radius(self, value):
        self.Ri_region = value
