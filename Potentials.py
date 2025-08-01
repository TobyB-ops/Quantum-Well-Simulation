import numpy as np


#i think x should be passed in GetPotential() rather than the initialisation function of each potential class - tom


class HarmonicOscillator:
    def __init__(self, mass, width, x, omega, center):
        self.mass = mass                
        self.width = width
        self.x = x
        self.omega = omega
        self.center = center
    def GetPotential(self):
        return 1/2 * self.mass * self.omega**2 * (self. x - self.center)**2
    def GroundStateEnergy(self):
        hbar = 6.63e-34/(2 * np.pi)
        return 0.5 * hbar * self.omega
    
class FreeParticle:
    def __init__(self, x, mass, momentum):
        self.x = x
        self.mass = mass
        self.momentum = momentum
        
    def GetPotential(self):
        return np.zeros(self.x.shape)
    
    def GroundStateEnergy(self):
        return self.momentum**2 / (2 * self.mass)
    
class InfinitePotentialWell:
    def __init__(self, mass, width, x,  xmin = 0):
        self.xmin = xmin
        self.mass = mass
        self.width = width
        self.x = x
        
    def GetPotential(self):
        xmax = self.xmin + self.width
        return np.where((self.x < self.xmin) | (self.x > xmax), 1e-5, 0)
    
    def GroundStateEnergy(self):
        h = 6.63e-34
        return h*2/(8 * self.mass * self.width**2 )
    
class FinitePotentialWell:
    def __init__(self, mass, width, x, xmin = 0, v0=1e-18):
        
        self.xmin = xmin
        self.mass = mass
        self.width = width
        self.v0 = v0
        self.x = x
              
    def GetPotential(self):
        xmax = self.xmin + self.width
        print(xmax)
        return np.where((self.x < self.xmin) | (self.x > xmax), self.v0, 0)
    
    def GroundStateEnergy(self):
        h = 6.63e-34
        return h*2/(8 * self.mass * self.width**2 )

class ColoumbPotential:
    def __init__(self, mass, width, x, xmin1, xmin2, v0):
        self.mass = mass                
        self.width = width
        self.x = x
    def GetPotential(self):
        eps = 8.85e-12
        e = 1.60e-19
        return -e**2 / (4 * np.pi * eps * self.x)
    def GroundStateEnergy(): 
        return 13.6 * 1.6e-19
    
class DoublePotentialWell:
    def __init__(self, mass, width, x, xmin1, xmin2, v0):
        self.mass = mass
        self.width = width
        self.x = x
        self.xmin1 = xmin1
        self.xmin2 = xmin2
        self.v0 = v0

    def GetPotential(self):
        xmax1 = self.xmin1 + self.width
        xmax2 = self.xmin2 + self.width
        return np.where(
            ((self.x >= self.xmin1) & (self.x <= xmax1)) | 
            ((self.x >= self.xmin2) & (self.x <= xmax2)),
            0,  # Inside wells
            self.v0  # Outside wells
        )
        

    
    
        '''
    def HarmonicOscillator(self, omega, center = 0):
        """
        mass - kg
        omega - Hz
        x - m
        center - m

        For a given mass and angular frequency determine the potential at a point x
        """
        return 1/2 * self.mass * omega **2 * (center - self.x)**2
        

    def InfinitePotentialWell(self, xmin = 0,):

        xmax = xmin + self.width

        return np.where((self.x < xmin) | (self.x > xmax), np.inf, 0)

    def FinitePotentialWell(self, xmin = 0, v0=1e-18):


        xmax = xmin + self.width

        return np.where((self.x < xmin) | (self.x > xmax), v0, 0)

    def ColoumbPotential(self):
        
        v(r) = -e^2/4 pi E_0 x  1D
        
        eps = 8.85e-12
        e = 1.60e-19
        return -e**2 / (4 * np.pi * eps * self.x)
       
    def DoublePotentialWell( self, xmin1=0, xmin2=1e-9, v0=1e-18):
        """
        Defines two finite potential wells at positions xmin1 and xmin2.

        - mass: mass of the particle (kg)
        - width: width of each well (m)
        - x: position array (m)
        - xmin1: starting position of the first well (m)
        - xmin2: starting position of the second well (m)
        - v0: potential outside the wells (J)
        """
        xmax1 = xmin1 + self.width
        xmax2 = xmin2 + self.width

        return np.where(
            ((self.x >= xmin1) & (self.x <= xmax1)) | ((self.x >= xmin2) & (self.x <= xmax2)), 
            0,  # Inside wells: V = 0
            v0  # Outside wells: V = v0
        )
        '''