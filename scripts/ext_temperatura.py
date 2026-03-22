import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# =============================================================
# Histograma de temperatura — extended report (500 ps, 298 K)
# =============================================================

path_temp = '../extended_report/4-analysis/temp.xvg'
data_temp = np.loadtxt(path_temp, comments=['#', '@'])
t, T = data_temp[:, 0], data_temp[:, 1]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7))

# Panel superior: evolución temporal
ax1.plot(t, T, color='#2166ac', linewidth=0.6)
ax1.axhline(298, color='k', linewidth=0.8, linestyle='--', alpha=0.6,
            label=r'$T_\mathrm{ref} = 298\,\mathrm{K}$')
ax1.axhline(np.mean(T), color='#d6604d', linewidth=0.8, linestyle='--',
            label=rf'$\langle T \rangle = {np.mean(T):.1f}\,\mathrm{{K}}$')
ax1.set_xlabel(r'Tiempo (ps)', fontsize=11)
ax1.set_ylabel(r'$T$ (K)', fontsize=11)
ax1.set_title('Evolución temporal de la temperatura', fontsize=11)
ax1.legend(fontsize=10, framealpha=0.9)
ax1.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1.tick_params(which='both', direction='in', top=True, right=True)

# Panel inferior: histograma
ax2.hist(T, bins=60, density=True, alpha=0.6, color='#2166ac')
ax2.axvline(298, color='k', linewidth=0.8, linestyle='--', alpha=0.6,
            label=r'$T_\mathrm{ref} = 298\,\mathrm{K}$')
ax2.axvline(np.mean(T), color='#d6604d', linewidth=0.8, linestyle='--',
            label=rf'$\langle T \rangle = {np.mean(T):.1f}\,\mathrm{{K}}$')
ax2.set_xlabel(r'$T$ (K)', fontsize=11)
ax2.set_ylabel(r'Densidad de probabilidad', fontsize=11)
ax2.set_title('Distribución de temperaturas', fontsize=11)
ax2.legend(fontsize=10, framealpha=0.9)
ax2.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax2.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax2.tick_params(which='both', direction='in', top=True, right=True)

fig.tight_layout()
fig.savefig('../plots/ext_temperature.pdf', dpi=300, bbox_inches='tight')
fig.savefig('../plots/ext_temperature.png', dpi=300, bbox_inches='tight')
print('Guardado: ext_temperature.pdf')
