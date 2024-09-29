import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def plot_delta_met(x, y, cor, cmap_name='Blues', xlabel='[Mg/H] (This Work)', ylabel1='[Mg/H] (Syntspec DR17 NLTE)', ylabel2=r'$\delta$($x-y$)', colorbar_label=r'$T_{\rm eff}$'):
    plt.figure()
    plt.subplots(nrows=4, ncols=1, figsize=(3, 3))
    plt.subplots_adjust(left=0.2, right=0.9, bottom=0.13, top=0.91, wspace=0.05, hspace=0.00)


    cmap = matplotlib.colormaps[cmap_name]
    cmap_data = plt.hexbin([0, 0, 0], [0, 0, 0], [1, 2, 3], vmin=4500., vmax=6000., cmap=cmap)


    plt.subplot2grid((4, 1), (0, 0), rowspan=3)
    plt.scatter(x, y, marker='o', c=cor, vmin=4500., vmax=6000., cmap=cmap, edgecolor='k', alpha=0.9, s=20, linewidth=0.4)
    plt.plot([-10000, 10000], [-10000, 10000], '--k', linewidth=0.4)

    cbar = plt.colorbar(cmap_data, shrink=0.95)
    cbar.set_label(colorbar_label, fontsize=7)
    cbar.ax.tick_params(labelsize=6, size=2)


    plt.xlim(-0.4, 0.25)
    plt.ylim(-0.4, 0.25)
    plt.ylabel(ylabel1, fontsize=6)
    plt.xticks([-0.3, -0.2, -0.1, 0., 0.1, 0.2], fontsize=6)
    plt.yticks([-0.4, -0.3, -0.2, -0.1, 0., 0.1, 0.2], fontsize=6)


    plt.tick_params(axis='x', which='minor', top=True, direction='in', size=1, width=0.5)
    plt.tick_params(axis='y', which='minor', right=True, direction='in', size=1, width=0.5)
    plt.tick_params(axis='x', which='major', top=True, direction='in', size=2, width=0.5)
    plt.tick_params(axis='y', which='major', right=True, direction='in', size=2, width=0.5)
    plt.minorticks_on()

    plt.subplot2grid((4, 1), (3, 0))
    plt.scatter(x, x - y, marker='o', c=cor, vmin=4500., vmax=6000., cmap=cmap, edgecolor='k', alpha=0.9, s=20, linewidth=0.4)
    plt.plot([-10000, 10000], [0, 0], '--k', linewidth=0.4)


    plt.xlim(-0.4, 0.25)
    plt.ylim(-0.5, 0.5)
    plt.xlabel(xlabel, fontsize=6)
    plt.ylabel(ylabel2, fontsize=6)


    plt.text(-.39, 0.3, r'$\delta$($x-y$) = ' + str(np.around(np.mean(x - y), 2)) + ' $\pm$ ' + str(np.around(np.std(x - y), 2)), fontsize=4)


    cbar = plt.colorbar(cmap_data, shrink=0.01)
    cbar.ax.tick_params(labelsize=False, size=False)
    cbar.remove()

    plt.xticks([-0.4, -0.2, 0., 0.2], fontsize=6)
    plt.yticks([-0.40, -0.20, 0.00, 0.20, 0.40], fontsize=6)
    plt.tick_params(axis='x', which='minor', top=True, direction='in', size=1, width=0.5)
    plt.tick_params(axis='y', which='minor', right=True, direction='in', size=1, width=0.5)
    plt.tick_params(axis='x', which='major', top=True, direction='in', size=2, width=0.5)
    plt.tick_params(axis='y', which='major', right=True, direction='in', size=2, width=0.5)
    plt.minorticks_on()

    plt.show()

# EXEMPLOS DE TESTE


x_data1 = np.random.uniform(-0.4, 0.25, 100)
y_data1 = np.random.uniform(-0.4, 0.25, 100)
temperature_data1 = np.random.uniform(4500, 6000, 100)

plot_delta_met(x_data1, y_data1, temperature_data1)

x_data2 = np.array([-0.3, -0.1, 0.0, 0.1, 0.2])
y_data2 = np.array([-0.25, -0.05, 0.05, 0.15, 0.22])
temperature_data2 = np.array([5000, 5200, 5400, 5600, 5800])


plot_delta_met(x_data2, y_data2, temperature_data2, cmap_name='Reds')

x_data3 = np.random.uniform(-0.4, 0.25, 100)
y_data3 = x_data3 + np.random.uniform(-0.1, 0.1, 100)
temperature_data3 = np.random.uniform(4500, 6000, 100)

plot_delta_met(x_data3, y_data3, temperature_data3, cmap_name='viridis')