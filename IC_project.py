import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap


def delta_met(data: pd.DataFrame, x_label: str, y_label: str, colorbar_label: str, x_limits: float, y_limits: float, file_name: str,
              dpi: int, colors=None, x_axis: str = 'default_x', y_axis: str = 'default_y', color_axis: str = 'default_color', colorbar_limits=(4500, 6000)):

    if isinstance(colors, str):
        ccmap = plt.get_cmap(colors)
    else:
        if colors is None:
            colors = ['#12355b', '#420039', '#d72638', '#ffffff', '#ff570a']
        ccmap = LinearSegmentedColormap.from_list("custom_cmap", colors)


    df_El = data['Mg_trends'][0]

    x = df_El[x_axis]
    y = df_El[y_axis]
    cor = df_El[color_axis]


    plt.figure(1, figsize=(4, 4))
    plt.subplots_adjust(left=0.17, right=0.8, bottom=0.1, top=0.95, wspace=0.2, hspace=0.0)

    ax1 = plt.subplot2grid((4, 1), (0, 0), rowspan=3)
    scatter = ax1.scatter(x, y, marker='o', c=cor, vmin=colorbar_limits[0], vmax=colorbar_limits[1],
                          cmap=ccmap, edgecolor='k', alpha=0.9, s=20, linewidth=0.4)

    ax1.plot([x_limits[0], x_limits[1]], [x_limits[0], x_limits[1]], '--k', linewidth=0.4)

    ax1.set_xlim(x_limits)
    ax1.set_ylim(y_limits)
    ax1.set_ylabel(y_label, fontsize=8)
    ax1.tick_params(axis='both', labelsize=8)  # Set font size for x-axis

    ax1.tick_params(axis='both', left=True, top=True, right=True, bottom=True, labelleft=True, labeltop=False,
                    labelright=False, labelbottom=False)

    ax1.tick_params(axis='x', which='minor', top=True, direction='in', size=1, width=0.5)
    ax1.tick_params(axis='y', which='minor', right=True, direction='in', size=1, width=0.5)
    ax1.tick_params(axis='x', which='major', top=True, direction='in', size=2, width=0.5)
    ax1.tick_params(axis='y', which='major', right=True, direction='in', size=2, width=0.5)
    ax1.minorticks_on()

    ax2 = plt.subplot2grid((4, 1), (3, 0))
    ax2.scatter(x, x - y, marker='o', c=cor, vmin=colorbar_limits[0], vmax=colorbar_limits[1],
                cmap=ccmap, edgecolor='k', alpha=0.9, s=20, linewidth=0.4)

    ax2.plot([x_limits[0], x_limits[1]], [0, 0], '--k', linewidth=0.4)

    ax2.set_xlim(x_limits)
    ax2.set_ylim(min(x - y) + min(x - y) * 0.2, max(x - y) + max(x - y) * 0.2)

    ax2.tick_params(axis='y', which='both', left=False, labelleft=False)
    ax2.tick_params(axis='both', labelsize=8)  # Set font size for both x and y axes

    ax2.set_xlabel(x_label, fontsize=8)
    ax2.set_ylabel(r'$\delta$($x-y$)', fontsize=8)
    ax2.text(min(x_limits) - min(x_limits) * 0.1, max(x - y) - max(x - y) * 0.2,
             r'$\delta$ = ' + str(np.around(np.mean(x - y), 2)) + ' $\pm$ ' + str(np.around(np.std(x - y), 2)),
             fontsize=6)

    cax = plt.axes([0.82, 0.33, 0.03, 0.6])
    cbar = plt.colorbar(scatter, cax=cax)
    cbar.set_label(colorbar_label, fontsize=10)
    cbar.ax.tick_params(labelsize=6, size=2)

    ax2.tick_params(axis='both', left=True, top=True, right=True, bottom=True, labelleft=True, labeltop=False,
                    labelright=False, labelbottom=True)

    ax2.tick_params(axis='x', which='minor', top=True, direction='in', size=1, width=0.5)
    ax2.tick_params(axis='y', which='minor', right=True, direction='in', size=1, width=0.5)
    ax2.tick_params(axis='x', which='major', top=True, direction='in', size=2, width=0.5)
    ax2.tick_params(axis='y', which='major', right=True, direction='in', size=2, width=0.5)
    ax2.minorticks_on()

    plt.savefig(f'{file_name}.jpg', dpi=dpi)
    plt.savefig(f'{file_name}.pdf', dpi=dpi)
    plt.clf()


####### DADOS ALEATÓRIOS PARA TESTE #######
np.random.seed(42)
num_points = 100
data = {
    'Mg_trends': [{
        'Mg': np.random.uniform(-0.1,0.1, num_points),
        'Mg_H_raw_Syn_NLTE': np.random.uniform(-0.5,0.5, num_points),
        'Teff_raw_Syn_NLTE': np.random.uniform(4600, 6000, num_points)
    }]
}
df = pd.DataFrame(data)
####### DADOS ALEATÓRIOS PARA TESTE #######

tailwind_colors = ['#7192B1', '#5C5830', '#A49042', '#978C29', '#A34E33']

delta_met(
    data=df,
    x_label='[Mg/H] (This Work)',
    y_label='[Mg/H] (Syntspec DR17 NLTE)',
    colorbar_label='Teff',
    x_limits=(-0.19, 0.19),
    y_limits=(-0.19, 0.19),
    file_name='figure_delta_Mg_Thiswork_close',
    dpi=500,
    colors='viridis',
    x_axis='Mg',
    y_axis='Mg_H_raw_Syn_NLTE',
    color_axis='Teff_raw_Syn_NLTE',
    colorbar_limits=(1, 6000)
)
