import numpy as np
from collections import namedtuple


class Material(namedtuple):
    spin_moment: float
    exchange_between_i_and_j: float
    anisotropy_i: float


class Spin(object):

    def __init__(self, position_x,position_y, position_z, spin_position_x, spin_position_y,spin_position_z,type_of_material,anisotropy,spin_moment):

        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z
        self.spin_position_x = spin_position_x
        self.spin_position_y = spin_position_y
        self.spin_position_z = spin_position_z
        self.type_of_material = type_of_material
        self.anisotropy = anisotropy
        self.spin_moment = spin_moment

def calculate_fields(field):
    field = [0,0,0]
    field[2] = field[2] + calculate_anisotropy_field()
    #field = field + calculate_thermal_field()
    #field = field + calculate_exchange_field()
    return field

def calculate_anisotropy_field():

    return -atom_spins[atom_index].spin_position_z*atom_spins[atom_index].spin_position_z*atom_spins[atom_index].anisotropy


if __name__ == '__main__':

    number_of_atoms = 1
    number_of_timesteps = 30
    timestep_size = 1

    atom_spins = [0 for i in range(number_of_atoms)]
    atom_index = 0

    iron = Material(1,1,1)
    cobalt = Material(2,2,2)

    atom_spins[atom_index] = Spin(0,0,0,0.4,0.8,0.1,"iron",1,1)

    total_field = 0

    for i in range(0,number_of_timesteps):

        total_field = calculate_fields(total_field)

        spin_positions = [atom_spins[atom_index].spin_position_x,atom_spins[atom_index].spin_position_y,atom_spins[atom_index].spin_position_z]

        s_cross_h = np.cross(spin_positions, total_field)
        s_cross_s_cross_h = np.cross(spin_positions, s_cross_h)
        euler_step = s_cross_h + s_cross_s_cross_h

        spin_positions_after_euler_step = [0,0,0]
        spin_positions_after_euler_step[0]=atom_spins[atom_index].spin_position_x + euler_step[0]*timestep_size
        spin_positions_after_euler_step[1]=atom_spins[atom_index].spin_position_y + euler_step[1]*timestep_size
        spin_positions_after_euler_step[2]=atom_spins[atom_index].spin_position_z + euler_step[2]*timestep_size

        spin_positions_after_euler_step = spin_positions_after_euler_step/np.linalg.norm(spin_positions_after_euler_step)

        atom_spins[atom_index].spin_position_x = spin_positions_after_euler_step[0]
        atom_spins[atom_index].spin_position_y = spin_positions_after_euler_step[1]
        atom_spins[atom_index].spin_position_z = spin_positions_after_euler_step[2]

        print(spin_positions_after_euler_step)
