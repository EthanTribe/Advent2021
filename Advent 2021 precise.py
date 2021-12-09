import timeit
start = timeit.default_timer()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


from datetime import date
day = 25#int(date.today().strftime('%d'))
print(day)

from decimal import * 
focusPointReal = Decimal('-0.743643887037158704752191506114774')
focusPointImag = Decimal('0.131825904205311970493132056385139')

imax = 100000

# define the function to iterate the Mbrot sequence
def inSet(c):               
    iterate = [Decimal(0), Decimal(0)]
    for i in range(imax):
        absIterate = (iterate[0]**2 + iterate[1]**2).sqrt()
        if absIterate > Decimal(2):
            return i
        else:
            newIterate = [Decimal(0), Decimal(0)]
            newIterate[0] = iterate[0]**2 - iterate[1]**2 + c[0]
            newIterate[1] = Decimal(2) * iterate[0] * iterate[1] + c[1]
            iterate = newIterate
    return imax

# set-up the array representing the complex plane
dim = 192#0*2
width = Decimal(10)**Decimal(-day)
xmin,xmax = focusPointReal-width, focusPointReal+width
ymin,ymax = focusPointImag-width*Decimal(9/16), focusPointImag+width*Decimal(9/16)
xStep = (xmax - xmin) / (Decimal(dim)-1)
xList = [xmin + Decimal(i) * xStep for i in range(dim)]
yStep = (ymax - ymin) / (Decimal(dim*9/16)-1)
yList = [ymin + Decimal(i) * yStep for i in range(dim*9//16)]

points = np.zeros((len(yList),len(xList)))
for i in range(len(xList)-1,-1,-1):
    for j in range(len(yList)):
        pointIn = inSet([xList[i],yList[j]])
        points[j,i] = pointIn

plt.ion()
fig = plt.figure()
fig.set_size_inches((1.6,.9))
ax =  plt.Axes(fig, [0.,0.,1.,1.])
ax.set_axis_off();
fig.add_axes(ax)

power = 1
cmaps = [cm.magma, cm.magma_r, cm.viridis, cm.viridis_r, cm.plasma, cm.plasma_r, cm.inferno, cm.inferno_r, cm.cividis, cm.cividis_r, cm.RdYlBu, cm.RdYlBu_r, cm.RdYlGn, cm.RdYlGn_r, cm.Spectral, cm.Spectral_r, cm.ocean, cm.ocean_r, cm.gist_earth, cm.gist_earth_r, cm.terrain, cm.terrain_r, cm.gnuplot, cm.gnuplot_r, cm.gnuplot2, cm.gnuplot2_r, cm.CMRmap, cm.CMRmap_r, cm.cubehelix, cm.cubehelix_r, cm.rainbow, cm.rainbow_r]
cmapsOrder = [28, 17, 15,  2,  7, 21,  4,  6, 27, 11, 26, 16, 24, 31,  8, 23, 19, 22,  1,  3,  9, 29, 30, 14, 10, 13, 18, 20, 25,  5,  0, 12]
print("Using colour map " + cmaps[cmapsOrder[day]].name + ".")
cax = ax.matshow(points**power, cmap=cmaps[cmapsOrder[day]], origin='lower')#np.random.choice(cmaps,1)[0]
plt.axis('off')
plt.savefig('Adventttttt{}.jpg'.format(day),format='jpg',dpi=2400)


stop = timeit.default_timer()
print('Time: ', stop - start) 