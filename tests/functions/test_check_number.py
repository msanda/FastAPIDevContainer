from api.functions import check_number


def test_large_even_number():
    output = check_number(200)
    assert output == 3