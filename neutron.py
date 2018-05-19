import numpy as np
class neutron (object):

    #Position in 3D space , both starting and ending , this can then be checked
    # in the main for whether inside the sphere or not
    # direction of travel is randomly assigned


    def __init__(self, initial_position, diffusion_length, direction, numberofneutrons):

        self.direction =  direction #array for direction of neutron travel (x y z)

        self.diffusion_length = diffusion_length

        self.initialposition = initial_position # position (x y z)

        self.final_position = []

        self.numberofneutrons = numberofneutrons

    def findfinalposition(self):
        for i in range(0,self.numberofneutrons):
            self.final_position.append([])
            for j in range (0,3):
                if self.direction[j] >= 0.5:
                    self.final_position[i].append(self.initialposition[j] + self.diffusion_length)
                else:
                    self.final_position[i].append(self.initialposition[j] - self.diffusion_length)
        return self.final_position