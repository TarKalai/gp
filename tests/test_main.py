from gp.main import fibonacci_recursive


def test_main() -> None:
    assert True


def test_fibonacci_recursive() -> None:
    expected_answer = 233
    assert fibonacci_recursive(13) == expected_answer
