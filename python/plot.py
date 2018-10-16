from numpy import *
from matplotlib.pyplot import *
#figure(figsize = (6,5))
rc('text', usetex = True)

x = linspace(0,4*pi,1000)
sine = sin(x)
cosine = cos(x)

subplot(211)
plot(x,sine,label = '$\sin x$')
plot(x,cosine,label = '$\cos x$')
title('$\\sin(x)$ and $\\cos(x)$')
xlabel('x')
ylim(-1.1,1.1)
legend(loc = 'lower center')

subplot(212)
plot(x,cosine+0.5*sin(4*x),'r')
title('$\\cos x + 0.5\\sin x$')
xlabel('x')

tight_layout()
show()

""" colormap
imshow([nested list])
colorbar()
"""