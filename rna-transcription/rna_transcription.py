def to_rna(dna_strand):
    dna_torna={'A':'U','G':'C','T':'A','C':'G'}
    rna = ''
    for x in dna_strand:
       rna += dna_torna.get(x,rna)
    return rna