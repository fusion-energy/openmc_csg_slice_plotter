import openmc
from openmc_csg_slice_plotter import plot_geometry_slice

# surfaces
inner_wall_surface = openmc.ZCylinder(r=80, name='inner_wall_surface')
outer_wall_surface = openmc.ZCylinder(r=120, name='outer_wall_surface')
lid_upper_surface = openmc.ZPlane(z0=160, name='lid_upper_surface')
lid_lower_surface = openmc.ZPlane(z0=120, name='lid_lower_surface')
base_upper_surface = openmc.ZPlane(z0=40, name='base_upper_surface')
base_lower_surface = openmc.ZPlane(z0=0, name='base_lower_surface')


# regions
wall_region = -outer_wall_surface & +inner_wall_surface & -lid_lower_surface & +base_upper_surface
lid_region = -outer_wall_surface & -lid_upper_surface & +lid_lower_surface
base_region = -outer_wall_surface & -base_upper_surface & +base_lower_surface

# cells
wall_cell = openmc.Cell(region=wall_region)
lid_cell = openmc.Cell(region=lid_region)
base_cell = openmc.Cell(region=base_region)


universe = openmc.Universe(cells=[wall_cell, lid_cell, base_cell])
my_geometry = openmc.Geometry(universe)


for view_direction in ['x', 'y', 'z']:

    plot = plot_geometry_slice(
        view_direction=view_direction,
        geometry=my_geometry,
        slice_value=0,
        pixels=80000
    )


    # plot.write_image is also an option but as the html has hovertext this is prefered
    plot.write_html(f'example_geometry_plot_2_{view_direction}.html')

    # loads up the plot in a browser
    plot.show()
