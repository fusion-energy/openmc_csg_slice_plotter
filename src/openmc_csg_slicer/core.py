import plotly.graph_objects as go
import numpy as np
import math


def check_for_inf_value(var_name, view_direction):
    if np.isinf(var_name):
        print(f'view direction {view_direction}\n')
        msg = f"{var_name} can't be obtained from the bounding box as boundary is at inf. {var_name} value must be specified by user"
        
        raise ValueError(msg)

def plot_geometry_slice(
    geometry,
    view_direction="x",
    plot_left=None,
    plot_right=None,
    plot_top=None,
    plot_bottom=None,
    slice_value=None,
    pixels=1000,
):
    surfaces = get_all_surfaces(geometry_or_surfaces)
    bb = geometry.bounding_box

    if view_direction == "x":
        # need plot_left, plot_right, plot_top, plot_bottom

        if plot_left is None:
            plot_left = bb[0][1]
            check_for_inf_value(plot_left, view_direction)

        if plot_right is None:
            plot_right = bb[1][1]
            check_for_inf_value(plot_right, view_direction)

        if plot_top is None:
            plot_top = bb[1][2]
            check_for_inf_value(plot_top, view_direction)

        if plot_bottom is None:
            plot_bottom = bb[0][2]
            check_for_inf_value(plot_bottom, view_direction)

        if slice_value is None:
            slice_value = (bb[0][0] + bb[1][0]) / 2
            check_for_inf_value(slice_value, view_direction)

        xlabel = "Y [cm]"
        ylabel = "Z [cm]"

    if view_direction == "y":
        # need plot_left, plot_right, plot_top, plot_bottom

        if plot_left is None:
            plot_left = bb[0][0]
            check_for_inf_value(plot_left, view_direction)

        if plot_right is None:
            plot_right = bb[1][0]
            check_for_inf_value(plot_right, view_direction)

        if plot_top is None:
            plot_top = bb[1][2]
            check_for_inf_value(plot_top, view_direction)

        if plot_bottom is None:
            plot_bottom = bb[0][2]
            check_for_inf_value(plot_bottom, view_direction)

        if slice_value is None:
            slice_value = (bb[0][1] + bb[1][1]) / 2
            check_for_inf_value(slice_value, view_direction)

        xlabel = "X [cm]"
        ylabel = "Z [cm]"

    if view_direction == "z":
        # need plot_left, plot_right, plot_top, plot_bottom

        if plot_left is None:
            plot_left = bb[0][0]
            check_for_inf_value(plot_left, view_direction)

        if plot_right is None:
            plot_right = bb[1][0]
            check_for_inf_value(plot_right, view_direction)

        if plot_top is None:
            plot_top = bb[1][1]
            check_for_inf_value(plot_top, view_direction)

        if plot_bottom is None:
            plot_bottom = bb[0][1]
            check_for_inf_value(plot_bottom, view_direction)

        if slice_value is None:
            slice_value = (bb[0][2] + bb[1][2]) / 2
            check_for_inf_value(slice_value, view_direction)

        xlabel = "X [cm]"
        ylabel = "Y [cm]"

    else:
        raise ValueError("supported view_directions 'x', 'y' or 'z'")
    
    plot_surfaces_slice(
        view_direction=view_direction,
        plot_left=plot_left,
        plot_right=plot_right,
        plot_top=plot_top,
        plot_bottom=plot_bottom,
        slice_value=slice_value,
        pixels=pixels
    )

def plot_surfaces_slice(
    surfaces,
    view_direction="x",
    plot_left=None,
    plot_right=None,
    plot_top=None,
    plot_bottom=None,
    slice_value=None,
    pixels=1000,
)
    """Accepts a CSG surface and returns a"""

    if isinstance(geometry_or_surfaces, openmc.Geometry()):

        
    


    if view_direction == "x":
        # need plot_left, plot_right, plot_top, plot_bottom

        xlabel = "Y [cm]"
        ylabel = "Z [cm]"

    if view_direction == "y":
        # need plot_left, plot_right, plot_top, plot_bottom
        xlabel = "X [cm]"
        ylabel = "Z [cm]"

    if view_direction == "z":
        # need plot_left, plot_right, plot_top, plot_bottom

        xlabel = "X [cm]"
        ylabel = "Y [cm]"

    else:
        raise ValueError("supported view_directions 'x', 'y' or 'z'")

    plot_width = abs(plot_left - plot_right)
    plot_height = abs(plot_bottom - plot_top)
    aspect_ratio = plot_height / plot_width

    numerator = math.sqrt(4 * aspect_ratio * pixels)
    denominator = 2 * aspect_ratio

    pixels_across = numerator / denominator
    pixels_up = int(pixels / pixels_across)
    pixels_across = int(pixels_across)

    fig = go.Figure()

    for surface in surfaces:
        results_on_grid = []
        for y in np.linspace(plot_top, plot_bottom, pixels_across):
            grid_row = []
            for x in np.linspace(plot_left, plot_right, pixels_up):
                if view_direction == "z":
                    grid_row.append(surface.evaluate((x, y, slice_value)))
                if view_direction == "x":
                    grid_row.append(surface.evaluate((slice_value, x, y)))
                if view_direction == "y":
                    grid_row.append(surface.evaluate((x, slice_value, y)))

            results_on_grid.append(grid_row)
        
        rand_c = np.random.rand(3,)
        color = f"rgb{rand_c[0],rand_c[1],rand_c[2]}"
        print(color)
        # color="rgb(0,0,0)"
        fig.add_trace(
            go.Contour(
                z=results_on_grid,
                ncontours=1,
                contours_coloring="lines",
                line_width=2,
                x0=plot_left,
                dx=abs(plot_left - plot_right) / (len(results_on_grid[0]) - 1),
                y0=plot_bottom,
                dy=abs(plot_bottom - plot_top) / (len(results_on_grid) - 1),
                colorscale=[[0, color], [1, color]],
                name=f"ID={surface.id} Name={surface.name}",
                contours={"value": 0},
                texttemplate="ds",
                hoverinfo="all",
                showlegend =True
                # colorscale =[[0,]]
            )
        )
        print(surface.name)

    fig.update_traces(line={"color": "rgb(0,0,0)"})
    fig.update_layout(
        xaxis={"title": x_label},
        yaxis={"title": y_label},
        autosize=False,
        height=800,

        # showlegend=True,
    )
    fig.update_yaxes(
        scaleanchor="x",
        scaleratio=1,
    )
    fig.show()



import openmc

sphere1 = openmc.Sphere(r=10, name="sphere_r_10")
sphere2 = openmc.Sphere(r=20, name="sphere_r_20")
zplane = openmc.XPlane(x0=-5, name="zplane_z0_5")
xcy = openmc.ZCylinder(r=15, name="ZCylinder")



plot_axis_slice(surfaces=[sphere1, sphere2, zplane, xcy])

