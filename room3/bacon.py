from typing import Sequence

cipher = {
    "00000": "A",
    "00001": "B",
    "00010": "C",
    "00011": "D",
    "00100": "E",
    "00101": "F",
    "00110": "G",
    "00111": "H",
    "01000": "I",
    "01001": "J",
    "01010": "K",
    "01011": "L",
    "01100": "M",
    "01101": "N",
    "01110": "O",
    "01111": "P",
    "10000": "Q",
    "10001": "R",
    "10010": "S",
    "10011": "T",
    "10100": "U",
    "10101": "V",
    "10110": "W",
    "10111": "X",
    "11000": "Y",
    "11001": "Z",
    "11010": " ",
}


def clean(s: str) -> str:
    return ''.join(c for c in s if c.isalpha())

def chunk(s: str) -> Sequence[str]:
    chunk_size = 5
    for i in range(0, len(s), chunk_size):
        yield s[i : i + chunk_size]

def hash_chunk(chunk: str) -> str:
    return "".join("1" if s.isupper() else "0" for s in chunk)

def decode_character(key: str) -> str:
    return cipher.get(key, "")

def _decode(message: str) -> str:
    cleaned_msg = clean(message)    
    chunks = chunk(cleaned_msg)
    for c in chunks:
        lookup_key = hash_chunk(c)
        char = decode_character(lookup_key)
        yield char


def decode(message: str) -> str:
    return "".join(_decode(message))


if __name__ == "__main__":
    with open("../message.txt") as f:
        print(decode(f.read()))
