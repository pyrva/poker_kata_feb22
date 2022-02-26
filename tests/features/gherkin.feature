Feature: Poker Rules

    Let's look at some poker rules with BDD

    Scenario: Player 1 wins with high card: Ace
        Given a new deal
        And Player 1 is dealt 2H 3D 5S 9C KD
        And Player 2 is dealt 2C 3H 4S 8C AH
        When hands are compared
        Then Player 2 is the winner
        # And they win with "High Card: Ace"

    Scenario: An example full house 4 over 2
        Given a new deal
        And Player 1 is dealt 2H 4S 4C 2D 4H
        And Player 2 is dealt 2S 8S AS QS 3S
        When hands are compared
        Then Player 1 is the winner
    
    Scenario: Player 1 wins with high card: 9
        Given a new deal
        And Player 1 is dealt 2H 3D 5S 9C KD
        And Player 2 is dealt 2C 3H 4S 8C KH
        When hands are compared
        Then Player 2 is the winner
    
    Scenario: Player 2 wins with King of Hearts beats Diamonds
        Given a new deal
        And Player 1 is dealt 2H 3D 5S 9C KD
        And Player 2 is dealt 2D 3H 5C 9S KH
        When hands are compared
        Then Player 2 is the winner
