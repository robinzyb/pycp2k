from pycp2k.inputsection import InputSection
from ._im_time8 import _im_time8


class _ri_laplace3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Quadrature_points = None
        self.Size_integ_group = None
        self.Im_time = None
        self.IM_TIME = _im_time8()
        self._name = "RI_LAPLACE"
        self._keywords = {'Quadrature_points': 'QUADRATURE_POINTS', 'Size_integ_group': 'SIZE_INTEG_GROUP', 'Im_time': 'IM_TIME'}
        self._subsections = {'IM_TIME': 'IM_TIME'}
        self._aliases = {'Laplace_num_quad_points': 'Quadrature_points', 'Laplace_group_size': 'Size_integ_group', 'Imag_time': 'Im_time'}


    @property
    def Laplace_num_quad_points(self):
        """
        See documentation for Quadrature_points
        """
        return self.Quadrature_points

    @property
    def Laplace_group_size(self):
        """
        See documentation for Size_integ_group
        """
        return self.Size_integ_group

    @property
    def Imag_time(self):
        """
        See documentation for Im_time
        """
        return self.Im_time

    @Laplace_num_quad_points.setter
    def Laplace_num_quad_points(self, value):
        self.Quadrature_points = value

    @Laplace_group_size.setter
    def Laplace_group_size(self, value):
        self.Size_integ_group = value

    @Imag_time.setter
    def Imag_time(self, value):
        self.Im_time = value
