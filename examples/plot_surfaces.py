import openmc
from openmc_csg_slicer import plot_axis_slice

sphere1 = openmc.Sphere(r=10, name="sphere_r_10")
sphere2 = openmc.Sphere(r=20, name="sphere_r_20")
zplane = openmc.XPlane(x0=-5, name="zplane_z0_5")
xcy = openmc.ZCylinder(r=15, name="ZCylinder")

plot_axis_slice(surfaces=[sphere1, sphere2, zplane, xcy])
