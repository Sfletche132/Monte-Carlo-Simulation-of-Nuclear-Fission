import numpy as np
class cart2sph (object):
    def __init__ (self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.output = {}
    def convert (self):
        hxy = np.hypot(self.x, self.y)
        r = np.hypot(hxy, self.z)
        el = np.arctan2(self.z, hxy)
        az = np.arctan2(self.y, self.x)
        self.output = [az, el, r]
        return self.output