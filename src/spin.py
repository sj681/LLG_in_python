import numpy as np

class Spin(object):

    Z_INDEX = 2

    def __init__(self, position, magnetization_direction, material_type, anisotropy, spin_moment):
        self.position = position
        self.magnetization_direction = magnetization_direction
        self.material_type = material_type
        self.anisotropy = anisotropy
        self.spin_moment = spin_moment

    def anisotropy_field(self):
        return -self.magnetization_direction[self.Z_INDEX]*self.magnetization_direction[self.Z_INDEX]*self.anisotropy

    def make_timestep(self, timestep_size, total_field):

        s_cross_h = np.cross(self.magnetization_direction, total_field)
        s_cross_s_cross_h = np.cross(self.magnetization_direction, s_cross_h)
        euler_step = (s_cross_h + s_cross_s_cross_h) * timestep_size

        pre_normalized_spin_positions = self.magnetization_direction + euler_step
        self.magnetization_direction = pre_normalized_spin_positions / np.linalg.norm(pre_normalized_spin_positions)


class SpinBuilder(object):
    position = np.array([0, 0, 0])
    magnetization_direction = np.array([0, 0, 0])

    def __init__(self) -> None:
        pass

    def with_position(self, x:float=0, y:float=0, z:float=0):
        self.position = np.array([x, y, z])
        return self
    
    def with_magnetization_direction(self, x:float=0, y:float=0, z:float=0):
        self.magnetization_direction = np.array([x, y, z])
        return self

    def with_material_type(self, material_type):
        self.material_type = material_type
        return self

    def with_anisotropy(self, anisotropy):
        self.anisotropy = anisotropy
        return self

    def with_spin_moment(self, spin_moment):
        self.spin_moment = spin_moment
        return self

    def build(self):
        return Spin(
            position = self.position,
            magnetization_direction = self.magnetization_direction,
            material_type=self.material_type,
            anisotropy=self.anisotropy,
            spin_moment=self.spin_moment
        )
