import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap


# Define a function that creates two plots:
# (1) A scatter plot comparing x and y variables.
# (2) A scatter plot showing the difference between x and y.
def delta_met(data: pd.DataFrame, x_label: str, y_label: str, colorbar_label: str, x_limits: float, y_limits: float,
              file_name: str,
              dpi: int, colors=None, data_axis: str = 'default_data', x_axis: str = 'default_x',
              y_axis: str = 'default_y', color_axis: str = 'default_color', colorbar_limits=(4500, 6000)):
    """
    Arguments:

    data: The DataFrame containing the data.
    x_label, y_label, colorbar_label: Labels for the x-axis, y-axis, and colorbar.
    x_limits, y_limits: Limit values for the x and y axes.
    file_name: The filename for saving the output image.
    dpi: Resolution of the output figure.
    colors: Colormap to be used, either predefined or custom.
    data_axis, x_axis, y_axis, color_axis: Specify the data columns to use for the x, y, and color values.
    colorbar_limits: Define the minimum and maximum range for the colorbar.

    """
    # If 'colors' is provided as a string, we use it to select a predefined colormap.
    # Otherwise, we use a custom list of colors for the colormap.
    if isinstance(colors, str):
        ccmap = plt.get_cmap(colors)
    else:
        # If no colors are provided, we set a default custom color map.
        if colors is None:
            colors = ['#12355b', '#420039', '#d72638', '#ffffff', '#ff570a']
        ccmap = LinearSegmentedColormap.from_list("custom_cmap", colors)

    # Extract the data from the specified axis within the dataframe.
    # If no specific data axis is provided, the entire data is used.
    if data_axis != 'default_data':
        df_El = data[data_axis]
    else:
        df_El = data

    # Ensure that the x-axis, y-axis, and color-axis columns exist in the dataframe.
    # If not, raise an error.
    if x_axis not in df_El.columns or y_axis not in df_El.columns or color_axis not in df_El.columns:
        raise ValueError("Uma ou mais colunas especificadas não existem no dataframe!")

    # Extract values for x, y, and color from the dataframe.
    x = df_El[x_axis]
    y = df_El[y_axis]
    cor = df_El[color_axis]

    # Create the main figure and adjust subplot layout.
    plt.figure(1, figsize=(4, 4))
    plt.subplots_adjust(left=0.17, right=0.8, bottom=0.1, top=0.95, wspace=0.2, hspace=0.0)

    # Create the first plot: a scatter plot of x vs y.
    ax1 = plt.subplot2grid((4, 1), (0, 0), rowspan=3)
    scatter = ax1.scatter(x, y, marker='o', c=cor, vmin=colorbar_limits[0], vmax=colorbar_limits[1],
                          cmap=ccmap, edgecolor='k', alpha=0.9, s=20, linewidth=0.4)

    # Add a diagonal reference line where x = y (dashed black line).
    ax1.plot([x_limits[0], x_limits[1]], [x_limits[0], x_limits[1]], '--k', linewidth=0.4)

    # Set axis limits and labels.
    ax1.set_xlim(x_limits)
    ax1.set_ylim(y_limits)
    ax1.set_ylabel(y_label, fontsize=8)

    # Configure axis ticks and appearance.
    ax1.tick_params(axis='both', labelsize=8)
    ax1.tick_params(axis='both', left=True, top=True, right=True, bottom=True, labelleft=True, labeltop=False,
                    labelright=False, labelbottom=False)
    ax1.tick_params(axis='x', which='minor', top=True, direction='in', size=1, width=0.5)
    ax1.tick_params(axis='y', which='minor', right=True, direction='in', size=1, width=0.5)
    ax1.tick_params(axis='x', which='major', top=True, direction='in', size=2, width=0.5)
    ax1.tick_params(axis='y', which='major', right=True, direction='in', size=2, width=0.5)
    ax1.minorticks_on()

    # Create the second plot: a scatter plot of the difference (x - y) as a function of x.
    ax2 = plt.subplot2grid((4, 1), (3, 0))
    ax2.scatter(x, x - y, marker='o', c=cor, vmin=colorbar_limits[0], vmax=colorbar_limits[1],
                cmap=ccmap, edgecolor='k', alpha=0.9, s=20, linewidth=0.4)

    # Add a horizontal reference line at y = 0 (dashed black line).
    ax2.plot([x_limits[0], x_limits[1]], [0, 0], '--k', linewidth=0.4)

    # Set axis limits and labels for the second plot.
    ax2.set_xlim(x_limits)
    ax2.set_ylim(min(x - y) + min(x - y) * 0.2, max(x - y) + max(x - y) * 0.2)

    # Configure axis ticks and appearance for the second plot.
    ax2.tick_params(axis='y', which='both', left=False, labelleft=False)
    ax2.tick_params(axis='both', labelsize=8)
    ax2.set_xlabel(x_label, fontsize=8)
    ax2.set_ylabel(r'$\delta$($x-y$)', fontsize=8)

    # Add a text box in the second plot showing the mean and standard deviation of the differences.
    ax2.text(min(x_limits) - min(x_limits) * 0.1, max(x - y) - max(x - y) * 0.2,
             r'$\delta$ = ' + str(np.around(np.mean(x - y), 2)) + ' $\pm$ ' + str(np.around(np.std(x - y), 2)),
             fontsize=6)

    # Create and customize the colorbar.
    cax = plt.axes([0.82, 0.33, 0.03, 0.6])
    cbar = plt.colorbar(scatter, cax=cax)
    cbar.set_label(colorbar_label, fontsize=10)
    cbar.ax.tick_params(labelsize=6, size=2)

    # Add minor ticks to the second plot.
    ax2.tick_params(axis='both', left=True, top=True, right=True, bottom=True, labelleft=True, labeltop=False,
                    labelright=False, labelbottom=True)
    ax2.tick_params(axis='x', which='minor', top=True, direction='in', size=1, width=0.5)
    ax2.tick_params(axis='y', which='minor', right=True, direction='in', size=1, width=0.5)
    ax2.tick_params(axis='x', which='major', top=True, direction='in', size=2, width=0.5)
    ax2.tick_params(axis='y', which='major', right=True, direction='in', size=2, width=0.5)
    ax2.minorticks_on()

    # Save the figure as both .jpg and .pdf.
    plt.savefig(f'{file_name}.jpg', dpi=dpi)
    plt.savefig(f'{file_name}.pdf', dpi=dpi)
    plt.clf()


# Read data from an Excel file.
df = pd.read_excel(r"C:\Users\santo\Downloads\M67 paper II data d_new_31_05_2018_NoBE.xlsx",
                   sheet_name=None)

# Print the dataframe for debugging purposes.
print(df)

# Call the delta_met function to create the plots.
delta_met(
    data=df,
    x_label='[Mg/H] (This Work)',
    y_label='[Mg/H] (Syntspec DR17 NLTE)',
    colorbar_label='SNR',
    x_limits=(-.2, .2),
    y_limits=(-.2, .2),
    file_name='figure_delta_Mg_Thiswork_close',
    dpi=500,
    colors='viridis',
    data_axis='d_new_31_05_2018_NoBE',
    x_axis='Fe',  # Column for the x-axis
    y_axis='Mg',  # Column for the y-axis
    color_axis='SNR',  # Column for coloring the points
    colorbar_limits=(50, 200)
)

