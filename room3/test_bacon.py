import pytest

import bacon


def test_clean():
    assert bacon.clean("Hello, world!") == "Helloworld"


def test_chunk():
    assert list(bacon.chunk("abcdefghijkl")) == ["abcde", "fghij", "kl"]


@pytest.mark.parametrize("input, expected", (
    ("aaaaa", "00000"),
    ("aaaaA", "00001"),
    ("aaaAa", "00010"),
    ("aaaAA", "00011"),
    ("AaaAa", "10010"),
    ("AAAAA", "11111"),
))
def test_hash_chunk(input, expected):
    assert bacon.hash_chunk(input) == expected


@pytest.mark.parametrize("output, cyphertext", [
    [
        "A",
        "aaaaa"
    ],
    [
        "B",
        "aaaaA"
    ],
    [
        "C",
        "aaaAa"
    ],
    [
        "HELLO WORLD",
        "thE QUicK broWn FOx JuMPs OVEr THe LaZy DOgs, GAMbOlinG iN tHE fieLDS WHERE THE SHEPHERDS KEEP WATCH"
    ],
    [
        "steganography",
        "To eNcOde A MesSage eACh letter OF tHe PLAintEXt Is rePlaced bY A GRouP OF FIve oF THE LETTERS 'A' OR 'B'."
    ],
])
def test_decode(output, cyphertext):
    assert bacon.decode(cyphertext).lower() == output.lower()
