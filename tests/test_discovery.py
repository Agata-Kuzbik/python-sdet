
def test_is_string():
    name = "Agata"

    assert  isinstance(name, str)

def add_numbers():

    assert 1 + 2 == 3

class Test_results():

    def test_add_numbers(self):

        assert 1 + 4 == 5


def test_add_numbers_incorrect_value():

    expected = 4
    actual = 2 + 2

    assert actual == expected, f"got {actual}, expected {expected}"
    


       