def to_rna(dna_strand=''):
    dna_seq=list('AGTC')
    rna_seq=list('UCAG')
    rna=''
    for x in dna_strand:
        if x is dna_seq[0]:
            rna += rna_seq[0]
        if x is dna_seq[1]:
            rna += rna_seq[1]
        if x is dna_seq[2]:
            rna += rna_seq[2]
        if x is dna_seq[3]:
            rna += rna_seq[3]
    if rna is not '':
       return rna
    else:
        return ''