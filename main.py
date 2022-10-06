import numpy as np


class material_properties(object):
    #class to store the magnetic properties of each material type
    def __init__(self, spin_moment, exchange_between_i_and_j, anisotropy_i):
        #spin moment
        self.spin_moment = spin_moment
        #exchange
        self.exchange_between_i_and_j = exchange_between_i_and_j
        #anisotropy
        self.anisotropy_i = anisotropy_i

class initialise_system_properties(object):
    #class to store the magnetic properties of each material type
    def __init__(self, temperature,dimensions_in_x,dimensions_in_y,dimensions_in_z):
        #Temperature
        self.temperature = temperature
        dimensions_in_x = dimensions_in_x
        dimensions_in_y = dimensions_in_y
        dimensions_in_z = dimensions_in_z

        create_lattice_structure()





natoms = dimx*dimy*dimz

cx = [0]*natoms
cy = [0]*natoms
cz = [0]*natoms

sx = [0]*natoms
sy = [0]*natoms
sz = [1]*natoms

iron = material_properties(1,1,1)
co = material_properties(2,2,2)



print(iron.mus)
