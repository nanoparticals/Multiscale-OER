#from ase.calculators.FCPelectrochem import FCP
from ase.calculators.vasp.vaspFCP import VaspFCP
from ase.calculators.vasp import Vasp
from ase.io import read
from ase.optimize import LBFGS

calc=VaspFCP(xc='PBE', #functional
      pp='PBE',            #type of pseudopotential
      kpts=(4, 2, 1),      #kpoint
      ncore=16,
      ismear=0, sigma=0.1, algo='Fast', ediff=1E-5, ispin=2 ,prec='Accurate',
      encut=500,  nelm=500 ,lreal='Auto',ivdw = 11,tau=0,lasph=True, #parameters for SCF
      lrhoion=False, lsol=True, eb_k=78.4, lambda_d_k=9.61, #parameters for vaspsol
      lwave=False, lcharg = False,              #write WAVECAR to speed up the SCF of the next ionic step
      command=r'source /opt/intel/compilers_and_libraries_2018/linux/bin/compilervars.sh intel64;source /opt/intel/mkl/bin/mklvars.sh intel64;source /opt/intel/impi/2018.1.163/bin64/mpivars.sh;killall vasp_std &> /dev/null;mpirun -n 32 /opt/vasp544-fullsol/bin/vasp_std',
      U=0.763,                                          #electrochemical potential vs. SHE
      NELECT =967,                                 #initial guass of number of electrons
      NELECT0=967,                                    #number of electrons at the potential of zero charge
      work_ref=4.6,                                   #the work function of SHE in eV. 
      )      

atoms=read('POSCAR')
atoms.calc = calc
optimizer = LBFGS(atoms)
optimizer.run(fmax=0.01)
