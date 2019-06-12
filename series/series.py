from typing import List


def slices(series: str, length: int) -> List[str]:
    if series == '':
        raise ValueError('Series must not be an empty string')

    if length <= 0:
        raise ValueError('Length must be positive integer')

    if length > len(series):
        raise ValueError('Slice length must not exceed length of series')

    return [
        series[i:i + length]
        for i in range(len(series) - length + 1)
    ]
