STRANDS = {'A': 'U', 'G': 'C', 'T': 'A', 'C': 'G'}
def to_rna(dna_strand):
   return ''.join(STRANDS[x] for x in dna_strand)