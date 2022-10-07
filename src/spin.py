class Spin(object):

    def __init__(self, position_x, position_y, position_z, spin_position_x, spin_position_y, spin_position_z, type_of_material, anisotropy, spin_moment):

        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z
        self.spin_position_x = spin_position_x
        self.spin_position_y = spin_position_y
        self.spin_position_z = spin_position_z
        self.type_of_material = type_of_material
        self.anisotropy = anisotropy
        self.spin_moment = spin_moment

    def anisotropy_field(self):
        return -self.spin_position_z*self.spin_position_z*self.anisotropy


class SpinBuilder(object):
    position_x = 0
    position_y = 0
    position_z = 0
    spin_position_x = 0
    spin_position_y = 0
    spin_position_z = 0

    def __init__(self) -> None:
        pass

    def with_position(self, x, y, z):
        self.position_x = x
        self.position_y = y
        self.position_z = z
        return self
    
    def with_direction(self, x, y, z):
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
            position_x=self.position_x,
            position_y=self.position_y,
            position_z=self.position_z,
            spin_position_x=self.spin_position_x,
            spin_position_y=self.spin_position_y,
            spin_position_z=self.spin_position_z,
            type_of_material=self.type_of_material,
            anisotropy=self.anisotropy,
            spin_moment=self.spin_moment
        )
