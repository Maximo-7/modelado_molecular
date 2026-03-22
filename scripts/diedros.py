import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# --- Rutas ---
# Ficheros generados con grep + awk: columnas = índice, phi, psi
path_ARG3_298 = '../T298/4-analysis/dih_ARG3.dat'
path_ARG3_400 = '../T400/4-analysis/dih_ARG3.dat'
path_GLN4_298 = '../T298/4-analysis/dih_GLN4.dat'
path_GLN4_400 = '../T400/4-analysis/dih_GLN4.dat'

# --- Carga de datos ---
arg3_298 = np.loadtxt(path_ARG3_298)
arg3_400 = np.loadtxt(path_ARG3_400)
gln4_298 = np.loadtxt(path_GLN4_298)
gln4_400 = np.loadtxt(path_GLN4_400)

# El índice de frame se convierte a tiempo (ps): dt = 0.001 ps
dt = 0.001
t_arg3_298 = (arg3_298[:, 0] - 1) * dt
t_arg3_400 = (arg3_400[:, 0] - 1) * dt
t_gln4_298 = (gln4_298[:, 0] - 1) * dt
t_gln4_400 = (gln4_400[:, 0] - 1) * dt

phi_arg3_298, psi_arg3_298 = arg3_298[:, 1], arg3_298[:, 2]
phi_arg3_400, psi_arg3_400 = arg3_400[:, 1], arg3_400[:, 2]
phi_gln4_298, psi_gln4_298 = gln4_298[:, 1], gln4_298[:, 2]
phi_gln4_400, psi_gln4_400 = gln4_400[:, 1], gln4_400[:, 2]

# --- Figura: 4 paneles (phi y psi para cada residuo) ---
fig, axes = plt.subplots(2, 2, figsize=(10, 6))
(ax1, ax2), (ax3, ax4) = axes

def plot_dih(ax, t_298, d_298, t_400, d_400, title):
    ax.plot(t_298, d_298, color='#2166ac', linewidth=0.9, label=r'$T = 298\,\mathrm{K}$')
    ax.plot(t_400, d_400, color='#d6604d', linewidth=0.9, label=r'$T = 400\,\mathrm{K}$')
    ax.axhline(np.mean(d_298), color='#2166ac', linewidth=0.8, linestyle='--', alpha=0.6)
    ax.axhline(np.mean(d_400), color='#d6604d', linewidth=0.8, linestyle='--', alpha=0.6)
    ax.set_title(title, fontsize=10)
    ax.set_ylabel(r'Ángulo (°)', fontsize=10)
    ax.set_ylim(-180, 180)
    ax.yaxis.set_ticks([-180, -90, 0, 90, 180])
    ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax.tick_params(which='both', direction='in', top=True, right=True)
    ax.legend(fontsize=8, framealpha=0.9)

plot_dih(ax1, t_arg3_298, phi_arg3_298, t_arg3_400, phi_arg3_400,
         r'$\phi$ (Arg-3)')
plot_dih(ax2, t_arg3_298, psi_arg3_298, t_arg3_400, psi_arg3_400,
         r'$\psi$ (Arg-3)')
plot_dih(ax3, t_gln4_298, phi_gln4_298, t_gln4_400, phi_gln4_400,
         r'$\phi$ (Gln-4)')
plot_dih(ax4, t_gln4_298, psi_gln4_298, t_gln4_400, psi_gln4_400,
         r'$\psi$ (Gln-4)')

for ax in (ax3, ax4):
    ax.set_xlabel(r'Tiempo (ps)', fontsize=10)

fig.tight_layout()
fig.savefig('../plots/dihedrals.pdf', dpi=300, bbox_inches='tight')
fig.savefig('../plots/dihedrals.png', dpi=300, bbox_inches='tight')
print('Guardado: dihedrals.pdf y dihedrals.png')
