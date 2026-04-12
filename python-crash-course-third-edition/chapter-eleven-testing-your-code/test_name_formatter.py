from name_formatter import get_formatter_name

def test_first_last_name():
    formatted_name = get_formatter_name("jose", "martinez")
    assert formatted_name == "Jose Martinez"