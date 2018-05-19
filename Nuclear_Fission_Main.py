import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import time
from mpl_toolkits.mplot3d import Axes3D

from determine_no_neutrons import determine_no_neutrons
from diffusionlengthrandom import diffusionlengthrandom
from fissioncheck import fissioncheck
from neutron import neutron
from sph2cart import sph2cart
import matplotlib

params = {
    'text.latex.preamble': ['\\usepackage{gensymb}'],
    'image.origin': 'lower',
    'image.interpolation': 'nearest',
    'image.cmap': 'gray',
    'axes.grid': False,
    'savefig.dpi': 150,  # to adjust notebook inline plot size
    'axes.labelsize': 8, # fontsize for x and y labels (was 10)
    'axes.titlesize': 8,
    'font.size': 8, # was 10
    'legend.fontsize': 6, # was 10
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'text.usetex': True,
    'figure.figsize': [5.0, 5.0],
    'font.family': 'serif',
}
matplotlib.rcParams.update(params)

start_time = time.time()
a = 0.017  # mean free path for collision
b = 0.21  # mean free path for spontaneous collision
index = 0
radius = 0.05
averagefissioneventsperradii = []
radiiarr = []
xarr = []
yarr = []
zarr = []
xtotalinitial = 0
ytotalinitial = 0
ztotalinitial = 0
xtotalfinal = 0
ytotalfinal = 0
ztotalfinal = 0
xarrfin = []
yarrfin = []
zarrfin = []
for j in range(0, 500):
    fission = 0
    diffusionlength = diffusionlengthrandom(random.random()).find_diffusion_len()
    # diffusionlength = np.sqrt(2 * a * b)
    for i in range(0, 100):
        numberofneutrons = determine_no_neutrons(random.random()).find_no_neutron()
        print(j, numberofneutrons)  # this is a debug thing lol
        if numberofneutrons < 1:
            continue
        random_direction = [random.random(), random.random(),
                            random.random()]  # random direction in x y z between 0 and 1
        azimuth_random = 2 * np.pi * random.random()
        elevation_random = np.arccos(1.0 - 2.0 * random.random())
        # elevation_random = np.arcsin(2.0 * random.random() - 1.0)
        radius_random = radius * np.cbrt(random.random())
        initialposition = sph2cart(azimuth_random, elevation_random,
                                   radius_random).convert()  # converted from spherical to cartesian x y z output
        finalposition = neutron(initialposition, diffusionlength, random_direction,
                                numberofneutrons).findfinalposition()  # finding final positions for neutrons
        fission = fissioncheck(finalposition, numberofneutrons, radius, fission).checkfission()
        xtotalinitial += initialposition[0]
        ytotalinitial += initialposition[1]
        ztotalinitial += initialposition[2]
    xarr.append(xtotalinitial / 100)
    yarr.append(ytotalinitial / 100)
    zarr.append(ztotalinitial / 100)
    averagefissioneventsperradii.append(fission / 100)
    radiiarr.append(radius)
    radius += 0.0011
print("My program took", time.time() - start_time, "to run")
sns.set_style("whitegrid")
plt.plot(radiiarr, averagefissioneventsperradii, sns.xkcd_rgb["pale red"], lw=1)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 0.6 * np.outer(np.cos(u), np.sin(v))
y = 0.6 * np.outer(np.sin(u), np.sin(v))
z = 0.6 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.scatter(xarr, yarr, zarr, c=xarr, marker='.', cmap='cool')
ax.scatter(xarrfin, yarrfin, zarrfin, c=xarrfin, marker='.', cmap='autumn')
ax.plot_wireframe(x, y, z, lw=0.1)
plt.show()
