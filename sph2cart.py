import numpy as np
class sph2cart (object):
    def __init__ (self,az,el,r):
        self.az = az
        self.el = el
        self.r = r
        self.output = {}
    def convert (self):

        x = self.r *np.sin(self.el)* np.cos(self.az)
        y = self.r *np.sin(self.el) * np.sin(self.az)
        z = self.r * np.cos(self.el)
        self.output = [x, y, z]
        return self.output