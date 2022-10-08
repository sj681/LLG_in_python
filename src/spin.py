import numpy as np

class Spin(object):

    Z_INDEX = 2

    def __init__(self, position, spin_position, type_of_material, anisotropy, spin_moment):
        self.position = position
        self.spin_position = spin_position
        self.type_of_material = type_of_material
        self.anisotropy = anisotropy
        self.spin_moment = spin_moment

    def anisotropy_field(self):
        return -self.spin_position[self.Z_INDEX]*self.spin_position[self.Z_INDEX]*self.anisotropy


class SpinBuilder(object):
    position_x = 0
    position_y = 0
    position_z = 0
    spin_position_x = 0
    spin_position_y = 0
    spin_position_z = 0

    def __init__(self) -> None:
        pass

    def with_position(self, x:float=0, y:float=0, z:float=0):
        self.position_x = x
        self.position_y = y
        self.position_z = z
        return self
    
    def with_direction(self, x:float=0, y:float=0, z:float=0):
        self.spin_position_x = x
        self.spin_position_y = y
        self.spin_position_z = z
        return self

    def with_type_of_material(self, type_of_material):
        self.type_of_material = type_of_material
        return self

    def with_anisotropy(self, anisotropy):
        self.anisotropy = anisotropy
        return self

    def with_spin_moment(self, spin_moment):
        self.spin_moment = spin_moment
        return self

    def build(self):
        return Spin(
            position = np.array([self.position_x, self.position_y, self.position_z]),
            spin_position = np.array([self.spin_position_x, self.spin_position_y, self.spin_position_z]),
            type_of_material=self.type_of_material,
            anisotropy=self.anisotropy,
            spin_moment=self.spin_moment
        )
