#https://docs.scipy.org/doc/scipy/reference/constants.html
from scipy import constants

#basic constants can be retrieved directly (see link for list)
c = constants.c
mu_0 = constants.mu_0

#special constants can be found
print(constants.find("light")) #>>['speed of light in vacuum']
c = constants.physical_constants["speed of light in vacuum"]

print(constants.find("proton"))
proton_mass = constants.physical_constants["proton mass"]
print(proton_mass)