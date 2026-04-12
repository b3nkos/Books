from src.breadth_first_search import search

def test_search() -> None:
    assert search("you") == True
    assert search("claire") == True
    assert search("peggy") == False