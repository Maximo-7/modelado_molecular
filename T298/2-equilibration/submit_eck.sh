#!/bin/bash
#
#SBATCH -p eck-q
#SBATCH --chdir=/home/alumno07/modelado_molecular/trabajo/T298/2-equilibration
#SBATCH -J equilibrado_298
#SBATCH --cpus-per-task=1

date
gmx mdrun -deffnm arq -c arq.g96 -nt 1
date



