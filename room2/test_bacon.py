import pytest
import bacon

@pytest.mark.parametrize(
    "expected, message",
    [
        ("a", "aacda"),
        ("aa", "aacdaaacda"),
        ("aa ", "aacdaaacdaACbAa"),
        ("ca ", "aacDa aacdaACbAa"),
        ("ca ", "aacDa.aacdaACbAa"),
        ("ca ", "aacDa,aacdaACbAa"),
    ]
)
def test_decode(expected, message):
    assert bacon.decode(message) == expected

@pytest.mark.parametrize(
    "expected, chunk",
    [
        ("a", "aacda"),
        ("b", "aaaaB"),
        (" ", "ACbAa"),
    ]
)
def test_decode_one(expected, chunk):
    assert bacon.decode_one(chunk) == expected

@pytest.mark.parametrize(
    "expected, chunk",
    [
        (0, "aaaaa"),
        (1, "aaaaA"),
        (2, "aaaAa"),
        (10, "aCbAa"),
        (26, "ACbAa"),       
    ]
)
def test_bitmask(expected, chunk):
    assert bacon.bitmask(chunk) == expected
