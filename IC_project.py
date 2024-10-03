import matplotlib.pyplot as plt
import numpy as np


def plot_delta_met(x, y, cor, xlim_min, xlim_max, ylim_min, ylim_max,
                   xlabel='[Mg/H] (This Work)', ylabel1='[Mg/H] (Syntspec DR17 NLTE)', ylabel2=r'$\delta$($x-y$)',
                   colorbar_label=r'$T_{\rm eff}$', cmap_name='Blues', filename='plot', dpi=300):
    plt.figure(figsize=(6, 6))

    plt.subplots_adjust(left=0.2, right=0.9, bottom=0.13, top=0.91, wspace=0.05, hspace=0.2)

    cmap = plt.get_cmap(cmap_name)
    vmin, vmax = np.min(cor), np.max(cor)

    plt.subplot2grid((2, 1), (0, 0))
    sc = plt.scatter(x, y, marker='o', c=cor, vmin=vmin, vmax=vmax, cmap=cmap, edgecolor='k', alpha=0.9, s=20,
                     linewidth=0.4)
    plt.plot([-10000, 10000], [-10000, 10000], '--k', linewidth=0.4)
    cbar = plt.colorbar(sc, shrink=0.95)
    cbar.set_label(colorbar_label, fontsize=10)
    cbar.ax.tick_params(labelsize=8, size=2)

    plt.xlim(xlim_min, xlim_max)
    plt.ylim(ylim_min, ylim_max)
    plt.ylabel(ylabel1, fontsize=8)
    plt.xticks(np.linspace(xlim_min, xlim_max, num=6), fontsize=8)
    plt.yticks(np.linspace(ylim_min, ylim_max, num=6), fontsize=8)


    plt.tick_params(axis='x', which='minor', top=True, direction='in', size=1, width=0.5)
    plt.tick_params(axis='y', which='minor', right=True, direction='in', size=1, width=0.5)
    plt.tick_params(axis='x', which='major', top=True, direction='in', size=2, width=0.5)
    plt.tick_params(axis='y', which='major', right=True, direction='in', size=2, width=0.5)
    plt.minorticks_on()


    plt.subplot2grid((2, 1), (1, 0))
    sc2 = plt.scatter(x, x - y, marker='o', c=cor, vmin=vmin, vmax=vmax, cmap=cmap, edgecolor='k', alpha=0.9, s=20,
                      linewidth=0.4)
    plt.plot([-10000, 10000], [0, 0], '--k', linewidth=0.4)

    plt.xlim(xlim_min, xlim_max)
    plt.ylim(-0.5, 0.5)
    plt.xlabel(xlabel, fontsize=8)
    plt.ylabel(ylabel2, fontsize=8)

    plt.text(xlim_min + 0.01, 0.3, r'$\delta$($x-y$) = ' + str(np.around(np.mean(x - y), 2)) +
             ' $\pm$ ' + str(np.around(np.std(x - y), 2)), fontsize=6)

    plt.xticks(np.linspace(xlim_min, xlim_max, num=6), fontsize=8)
    plt.yticks(np.linspace(-0.5, 0.5, num=5), fontsize=8)


    plt.tick_params(axis='x', which='minor', top=True, direction='in', size=1, width=0.5)
    plt.tick_params(axis='y', which='minor', right=True, direction='in', size=1, width=0.5)
    plt.tick_params(axis='x', which='major', top=True, direction='in', size=2, width=0.5)
    plt.tick_params(axis='y', which='major', right=True, direction='in', size=2, width=0.5)
    plt.minorticks_on()


    plt.savefig(f'{filename}.pdf', dpi=dpi, format='pdf', bbox_inches='tight')
    plt.savefig(f'{filename}.jpg', dpi=dpi, format='jpg', bbox_inches='tight')

    plt.show()


# Exemplo de uso
x_data = np.random.uniform(-0.4, 0.25, 100)
y_data = np.random.uniform(-0.4, 0.25, 100)
temperature_data = np.random.uniform(4500, 6000, 100)

plot_delta_met(x_data, y_data, temperature_data, xlim_min=-0.4, xlim_max=0.25, ylim_min=-0.4, ylim_max=0.25,
               xlabel='X Axis Label', ylabel1='Y Axis Label', filename='my_plot', dpi=300)

