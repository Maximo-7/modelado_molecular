#!/bin/bash
#
#SBATCH -p eck-q
#SBATCH --chdir=/home/alumno07/modelado_molecular/trabajo/T298/3-run
#SBATCH -J run_298
#SBATCH --cpus-per-task=1

date
gmx mdrun -deffnm arq -c arq.g96 -nt 1
date



