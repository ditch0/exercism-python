import math
import re
from typing import List


def _normalize_text(text: str) -> str:
    return re.sub(r'[^a-z0-9]+', '', text.lower())


def _split_to_chunks(text: str, chunk_length: int) -> List[str]:
    if chunk_length == 0:
        return [text]
    return [text[i:i + chunk_length] for i in range(0, len(text), chunk_length)]


def encode(plain_text: str) -> str:
    text = _normalize_text(plain_text)
    chunk_length = math.ceil(math.sqrt(len(text)))
    chunks = _split_to_chunks(text, chunk_length)
    encoded_chunks = [
        ''.join(chunk[i] if i < len(chunk) else ' ' for chunk in chunks)
        for i in range(chunk_length)
    ]
    return ' '.join(encoded_chunks)
