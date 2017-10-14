#!/bin/bash
#SBATCH --partition=batch
##SBATCH --time=00:15:00
#SBATCH --nodes=2
## replace --nodes with --ntasks to specify number of cores; nodes and ntasks can't be specified together
#SBATCH --ntasks-per-node=8
#SBATCH --mem=24000
## mem-per-cpu can be used to specify per core memory limit; mem-per-cpu and mem can't be specified together
#SBATCH --job-name="spectral_test" 
#SBATCH --output=test-srun.out
##SBATCH --mail-user=bert@asti.dost.gov.ph
##SBATCH --mail-type=ALL
#SBATCH --requeue

echo "SLURM_JOBID="$SLURM_JOBID
echo "SLURM_JOB_NODELIST"=$SLURM_JOB_NODELIST
echo "SLURM_NNODES"=$SLURM_NNODES
echo "SLURMTMPDIR="$SLURMTMPDIR

echo "working directory = "$SLURM_SUBMIT_DIR

# Place commands to load environment modules here
module load anaconda2
source activate rutenv
# Set stack size to unlimited 
ulimit -s unlimited

# MAIN 
cd spectral/src
python3 topic-generator.py ../dist
source deactivate