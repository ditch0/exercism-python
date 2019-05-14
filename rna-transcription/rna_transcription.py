def to_rna(dna_strand: str) -> str:
    table = str.maketrans('GCTA', 'CGAU')
    return dna_strand.translate(table)
