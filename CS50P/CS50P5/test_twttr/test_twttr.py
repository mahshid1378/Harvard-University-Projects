from twttr import shorten


def test_shorten():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("Aref") == "rf"
    assert shorten("Rasht : city of the rain!") == "Rsht : cty f th rn!"
    assert shorten("1aeu2b333cii4f5ea") == "12b333c4f5"