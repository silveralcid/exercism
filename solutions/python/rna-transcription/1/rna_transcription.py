complement = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U",
}

def to_rna(dna_strand):
    return "".join(complement[n] for n in dna_strand)
