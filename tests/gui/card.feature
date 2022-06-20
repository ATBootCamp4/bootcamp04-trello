Feature: Test for Trello cards
    As a user I want to be able to manage cards

    Background: Needs to be logged in
        Given the user is logged in
        And the board "Example_board" is selected

    @wip
    Scenario: Create a Card on Trello
        When the user create a card "Example card3"
        Then element "Example card3" is displayed

    # Scenario: Update a Card
    #     When the user update "Example_card" name with "Another_name"
    #     Then element "Another_name" is displayed