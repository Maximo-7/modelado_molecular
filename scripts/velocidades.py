import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.stats import norm

# --- Rutas ---
path_298 = '../T298/4-analysis/veloc.xvg'
path_400 = '../T400/4-analysis/veloc.xvg'

# --- Carga de datos ---
data_298 = np.loadtxt(path_298, comments=['#', '@'])
data_400 = np.loadtxt(path_400, comments=['#', '@'])

t_298 = data_298[:, 0]
t_400 = data_400[:, 0]

# Átomos seleccionados (numeración en arq.gro, desde 1):
# 9=CA ALA-2, 39=C ARG-3, 41=N GLN-4, 51=CD GLN-4, 43=CA GLN-4
atom_indices = [9, 39, 41, 51, 43]
atom_labels  = ['CA (ALA-2)', 'C (ARG-3)', 'N (GLN-4)', 'CD (GLN-4)', 'CA (GLN-4)']

def get_velocities(data, atom_idx):
    """Devuelve vx, vy, vz, |v| para el átomo con índice atom_idx (desde 1)."""
    base = 1 + (atom_idx - 1) * 4  # índice de columna base (0-based)
    vx  = data[:, base]
    vy  = data[:, base + 1]
    vz  = data[:, base + 2]
    vmod = data[:, base + 3]
    return vx, vy, vz, vmod

# ============================================================
# Figura 1: evolución temporal de |v| para los 5 átomos
# ============================================================
fig1, axes = plt.subplots(5, 1, figsize=(8, 10), sharex=True)

for ax, idx, label in zip(axes, atom_indices, atom_labels):
    _, _, _, vmod_298 = get_velocities(data_298, idx)
    _, _, _, vmod_400 = get_velocities(data_400, idx)
    ax.plot(t_298, vmod_298, color='#2166ac', linewidth=0.9,
            label=r'$T = 298\,\mathrm{K}$')
    ax.plot(t_400, vmod_400, color='#d6604d', linewidth=0.9,
            label=r'$T = 400\,\mathrm{K}$')
    ax.axhline(np.mean(vmod_298), color='#2166ac', linewidth=0.8, linestyle='--', alpha=0.6)
    ax.axhline(np.mean(vmod_400), color='#d6604d', linewidth=0.8, linestyle='--', alpha=0.6)
    ax.set_ylabel(r'$|v|$ (nm/ps)', fontsize=9)
    ax.set_title(label, fontsize=9)
    ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax.tick_params(which='both', direction='in', top=True, right=True)
    ax.legend(fontsize=8, framealpha=0.9)

axes[-1].set_xlabel(r'Tiempo (ps)', fontsize=11)
fig1.suptitle(r'Evolución temporal de $|v|$ para 5 átomos seleccionados', fontsize=11)
fig1.tight_layout()
fig1.savefig('../plots/velocities_time.pdf', dpi=300, bbox_inches='tight')
fig1.savefig('../plots/velocities_time.png', dpi=300, bbox_inches='tight')
print('Guardado: velocities_time.pdf')

# ============================================================
# Figura 2: histogramas de vx con ajuste gaussiano (Maxwell-Boltzmann)
# para los 5 átomos, comparando temperaturas
# ============================================================
fig2, axes2 = plt.subplots(1, 5, figsize=(14, 4))

for ax, idx, label in zip(axes2, atom_indices, atom_labels):
    vx_298, _, _, _ = get_velocities(data_298, idx)
    vx_400, _, _, _ = get_velocities(data_400, idx)

    for vx, color, T_label in [
        (vx_298, '#2166ac', r'298 K'),
        (vx_400, '#d6604d', r'400 K')
    ]:
        mu, sigma = np.mean(vx), np.std(vx)
        ax.hist(vx, bins=25, density=True, alpha=0.4, color=color)
        x = np.linspace(vx.min() - 0.5, vx.max() + 0.5, 300)
        ax.plot(x, norm.pdf(x, mu, sigma), color=color,
                linewidth=1.5, label=T_label)

    ax.set_xlabel(r'$v_x$ (nm/ps)', fontsize=9)
    ax.set_ylabel(r'Densidad', fontsize=9)
    ax.set_title(label, fontsize=9)
    ax.legend(fontsize=8, framealpha=0.9)
    ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax.tick_params(which='both', direction='in', top=True, right=True)

fig2.suptitle(r'Distribución de $v_x$ y ajuste gaussiano (Maxwell-Boltzmann)',
              fontsize=11)
fig2.tight_layout()
fig2.savefig('../plots/velocities_histogram.pdf', dpi=300, bbox_inches='tight')
fig2.savefig('../plots/velocities_histogram.png', dpi=300, bbox_inches='tight')
print('Guardado: velocities_histogram.pdf')
