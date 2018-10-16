from numpy import *
from matplotlib.pyplot import *

# defining some physical constants and other variables
G = 6.67408*10**-11#Gravitational constant
m_s = 1.98855E+30 # sunmass
AU = 1.496E+11 # one astronomical unit in meters
"""
m_m = 7.34767309*10**22# moonmass
m_e = 5.972*10**24# earthmass
r_e = 1.47098074*10**11# average orbital radius
v_e = 30300 #average orbital velocity
"""
tstart = 0 # start time
tfinal = 60*60*24*365 # end time
dt = 60*60 # timestep
N = int((tfinal - tstart)/dt) #number of iterations

#Initial conditions in for position(m) and velocity(m/s), 2017-01-24
# Source: http://ssd.jpl.nasa.gov/horizons.cgi
rx0 = -8.174362383830018E+010
ry0 = 1.227724665696847E+011
rz0 = -2.780267353618890E+07

vx0 = -2.521205039324612E+04
vy0 = -1.673375943691125E+04
vz0 = 1.154436333028031

t = linspace(tstart,tfinal,N+1) # defining the time array
r = zeros([N+1,3]) # array of positional vectors (N+1 x 3 matrix) where element r[i] gives the position in three dimensions at time t[i]
v = zeros([N+1,3]) # velocities are stored in same format as position
r[0] = [rx0,ry0,rz0] # assigns initial conditions for first array element
v[0] = [vx0,vy0,vz0]

# function that returns absolute value of gravitational acceleration caused by the sun at a distance r
def gAcc(r):
    return G*m_s/r**2

# simple eulers method
for i in range(len(t)-1):
    r[i+1] = r[i] + v[i]*dt
    dis = linalg.norm(r[i+1]) # distance from the sun, |r|
    a = -1* gAcc(dis) * (r[i+1]/dis) # a = -g(r/|r|), where r is a vector
    v[i+1] = v[i] + a*dt

plot(r[::,0], r[::,1]) #plots rx vs ry
show()