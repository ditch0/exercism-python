from typing import Mapping, List

LegacyScoreMap = Mapping[int, List[str]]
ScoreMap = Mapping[str, int]


def transform(legacy_data: LegacyScoreMap) -> ScoreMap:
    return {
        letter.lower(): score
        for score, letters in legacy_data.items()
        for letter in letters
    }
