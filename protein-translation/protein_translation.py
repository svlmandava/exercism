RNASEQ = {"AUG" : "Methionine", "UUU" : "Phenylalanine", "UUC" : "Phenylalanine", "UUA" : "Leucine", "UUG" : "Leucine", "UCU" : "Serine", "UCC" : "Serine", "UCA" : "Serine", "UCG" : "Serine", "UAU" : "Tyrosine", "UAC" : "Tyrosine", "UGU" : "Cysteine", "UGC" : "Cysteine", "UGG" : "Tryptophan", "UAA" : "STOP", "UAG" : "STOP", "UGA" : "STOP"}

def proteins(strand):
    protein = []
    for x in range(0, len(strand), 3):
      value = RNASEQ[strand[x : x + 3]]
      if value == "STOP" :
        break
      protein.append(value)
    return protein