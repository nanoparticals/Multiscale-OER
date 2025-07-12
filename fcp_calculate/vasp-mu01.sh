#!/bin/sh -f

#PBS -N test
#PBS -l nodes=1:ppn=32
#PBS -l walltime=1200:00:00
#PBS -q batch
#PBS -V
export VASP_PP_PATH=/home/haoxw/POTCAR
cd $PBS_O_WORKDIR
python fcp.py
