import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# --- Rutas ---
path_etot_298 = '../T298/4-analysis/total_energy.xvg'
path_etot_400 = '../T400/4-analysis/total_energy.xvg'
path_ekin_298 = '../T298/4-analysis/kinetic_energy.xvg'
path_ekin_400 = '../T400/4-analysis/kinetic_energy.xvg'

# --- Carga de datos ---
etot_298 = np.loadtxt(path_etot_298, comments=['#', '@'])
etot_400 = np.loadtxt(path_etot_400, comments=['#', '@'])
ekin_298 = np.loadtxt(path_ekin_298, comments=['#', '@'])
ekin_400 = np.loadtxt(path_ekin_400, comments=['#', '@'])

t_etot_298, E_tot_298 = etot_298[:, 0], etot_298[:, 1]
t_etot_400, E_tot_400 = etot_400[:, 0], etot_400[:, 1]
t_ekin_298, E_kin_298 = ekin_298[:, 0], ekin_298[:, 1]
t_ekin_400, E_kin_400 = ekin_400[:, 0], ekin_400[:, 1]

# --- Figura: energía total (arriba) y cinética (abajo) ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 6), sharex=True)

# Panel superior: energía total
ax1.plot(t_etot_298, E_tot_298, color='#2166ac', linewidth=0.9,
         label=r'$T = 298\,\mathrm{K}$')
ax1.plot(t_etot_400, E_tot_400, color='#d6604d', linewidth=0.9,
         label=r'$T = 400\,\mathrm{K}$')
ax1.axhline(np.mean(E_tot_298), color='#2166ac', linewidth=0.8,
            linestyle='--', alpha=0.6)
ax1.axhline(np.mean(E_tot_400), color='#d6604d', linewidth=0.8,
            linestyle='--', alpha=0.6)
ax1.set_ylabel(r'$E_\mathrm{tot}$ (kJ/mol)', fontsize=11)
ax1.set_title('Energía total', fontsize=11)
ax1.legend(fontsize=10, framealpha=0.9)
ax1.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1.tick_params(which='both', direction='in', top=True, right=True)

# Panel inferior: energía cinética
ax2.plot(t_ekin_298, E_kin_298, color='#2166ac', linewidth=0.9,
         label=r'$T = 298\,\mathrm{K}$')
ax2.plot(t_ekin_400, E_kin_400, color='#d6604d', linewidth=0.9,
         label=r'$T = 400\,\mathrm{K}$')
ax2.axhline(np.mean(E_kin_298), color='#2166ac', linewidth=0.8,
            linestyle='--', alpha=0.6)
ax2.axhline(np.mean(E_kin_400), color='#d6604d', linewidth=0.8,
            linestyle='--', alpha=0.6)
ax2.set_xlabel(r'Tiempo (ps)', fontsize=11)
ax2.set_ylabel(r'$E_\mathrm{kin}$ (kJ/mol)', fontsize=11)
ax2.set_title('Energía cinética', fontsize=11)
ax2.legend(fontsize=10, framealpha=0.9)
ax2.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax2.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax2.tick_params(which='both', direction='in', top=True, right=True)

fig.tight_layout()
fig.savefig('../plots/energies.pdf', dpi=300, bbox_inches='tight')
fig.savefig('../plots/energies.png', dpi=300, bbox_inches='tight')
print('Guardado: energies.pdf y energies.png')

# --- Cálculo teórico de la energía cinética ---
# E_kin = (3/2) * N * k_B * T
# k_B = 1.380649e-23 J/K = 8.314462e-3 kJ/(mol·K)  (usando R = N_A * k_B)
N_atoms = 2629  # átomos del sistema
k_B = 8.314462e-3  # kJ/(mol·K)

E_kin_teo_298 = 1.5 * N_atoms * k_B * 298
E_kin_teo_400 = 1.5 * N_atoms * k_B * 400

print(f'\nComparación energía cinética:')
print(f'T = 298 K:')
print(f'  Simulación: {np.mean(E_kin_298):.2f} kJ/mol')
print(f'  Teórico:    {E_kin_teo_298:.2f} kJ/mol')
print(f'T = 400 K:')
print(f'  Simulación: {np.mean(E_kin_400):.2f} kJ/mol')
print(f'  Teórico:    {E_kin_teo_400:.2f} kJ/mol')
