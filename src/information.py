import pylab  # aka matplotlib
from Bio import SeqIO  # biopython and it's friends :)
from Bio.SeqUtils import molecular_weight
from lib import info

# Pre-made data
records = list(SeqIO.parse("data/genome.gb", "genbank"))
dna_info = records[0]

# Major Properties
print('\nData imported...\nWorking with: ')
info.major(dna_info.name, dna_info.description, dna_info.seq[:100])