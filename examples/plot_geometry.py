import openmc
from openmc_csg_slice_plotter import plot_geometry_slice

# surfaces
central_sol_surface = openmc.ZCylinder(r=100, name='central_sol_surface')
central_shield_outer_surface = openmc.ZCylinder(r=140, name='central_shield_outer_surface')
vessel_inner_surface = openmc.Sphere(r=500, name='vessel_inner_surface')
first_wall_outer_surface = openmc.Sphere(r=540, name='first_wall_outer_surface')
breeder_blanket_outer_surface = openmc.Sphere(r=610, boundary_type='vacuum', name='breeder_blanket_outer_surface')

# regions
central_sol_region = -central_sol_surface & -breeder_blanket_outer_surface
central_shield_region = +central_sol_surface & -central_shield_outer_surface & -breeder_blanket_outer_surface
first_wall_region = -first_wall_outer_surface & +vessel_inner_surface
inner_vessel_region = -vessel_inner_surface & +central_shield_outer_surface
breeder_blanket_region = +first_wall_outer_surface & -breeder_blanket_outer_surface & +central_shield_outer_surface

# cells
central_sol_cell = openmc.Cell(region=central_sol_region)
central_shield_cell = openmc.Cell(region=central_shield_region)
inner_vessel_cell = openmc.Cell(region=inner_vessel_region)
first_wall_cell = openmc.Cell(region=first_wall_region)
breeder_blanket_cell = openmc.Cell(region=breeder_blanket_region)

universe = openmc.Universe(cells=[central_sol_cell, central_shield_cell, inner_vessel_cell, first_wall_cell, breeder_blanket_cell])
my_geometry = openmc.Geometry(universe)


for view_direction in ['x', 'y', 'z']:

    plot = plot_geometry_slice(
        view_direction=view_direction,
        geometry=my_geometry,
        plot_left=-700,
        plot_right=700,
        plot_top=700,
        plot_bottom=-700,
        slice_value=0,
        pixels=4000,
    )


    # plot.write_image is also an option but as the html has hovertext this is prefered
    plot.write_html(f'example_geometry_plot_{view_direction}.html')

    # loads up the plot in a browser
    plot.show()
