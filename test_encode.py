import pytest
from hypothesis import given
from hypothesis.strategies import text

import encode


@pytest.mark.parametrize(
    "secret, carrier, expected",
    (
        (
            "q",
            "hello",
            "Hello",
        ),
        (
            "QQ",
            "hello world",
            "Hello World",
        ),
        (
            "HELLO WORLD",
            "The quick brown fox jumps over the lazy dogs, gamboling in the fields where the shepherds keep watch",
            "thE QUicK broWn FOx JuMPs OVEr THe LaZy DOgs, GAMbOlinG iN tHE fieLDS WHERE THE SHEPHERDS KEEP WATCH",
        ),
        (
            "steganography",
            "To encode a message each letter of the plaintext is replaced by a group of five of the letters 'A' or 'B'.",
            "To eNcOde A MesSage eACh letter OF tHe PLAintEXt Is rePlaced bY A GRouP OF FIve oF THE LETTERS 'A' OR 'B'.",
        ),
        (
            "imperceptibility",
            "The quick brown fox jumps over the lazy dogs, gamboling in the fields where the shepherds keep watch",
            "tHe quiCK broWN FOx jUmpS oveR the Lazy Dogs, GAMBOliNG iN the fielDs Where ThE ShEpheRds KEEP watCH",
        ),
    ),
)
def test_encode(secret, carrier, expected):
    assert encode.g(secret, carrier) == expected


def test_encode_value_error():
    secret = "telecommunication"
    carrier = "The quick brown fox jumps over the lazy dogs, gamboling in the fields where the shepherds keep watch"
    with pytest.raises(ValueError):
        encode.g(secret, carrier)


@given(text(), text())
def test_encode_prop(message, carrier):
    try:
        encoded = encode.g(message, carrier)
    except ValueError:
        assert sum(c.isalpha() for c in carrier) < len(message) * 5
    else:
        assert encoded.upper() == carrier.upper()
