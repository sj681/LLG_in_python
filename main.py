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

    for timestep in range(0,number_of_timesteps):

        total_field = calculate_fields(total_field, atom_spins[atom_index])

        atom_spins[atom_index].make_timestep(timestep_size, total_field)

        print(atom_spins[atom_index].spin_position)
