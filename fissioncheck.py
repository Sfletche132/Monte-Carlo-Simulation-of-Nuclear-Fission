import numpy as np
class fissioncheck(object):
    def __init__(self,position,numberofneutrons,radiusofsphere,fission):
        self.position = position
        self.numberofneutrons = numberofneutrons
        self.sphereradius = radiusofsphere
        self.fission = fission
    def checkfission(self):
        for i in range(0,self.numberofneutrons):
            x = self.position [i] [0]
            y = self.position [i] [1]
            z = self.position [i] [2]
            hxy = np.hypot(x, y)
            radius_diffusedneutron = np.hypot(hxy, z)
            if radius_diffusedneutron >=0 and radius_diffusedneutron <= self.sphereradius :
                self.fission += 1
        return self.fission