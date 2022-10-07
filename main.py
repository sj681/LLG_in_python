import numpy as np
from typing import NamedTuple

from src.spin import SpinBuilder

class Material(NamedTuple):
    spin_moment: float
    exchange_between_i_and_j: float
    anisotropy_i: float


def calculate_fields(field, spin):
    field = [0,0,0]
    field[2] = field[2] + spin.anisotropy_field()
    #field = field + calculate_thermal_field()
    #field = field + calculate_exchange_field()
    return field


if __name__ == '__main__':

    number_of_atoms = 1
    number_of_timesteps = 30
    timestep_size = 1

    atom_spins = [0 for i in range(number_of_atoms)]
    atom_index = 0

    iron = Material(1,1,1)
    cobalt = Material(2,2,2)

    atom_spins[atom_index] = SpinBuilder().with_direction(0.4, 0.8, 0.1).with_type_of_material("iron").with_anisotropy(1).with_spin_moment(1).build()

    total_field = 0

    for i in range(0,number_of_timesteps):

        total_field = calculate_fields(total_field, atom_spins[atom_index])

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
