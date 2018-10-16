from numpy import *
from matplotlib.pyplot import *

k = 1.0 # spring constant
m = 1.0 # spring mass



# timesteps, arrays and initial conditions
N = 1001
t = linspace(0,50,N)
dt = t[1] - t[0]
x = zeros(N)
v = zeros(N)
#a = zeros(N)
x[0] = 1
v[0] = 0
#a[0] = acc(x[0])

def vel(x): # hooks law
    return (-k*x/m)*dt

# Regular Euler. N needs to be really high to negate numerical error 
# Especially for large t1's the energy is not conserved at all
for i in range(N-1):
    v[i+1] = v[i] + vel(x[i])
    x[i+1] = x[i] + v[i]*dt
plot(t,x)
show()

# Euler Chromer (semi-implicit)
for i in range(N-1):
    v[i+1] = v[i] + vel(x[i])
    x[i+1] = x[i] + v[i+1]*dt # <--- only difference
plot(t,x)
show()

# Euler "midtpunktsmetode"
for i in range(N-1):
    v1 = v[i] + vel(x[i])
    v2 = v1
plot(t,x)
show()