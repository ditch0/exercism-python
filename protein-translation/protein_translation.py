import itertools
from typing import List

CODONS_NAMES = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
}


def split_string_to_chunks(string: str, chunk_length: int) -> List[str]:
    return [string[i:i + chunk_length] for i in range(0, len(string), chunk_length)]


def proteins(strand: str) -> List[str]:
    codons = split_string_to_chunks(strand, 3)
    translatable_codons = itertools.takewhile(lambda codon: codon in CODONS_NAMES, codons)
    return [CODONS_NAMES[codon] for codon in translatable_codons]
