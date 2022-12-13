import openmc
from openmc_csg_slice_plotter import plot_surface_slice

# 4 simple surfaces, names have been added to make them easy to identify
sphere1 = openmc.Sphere(r=10, name="sphere_r_10")
sphere2 = openmc.Sphere(r=20, name="sphere_r_20")
zplane = openmc.XPlane(x0=-5, name="zplane_z0_5")
zcylinder = openmc.ZCylinder(r=15, name="ZCylinder")

for view_direction in ['x', 'y', 'z']:

    plot = plot_surface_slice(
        view_direction=view_direction,
        surfaces=[sphere1, sphere2, zplane, zcylinder],
        plot_left=-100,
        plot_right=100,
        plot_top=100,
        plot_bottom=-100,
        slice_value=0,
        pixels=4000,
    )


    # plot.write_image is also an option but as the html has hovertext this is prefered
    plot.write_html(f'example_surface_plot_{view_direction}.html')

    # loads up the plot in a browser
    plot.show()
