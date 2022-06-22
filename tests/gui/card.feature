@crud
Feature: Test for Trello cards
    As a user I want to be able to manage cards

    Background: Needs to be logged in
        Given the user is logged in
        And the board "Example_board" is selected

    @create_card
    Scenario: Create a Card on Trello
        When the user create a card "Example card" in the list "List example"
        Then the card in the list "List example" shows "Example card"

    @update_card
    Scenario: Update a Card
        When the user update the last card name in the list "List example" with "Another_name"
        Then the card in the list "List example" shows "Another_name"

    @delete_card
    Scenario: Delete a Card
        When the user delete the card "Another_name"
        Then the card "Another_name" is not shown in the list "List example"