from scipy.integrate import quad
import numpy as np
class determine_no_neutrons(object):
    def __init__(self,random):
        self.random_number = random
        self.neutronnumber = 0
    def find_no_neutron(self):
        integrand = 0
        i = 0
        while True:
            attncoeff = 1 / np.absolute(integrand - self.random_number)
            scalefac = np.exp(-attncoeff)
            if scalefac < 0.01 :
                scalefac = 0.01
            integrand, err = quad(lambda x: x*np.exp(-x), 0, i)
            absvalue = np.absolute(integrand - self.random_number)
            if absvalue < 0.01:
                break
            i = i + scalefac
        self.neutronnumber = int(i)
        return self.neutronnumber