from deck import Deck, Card, get_poker_hand
from dan import who_wins

d = Deck(include_jokers=False)

def test_example_1() -> None:
    # Player 1: 2H 3D 5S 9C KD
    player_1 = [
        Card(suit="Hearts", value=2),
        Card(suit="Diamonds", value=3),
        Card(suit="Spades", value=5),
        Card(suit='Clubs', value=9),
        Card(suit="Diamonds", value="King")
    ]

    # Player 2: 2C 3H 4S 8C AH
    player_2 = [
        Card(suit="Clubs", value=2),
        Card(suit="Hearts", value=3),
        Card(suit="Spades", value=4),
        Card(suit="Clubs", value=9),
        Card(suit="Hearts", value="Ace"),
    ]

    winner = who_wins(player_1, player_2)

    assert winner["winner"] == "Player 2"
    wins_with = str(winner["hand"][0]).split(".")[1]
    assert wins_with == "HighCard"



def test_expected_output():
    expected = 'Player 1 wins. - with high card: Ace'
    input_ = 'Player 1: 2H 3D 5S 9C KD  Player 2: 2C 3H 4S 8C AH'
    result = figure_this_out_dan(input_)
    assert result == expected