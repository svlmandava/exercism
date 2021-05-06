STRANDS={'A' : 'U' , 'G' : 'C' , 'T' : 'A' , 'C' : 'G'}
def to_rna(dna_strand):
   rna = ''
   for x in dna_strand:
      rna += STRANDS[x]
   return rna