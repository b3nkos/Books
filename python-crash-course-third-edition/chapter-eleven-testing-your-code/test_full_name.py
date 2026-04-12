from full_name import get_full_name

def test_first_last():
    assert get_full_name("jose", "martinez") == "Jose Martinez"

def test_first_middle_last():
    assert get_full_name("jose", "martinez", "luis") == "Jose Luis Martinez"