import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# --- Rutas ---
path_298 = '../T298/4-analysis/dist.xvg'
path_400 = '../T400/4-analysis/dist.xvg'

# --- Carga de datos ---
data_298 = np.loadtxt(path_298, comments=['#', '@'])
data_400 = np.loadtxt(path_400, comments=['#', '@'])

t_298, cn_298, co_298 = data_298[:, 0], data_298[:, 1], data_298[:, 2]
t_400, cn_400, co_400 = data_400[:, 0], data_400[:, 1], data_400[:, 2]

# --- Figura con dos paneles ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 6), sharex=True)

# Panel 1: enlace peptídico C--N (Arg-2, Gln-3)
ax1.plot(t_298, cn_298, color='#2166ac', linewidth=1.0, label=r'$T = 298\,\mathrm{K}$')
ax1.plot(t_400, cn_400, color='#d6604d', linewidth=1.0, label=r'$T = 400\,\mathrm{K}$')
ax1.axhline(np.mean(cn_298), color='#2166ac', linewidth=0.8, linestyle='--', alpha=0.6)
ax1.axhline(np.mean(cn_400), color='#d6604d', linewidth=0.8, linestyle='--', alpha=0.6)
ax1.set_ylabel(r'$d$ (nm)', fontsize=11)
ax1.set_title(r'Enlace peptídico C$-$N (Arg-2, Gln-3)', fontsize=11)
ax1.legend(fontsize=10, framealpha=0.9)
ax1.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1.tick_params(which='both', direction='in', top=True, right=True)

# Panel 2: enlace carbonilo C=O (Gln-3)
ax2.plot(t_298, co_298, color='#2166ac', linewidth=1.0, label=r'$T = 298\,\mathrm{K}$')
ax2.plot(t_400, co_400, color='#d6604d', linewidth=1.0, label=r'$T = 400\,\mathrm{K}$')
ax2.axhline(np.mean(co_298), color='#2166ac', linewidth=0.8, linestyle='--', alpha=0.6)
ax2.axhline(np.mean(co_400), color='#d6604d', linewidth=0.8, linestyle='--', alpha=0.6)
ax2.set_xlabel(r'Tiempo (ps)', fontsize=11)
ax2.set_ylabel(r'$d$ (nm)', fontsize=11)
ax2.set_title(r'Enlace carbonilo C=O (Gln-3)', fontsize=11)
ax2.legend(fontsize=10, framealpha=0.9)
ax2.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax2.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax2.tick_params(which='both', direction='in', top=True, right=True)

fig.tight_layout()
fig.savefig('../plots/distances.pdf', dpi=300, bbox_inches='tight')
fig.savefig('../plots/distances.png', dpi=300, bbox_inches='tight')
print('Guardado: distances.pdf y distances.png')
