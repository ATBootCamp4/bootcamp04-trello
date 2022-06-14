Feature: Test for Trello cards
    As a user I want to be able to manage cards

    Background: Needs to be logged in
        Given the user is logged in
        And the board "Example_board" is selected

    @wip
    Scenario: Create a Card on Trello
        When the user clicks on button "create_a_card_button"
        And send input value "Example card" to field "create_card_input"
        And the user clicks on button "submit_create_card_button"
        And the user clicks on button "submit_create_card_button"
        Then element "Example_card" is displayed
