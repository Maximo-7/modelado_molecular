import numpy as np
import matplotlib.pyplot as plt

# =============================================================
# Diagramas de Ramachandran — mapa de densidad lineal
# =============================================================

path_rama = '../extended_report/4-analysis/rama.xvg'

ala2_phi, ala2_psi = [], []
arg3_phi, arg3_psi = [], []
gln4_phi, gln4_psi = [], []

with open(path_rama) as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('@'):
            continue
        parts = line.split()
        phi, psi, resname = float(parts[0]), float(parts[1]), parts[2]
        if 'ALA-2' in resname:
            ala2_phi.append(phi); ala2_psi.append(psi)
        elif 'ARG-3' in resname:
            arg3_phi.append(phi); arg3_psi.append(psi)
        elif 'GLN-4' in resname:
            gln4_phi.append(phi); gln4_psi.append(psi)

residues = [
    (np.array(ala2_phi), np.array(ala2_psi), 'ALA-2'),
    (np.array(arg3_phi), np.array(arg3_psi), 'ARG-3'),
    (np.array(gln4_phi), np.array(gln4_psi), 'GLN-4'),
]

# Regiones conformacionales (Hollingsworth & Karplus, 2010)
regions = {
    r'$\alpha$':    (-63,  -43),
    r'$\beta$':     (-120, 130),
    r'$P_{II}$':    (-65,  145),
}

fig, axes = plt.subplots(1, 3, figsize=(14, 5))

for ax, (phi, psi, title) in zip(axes, residues):
    h = ax.hist2d(phi, psi, bins=100,
                  range=[[-180, 180], [-180, 180]],
                  density=True,
                  cmap='viridis')
    cbar = plt.colorbar(h[3], ax=ax)
    cbar.set_label('Densidad de probabilidad', fontsize=9)

    # Líneas de referencia en 0°
    ax.axhline(0, color='white', linewidth=0.5, alpha=0.4)
    ax.axvline(0, color='white', linewidth=0.5, alpha=0.4)

    # Anotaciones de regiones
    for label, (phi_c, psi_c) in regions.items():
        ax.annotate(label, xy=(phi_c, psi_c), color='white',
                    fontsize=10, ha='center',
                    bbox=dict(boxstyle='round,pad=0.2', fc='black', alpha=0.4))

    ax.set_xlabel(r'$\phi$ (°)', fontsize=11)
    ax.set_ylabel(r'$\psi$ (°)', fontsize=11)
    ax.set_title(title, fontsize=12)
    ax.set_xlim(-180, 180)
    ax.set_ylim(-180, 180)
    ax.set_xticks([-180, -90, 0, 90, 180])
    ax.set_yticks([-180, -90, 0, 90, 180])
    ax.tick_params(which='both', direction='in', top=True, right=True)

fig.suptitle('Diagramas de Ramachandran', fontsize=13)
fig.tight_layout()
fig.savefig('../plots/ext_ramachandran.pdf', dpi=300, bbox_inches='tight')
fig.savefig('../plots/ext_ramachandran.png', dpi=300, bbox_inches='tight')
print('Guardado: ext_ramachandran.pdf')

