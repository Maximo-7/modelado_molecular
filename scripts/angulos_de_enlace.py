import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# --- Rutas ---
path_CACO_298 = '../T298/4-analysis/angaver_CACO.xvg'
path_CACO_400 = '../T400/4-analysis/angaver_CACO.xvg'
path_NCAC_298 = '../T298/4-analysis/angaver_NCAC.xvg'
path_NCAC_400 = '../T400/4-analysis/angaver_NCAC.xvg'

# --- Carga de datos ---
data_CACO_298 = np.loadtxt(path_CACO_298, comments=['#', '@'])
data_CACO_400 = np.loadtxt(path_CACO_400, comments=['#', '@'])
data_NCAC_298 = np.loadtxt(path_NCAC_298, comments=['#', '@'])
data_NCAC_400 = np.loadtxt(path_NCAC_400, comments=['#', '@'])

t_CACO_298, caco_298 = data_CACO_298[:, 0], data_CACO_298[:, 1]
t_CACO_400, caco_400 = data_CACO_400[:, 0], data_CACO_400[:, 1]
t_NCAC_298, ncac_298 = data_NCAC_298[:, 0], data_NCAC_298[:, 1]
t_NCAC_400, ncac_400 = data_NCAC_400[:, 0], data_NCAC_400[:, 1]

# --- Figura con dos paneles ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 6))

# Panel 1: ángulo Cα-C=O (Arg-2)
ax1.plot(t_CACO_298, caco_298, color='#2166ac', linewidth=1.0, label=r'$T = 298\,\mathrm{K}$')
ax1.plot(t_CACO_400, caco_400, color='#d6604d', linewidth=1.0, label=r'$T = 400\,\mathrm{K}$')
ax1.axhline(121.212, color='#2166ac', linewidth=0.8, linestyle='--', alpha=0.6)
ax1.axhline(121.043, color='#d6604d', linewidth=0.8, linestyle='--', alpha=0.6)
ax1.set_ylabel(r'Ángulo (°)', fontsize=11)
ax1.set_title(r'Ángulo C$\alpha-$C$=$O (Arg-2)', fontsize=11)
ax1.legend(fontsize=10, framealpha=0.9)
ax1.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1.tick_params(which='both', direction='in', top=True, right=True)

# Panel 2: ángulo N-Cα-C (Gln-3)
ax2.plot(t_NCAC_298, ncac_298, color='#2166ac', linewidth=1.0, label=r'$T = 298\,\mathrm{K}$')
ax2.plot(t_NCAC_400, ncac_400, color='#d6604d', linewidth=1.0, label=r'$T = 400\,\mathrm{K}$')
ax2.axhline(113.696, color='#2166ac', linewidth=0.8, linestyle='--', alpha=0.6)
ax2.axhline(114.336, color='#d6604d', linewidth=0.8, linestyle='--', alpha=0.6)
ax2.set_xlabel(r'Tiempo (ps)', fontsize=11)
ax2.set_ylabel(r'Ángulo (°)', fontsize=11)
ax2.set_title(r'Ángulo N$-$C$\alpha-$C (Gln-3)', fontsize=11)
ax2.legend(fontsize=10, framealpha=0.9)
ax2.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax2.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax2.tick_params(which='both', direction='in', top=True, right=True)

fig.tight_layout()
fig.savefig('../plots/angles.pdf', dpi=300, bbox_inches='tight')
fig.savefig('../plots/angles.png', dpi=300, bbox_inches='tight')
print('Guardado: angles.pdf y angles.png')
