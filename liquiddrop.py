import math

class _particle(object):
  def __init__(self, charge, mass):
    self.charge = charge
    self.mass = mass
    
class neutron(_particle):
  def __init__(self):
    _particle.__init__(self, 0, 939.573)
    
class proton(_particle):
  def __init__(self):
    _particle.__init__(self, 1, 938.280)

class hydrogen(_particle):
  def __init__(self):
    _particle.__init__(self, 0, 938.791)
    
class electron(_particle):
  def __init__(self):
    _particle.__init__(self, -1, 0.511)
    
  
#semi-empirical mass formula parameters.
a_v = 15.56
a_s = 17.23
a_c = 0.697
a_a = 23.285
a_p = 12.0

def isEven(num):
  if num%2==0: return True
  else: return False

def pairingTerm(Z,A):
  if isEven(Z) and isEven(A): return a_p / math.sqrt(A)
  if isEven(Z) == False and isEven(A) == False: return -1.0*a_p / math.sqrt(A)
  return 0
  
def bindingEnergy(Z,A):
    
  return a_v*A - a_s*math.pow(A, 2./3.) - a_c*math.pow(Z,2)/math.pow(A,1./3.) - a_a*math.pow((A - 2*Z), 2) / A + pairingTerm(Z,A)
  
def nuclearmass(Z,A):
  n = neutron()
  p = proton()
  return Z*p.mass + (A-Z)*n.mass - bindingEnergy(Z,A)
  
#
def atomicmass(Z,A):
  n = neutron()
  h = hydrogen()
  return Z*h.mass + (A-Z)*n.mass - bindingEnergy(Z,A)
  