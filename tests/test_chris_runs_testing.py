from deck import Card
from main import *

def test_this_works() -> None:
    assert True

def test_this_does_not_work() -> None:
    assert not False


def test_parsing_card():
    value = '2H'
    result = get_card_from_text(value)
    assert result == Card('hearts', 2)


def test_parse_hand():
    given = 'Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH'

