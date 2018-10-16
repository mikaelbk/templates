from __future__ import division
from matplotlib.pyplot import *
from numpy import *

#Fysiske konstanter
ke=8.9875517873681764*10**9 #Coulomb's constant in Nm²/C²
G=6.67408*10**-11#Gravitational constant
h=6.626070040*10**34 #Planck's constant in Js
hbar=1.054571800*10**-34#h-bar
e=1.6021766208*10**-19#Elementary charge in Coulomb
c=299792458#Exact speed of light in vacuum
u=1.660539040*10**-27#Atomic mass unit in kg
me=9.10938215*10**-31#Electronic mass in kg
μ0=4*pi*10**-7#vacuum permeability
R=1.0967757*10**7
NA=6.022140857*10**23#Avogadro constant in 1/mol
ε0=1/(μ0*c**2)#vacuum permittivity
a0=hbar**2/(me*ke*(e**2))#Bhorradien

def euler(r0, v0, t0, t1, dt, a_r):
    # number of steps
    N = int((t1-t0)/dt)

    # creating arrays
    t = linspace(t0, t1, N)
    r = zeros((N,3))
    v = zeros((N,3))

    r[0] = r0
    v[0] = v0
    for i in range(N-1):
        r[i+1] = r[i] + v[i]*dt
        dis = linalg.norm(r[i+1]) # |r|, distance
        a = a_r(dis)*r[i+1]/dis
        v[i+1] = v[i] + v[i]*dt
    return t, r, v

#jordas startposisjon i 3-dimensjoner (x0,y0,z0) den 29 october
x0 = 1.217028542396214E+11
y0 = 8.567168551533313E+10
z0 = -2.309376537841951E+07
#jordas starthastighet i 3 dimensjoner (vx0,vy0,vz0) den 29 october
vx0 = -1.769518806056676E+04
vy0 = 2.421094267101882E+04
vz0 = -1.125332356349184

m_s = 1.98855E+30 # sunmass
m_m = 7.34767309*10**22# moonmass
m_e = 5.972*10**24# earthmass
r_e = 1.47098074*10**11# orbital radius
v_e = 30300 # 
tstart = 0 #
tfinal = 60*60*24*365 # seconds
dt = 60*60

#acceleration on a body subject to the gravitational force of the sun
def newtons_law(r):
    return (G*m_s)/(r**2)

t, r, v = euler([x0,y0,z0],[vx0,vy0,vz0],tstart,tfinal,dt,newtons_law)
plot(r[0],r[1])
show()