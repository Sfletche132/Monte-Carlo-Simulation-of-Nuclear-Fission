import numpy as np
from scipy.integrate import quad
class diffusionlengthrandom(object):
    def __init__(self,randomnumber):
        self.random_number = randomnumber
        self.diffusionlengthrandom = 0
    def find_diffusion_len(self):
        integrand = 0
        i = 0
        a = 0.017  # mean free path for collision
        b = 0.21  # mean free path for spontaneous collision
        while True:
            attncoeff = 1 / np.absolute(integrand - self.random_number)
            scalefac = np.exp(-attncoeff)
            if scalefac < 0.01 :
                scalefac = 0.01
            integrand , err = quad(lambda x: x*np.exp(-x), 0, i)
            absvalue = np.absolute(integrand - self.random_number)
            if absvalue < 0.01:
                break
            i = i + scalefac
        self.diffusionlengthrandom = np.sqrt(2 * a * b) * integrand
        return self.diffusionlengthrandom