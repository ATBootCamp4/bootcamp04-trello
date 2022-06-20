Feature: Test for Trello boards
    As a user I want to be able to manage boards

    Background: Needs to be logged in
        Given the user is logged in


    Scenario: Create a Board on Trello
        When the user clicks on button "create_a_board_button"
        And send input value "Test" to field "create_board_input"
        And the user clicks on button "submit_create_board_button"
        Then a board is created
