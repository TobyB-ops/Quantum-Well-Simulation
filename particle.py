class particle:
    
    def __init__(self, mass, charge):
        
        self.mass = mass
        self.charge = charge
        
class Hamiltonian:
    def __init__(self, particle, potential):
        ....
        
    def UpdatePotential(self, t):
        potential.GetPotential(t)
        
        
electron = particle(m, c)
hamiltonian(electron, "HarmonicOscillator")
       
class HarmonicOscillator:
    def __init__(self, mass, omega, x, center = 0):
        self.mass = mass
        self.omega = omega
        self.x = x
        self.center = center
        
    def GetPotential(self):
        return 1/2 * self.mass * self.omega**2 * (self.x - self.center) **2
    

        