from um import count


def test_count_single_um():
    assert count("um") == 1


def test_count_question_mark():
    assert count("um?") == 1


def test_count_case_insensitive():
    assert count("Um, thanks for the album.") == 1


def test_count_multiple_um():
    assert count("Um, thanks, um...") == 2


def test_count_no_um():
    assert count("This is a test.") == 0


if __name__ == "__main__":
    pytest.main()