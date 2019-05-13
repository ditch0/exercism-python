def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must have same length')

    return len([i for i in range(len(strand_a)) if strand_a[i] != strand_b[i]])
