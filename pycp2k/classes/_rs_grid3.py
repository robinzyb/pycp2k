from pycp2k.inputsection import InputSection


class _rs_grid3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Distribution_type = None
        self.Distribution_layout = None
        self.Max_distributed_level = None
        self.Lock_distribution = None
        self.Memory_factor = None
        self.Halo_reduction_factor = None
        self._name = "RS_GRID"
        self._keywords = {'Distribution_type': 'DISTRIBUTION_TYPE', 'Distribution_layout': 'DISTRIBUTION_LAYOUT', 'Max_distributed_level': 'MAX_DISTRIBUTED_LEVEL', 'Lock_distribution': 'LOCK_DISTRIBUTION', 'Memory_factor': 'MEMORY_FACTOR', 'Halo_reduction_factor': 'HALO_REDUCTION_FACTOR'}

