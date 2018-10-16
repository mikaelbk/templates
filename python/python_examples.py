from matplotlib.pyplot import *
from numpy import *

#numpy array creation--------------------------------------------------
thetaS = 0
thetaF = 2*pi
N = 100

theta = linspace(thetaS,thetaF,N)
sine = sin(theta)
cosine = cos(theta)

#plotting--------------------------------------------------
plot(theta,sine,label = "$sin(\\theta)$")
plot(theta,cosine, label = "$cos(\\theta)$")
xlabel("$\\theta$")
title("Trigonometric functions")
legend()
#savefig("trigonometric_functions.pdf")
show()

#writing to file
"""
with open("trig.txt","w") as fil: #the "with" keyword makes sure the file is closed when the loop is done
    for line in fil:
        a,b = [float(tall) for tall in line.split(" ")]
        qa.append(a)
        P_qa.append(b/100)
"""

#saving/load npz--------------------------------------------------
savez("trig", theta = theta, sine = sine, cosine = cosine)
npzfile = load("trig.npz")
theta = npzfile["theta"]