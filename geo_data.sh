#!/bin/bash
#SBATCH --mem=64GB
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4

#myscript.sh

if test $# -lt 2; then
    echo "usage: $0 GSEACC ROOTPATH"
    exit 1
fi
arg1=$1
arg2=$2

# copy input locally
#cp $arg1 /hpfs/userws/cobbc07/NCBI_files/test_rnaseq_counts.txt

python geo_data.py $arg1 $arg2