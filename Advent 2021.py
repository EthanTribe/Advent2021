import timeit
start = timeit.default_timer()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


from datetime import date
day = int(date.today().strftime('%d'))
print(day)
focusPoint = complex(-0.743643887037158704752191506114774, 0.131825904205311970493132056385139)#[Decimal('-0.743643887037158704752191506114774'), Decimal('0.131825904205311970493132056385139')]

imax = 2000

# define the function to iterate the Mbrot sequence
def inSet(c):                           
    iterate = 0
    for i in range(imax):
        if abs(iterate) > 2:
            return i
        else:
            iterate = iterate**2 + c
    return imax
# takes ~0.0003s per 1000 iterations
# so 40mins if 4HD and all 1000

# set-up the array representing the complex plane
dim = 19*2
width = 10**(-day)
xmin,xmax = focusPoint.real-width, focusPoint.real+width
ymin,ymax = focusPoint.imag-width*9/16, focusPoint.imag+width*9/16
xList = np.linspace(xmin,xmax,dim)
yList = np.linspace(ymin,ymax,int(dim*9/16))
points = np.zeros((len(yList),len(xList)))
lastPause = start
percentageRowsDoneCounter = 0
for i in range(len(xList)-1,-1,-1):
    percentageRowsDone = 100 - 100 * i / dim
    if percentageRowsDone > percentageRowsDoneCounter + 1:
        percentageRowsDoneCounter += 1
        pause = timeit.default_timer()
        print("This first ", round(100 - 100 * i / dim, 1), "% took ", round((pause - start) / 60, 1), " minutes, and ", round((pause - lastPause) / 60, 2), " minutes since the last check.")
        lastPause = pause
    for j in range(len(yList)):
        pointIn = inSet(complex(xList[i],yList[j]))
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
cax = ax.matshow(points**power, cmap=cmaps[cmapsOrder[day]], origin='lower')#, extent=(xmin,xmax,ymin,ymax)
plt.axis('off')
plt.savefig('Advent{} ({}).jpg'.format(day, imax),format='jpg',dpi=2400)

print("Mean: ", round(np.average(points)))
print("Median: ", round(np.median(points)))
numImax = len(np.where(points==imax)[0])
print("Percent imax: ", round(numImax * 100 / (len(points) * len(points[0])), 1))


stop = timeit.default_timer()
print('Time: ', round((stop - start)/60, 1), " minutes") 