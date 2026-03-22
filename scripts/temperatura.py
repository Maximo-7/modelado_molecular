import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# --- Rutas ---
path_298 = '../T298/4-analysis/temp.xvg'
path_400 = '../T400/4-analysis/temp.xvg'

# --- Carga de datos ---
data_298 = np.loadtxt(path_298, comments=['#', '@'])
data_400 = np.loadtxt(path_400, comments=['#', '@'])

t_298, T_298 = data_298[:, 0], data_298[:, 1]
t_400, T_400 = data_400[:, 0], data_400[:, 1]

# --- Figura: evolución temporal (izquierda) e histograma (derecha) ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Panel izquierdo: evolución temporal
ax1.plot(t_298, T_298, color='#2166ac', linewidth=0.9, label=r'$T = 298\,\mathrm{K}$')
ax1.plot(t_400, T_400, color='#d6604d', linewidth=0.9, label=r'$T = 400\,\mathrm{K}$')
ax1.axhline(298, color='#2166ac', linewidth=0.8, linestyle='--', alpha=0.6)
ax1.axhline(400, color='#d6604d', linewidth=0.8, linestyle='--', alpha=0.6)
ax1.set_xlabel(r'Tiempo (ps)', fontsize=11)
ax1.set_ylabel(r'$T$ (K)', fontsize=11)
ax1.set_title('Evolución temporal', fontsize=11)
ax1.legend(fontsize=10, framealpha=0.9)
ax1.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1.tick_params(which='both', direction='in', top=True, right=True)

# Panel derecho: histograma
ax2.hist(T_298, bins=20, alpha=0.6, color='#2166ac',
         label=r'$T = 298\,\mathrm{K}$', orientation='horizontal')
ax2.hist(T_400, bins=20, alpha=0.6, color='#d6604d',
         label=r'$T = 400\,\mathrm{K}$', orientation='horizontal')
ax2.axhline(298, color='#2166ac', linewidth=0.8, linestyle='--', alpha=0.6)
ax2.axhline(400, color='#d6604d', linewidth=0.8, linestyle='--', alpha=0.6)
ax2.set_xlabel(r'Frecuencia', fontsize=11)
ax2.set_ylabel(r'$T$ (K)', fontsize=11)
ax2.set_title('Distribución de temperaturas', fontsize=11)
ax2.legend(fontsize=10, framealpha=0.9)
ax2.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax2.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax2.tick_params(which='both', direction='in', top=True, right=True)

fig.tight_layout()
fig.savefig('../plots/temperature.pdf', dpi=300, bbox_inches='tight')
fig.savefig('../plots/temperature.png', dpi=300, bbox_inches='tight')
print('Guardado: temperature.pdf y temperature.png')
