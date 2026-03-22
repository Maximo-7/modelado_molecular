import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# --- Rutas ---
path_298 = '../T298/4-analysis/gyrate.xvg'
path_400 = '../T400/4-analysis/gyrate.xvg'

# --- Carga de datos ---
data_298 = np.loadtxt(path_298, comments=['#', '@'])
data_400 = np.loadtxt(path_400, comments=['#', '@'])

t_298, rg_298 = data_298[:, 0], data_298[:, 1]
t_400, rg_400 = data_400[:, 0], data_400[:, 1]

# --- Figura ---
fig, ax = plt.subplots(figsize=(7, 4))

ax.plot(t_298, rg_298, color='#2166ac', linewidth=1.2, label=r'$T = 298\,\mathrm{K}$')
ax.plot(t_400, rg_400, color='#d6604d', linewidth=1.2, label=r'$T = 400\,\mathrm{K}$')

# Medias como líneas horizontales discontinuas
ax.axhline(np.mean(rg_298), color='#2166ac', linewidth=0.8, linestyle='--', alpha=0.6)
ax.axhline(np.mean(rg_400), color='#d6604d', linewidth=0.8, linestyle='--', alpha=0.6)

# --- Formato ---
ax.set_xlabel(r'Tiempo (ps)', fontsize=11)
ax.set_ylabel(r'$R_\mathrm{gyr}$ (nm)', fontsize=11)
ax.set_title('Radio de giro del péptido ARQ', fontsize=12)
ax.legend(fontsize=10, framealpha=0.9)

ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.tick_params(which='both', direction='in', top=True, right=True)

fig.tight_layout()
fig.savefig('../plots/gyrate.pdf', dpi=300, bbox_inches='tight')
fig.savefig('../plots/gyrate.png', dpi=300, bbox_inches='tight')
print('Guardado: gyrate.pdf y gyrate.png')
