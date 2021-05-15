STRANDS={'A' : 'U', 'G' : 'C', 'T' : 'A', 'C' : 'G'}
def to_rna(dna_strand):
   rnalist = [STRANDS[x] for x in dna_strand]
   return ''.join(i for i in rnalist)