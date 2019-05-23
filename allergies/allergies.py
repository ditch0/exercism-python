from typing import List


class Allergies(object):
    _ITEMS = [
        'eggs',
        'peanuts',
        'shellfish',
        'strawberries',
        'tomatoes',
        'chocolate',
        'pollen',
        'cats',
    ]

    def __init__(self, score: int) -> None:
        self._lst = self._decode_score(score)

    def allergic_to(self, item: str) -> bool:
        return item in self.lst

    @property
    def lst(self):
        return self._lst

    def _decode_score(self, score: int) -> List[str]:
        bitmask = f'{score:>08b}'
        return [item for i, item in enumerate(self._ITEMS, 1) if bitmask[-i] == '1']
