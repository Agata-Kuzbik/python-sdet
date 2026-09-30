import pytest


def test_bad_int_conversion_raise():
    with pytest.raises(ValueError) as exc_info:
        int("abc")
    assert "invalid literal" in str(exc_info.value)


def test_price_equle():

    assert 19.99 + 4.99 + 49.99  == pytest.approx(74.97)

def test_add_float():

    assert 0.1 + 0.1 + 0.1 == pytest.approx(0.3)





