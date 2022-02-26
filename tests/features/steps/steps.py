from behave import given, when, then
from deck import Card
from dan import who_wins

suit_map = {
    "c": "Clubs",
    "d": "Diamonds",
    "h": "Hearts",
    "s": "Spades",
}

value_map = {
    "A": "Ace",
    "K": "King",
    "Q": "Queen",
    "J": "Jack",
}


def get_card_value(card_value):
    try:
        return int(card_value)
    except ValueError:
        return str(card_value)


def get_suite_value(suit_value) -> str:
    return suit_value.upper()


def get_card(short_hand) -> Card:
    card_value = get_card_value(short_hand[0:1])
    if isinstance(card_value, str):
        card_value = value_map[card_value.upper()]
    
    return Card(value=card_value, suit=get_suite_value(suit_map[short_hand[1:].lower()]))


@given(u'a new deal')
def setup_new_deal(context) -> None:
    context.players = {}


@given(u'Player {player_number} is dealt {card_1} {card_2} {card_3} {card_4} {card_5}')
def a_player_has_a_hand(context, player_number, card_1, card_2, card_3, card_4, card_5) -> None:
    hand = []
    
    hand.append(get_card(card_1))
    hand.append(get_card(card_2))
    hand.append(get_card(card_3))
    hand.append(get_card(card_4))
    hand.append(get_card(card_5))

    context.players[player_number] = hand


@when(u'hands are compared')
def compare_hands(context):
    context.winner = who_wins(context.players["1"], context.players["2"])


@then(u'Player {player} is the winner')
def assert_correct_player_wins(context, player):
    print(context.winner["winner"])
    assert player == context.winner["winner"].split(" ")[1]


@then(u'they win with "High Card: Ace"')
def step_impl(context):
    pass