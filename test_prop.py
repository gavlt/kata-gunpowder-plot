import string

import pytest
from hypothesis import given, note, assume
from hypothesis.strategies import text

from encode import g as encode
from room1.bacon import decode as decode1
from room2.bacon import decode as decode2
from room3.bacon import decode as decode3


@pytest.mark.parametrize("decode", (decode1, decode2, decode3))
@given(text(alphabet=string.ascii_letters + " "), text(alphabet=string.printable))
def test_decode_inverts_encode(decode, secret, carrier):
    assume(sum(c.isalpha() for c in carrier) >= len(secret) * 5)
    encoded = encode(secret, carrier)
    assert encoded.upper() == carrier.upper()
    note(f"Encoded as: {encoded}")
    decoded = decode(encoded)
    assert decoded.upper() == secret.upper()
