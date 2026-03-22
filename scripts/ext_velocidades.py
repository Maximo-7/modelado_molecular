import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.stats import norm

# =============================================================
# Histogramas de las tres componentes de velocidad
# átomo 9 = CA de ALA-2
# =============================================================

path_veloc = '../extended_report/4-analysis/veloc.xvg'
data = np.loadtxt(path_veloc, comments=['#', '@'])

# Átomo 9: índice Python = 1 + (9-1)*4 = 33 (columna 34 del fichero)
base = 1 + (9 - 1) * 4
vx = data[:, base]
vy = data[:, base + 1]
vz = data[:, base + 2]

components = [vx, vy, vz]
labels = [r'$v_x$', r'$v_y$', r'$v_z$']

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

for ax, v, label in zip(axes, components, labels):
    mu, sigma = np.mean(v), np.std(v)
    ax.hist(v, bins=60, density=True, alpha=0.5, color='#2166ac',
            label='Simulación')
    x = np.linspace(v.min() - 0.3, v.max() + 0.3, 400)
    ax.plot(x, norm.pdf(x, mu, sigma), color='#d6604d', linewidth=1.5,
            label=rf'Gaussiana ($\mu={mu:.3f}$, $\sigma={sigma:.3f}$)')
    ax.set_xlabel(rf'{label} (nm/ps)', fontsize=11)
    ax.set_ylabel(r'Densidad de probabilidad', fontsize=11)
    ax.set_title(rf'CA (ALA-2) — {label}', fontsize=10)
    ax.legend(fontsize=8, framealpha=0.9, loc='upper center',
              bbox_to_anchor=(0.5, -0.18), ncol=1)
    ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax.tick_params(which='both', direction='in', top=True, right=True)

fig.tight_layout(rect=[0, 0.08, 1, 1])
fig.savefig('../plots/ext_velocities_histogram.pdf', dpi=300, bbox_inches='tight')
fig.savefig('../plots/ext_velocities_histogram.png', dpi=300, bbox_inches='tight')
print('Guardado: ext_velocities_histogram.pdf')

