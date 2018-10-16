from numpy import *
"""
initialConditions is an array with values at time t[0]
timeArray is an array containing all times on the form timeArray = linspace(t0,t1,dt)
f is a function that takes 
"""

m = 0.1 #kg - mass
k = 10 #N/m - spring constant
b = 0.1 #Ns/m - frictional coefficient

t0 = 0 # initial time
t1 = 10 # final time
def a(t,f):
    return (-b*v/m) + (-k*z/m)

t = linspace(0,10,10001)

values = rk4(t,a,array([0.1,0]))
def rk4(timeArray,f,initialConditions):
    values = initialConditions.resize(len(timeArray),len(initialConditions))
    timeStep = timeInterval[1] - timeInterval[0]
    
    # loop that iterates over the entire time interval
    # for each iteration RK4 is performed
    for i in range(N-1):
        v1 = v[i]
        z1 = z[i]
        t1 = t[i]
        a1 = a(v1,z1,t1)

        z2 = z1 + v1        *timeStep/2
        v2 = v1 + a1        *timeStep/2
        a2 = a(v2,z2,t1+timeStep/2)

        z3 = z1 + v2        *timeStep/2
        v3 = v1 + a2        *timeStep/2
        a3 = a(v3,z3,t1+timeStep/2)

        z4 = z1 + v3        *timeStep
        v4 = v1 + a3        *timeStep
        a4 = a(v4,z4,t1+timeStep)

        a_avg = (a1+2*a2+2*a3+a4)/6
        v_avg = (v1+2*v2+2*v3+v4)/6
        
        z[i+1] = z1 + v_avg*timeStep
        v[i+1] = v[i] + a_avg*timeStep
    return v, z