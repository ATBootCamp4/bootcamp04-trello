Feature: Trello UI Boards
    As a User I want to be able to make CRUD and other operations with boards

    Background: The user is logged in
        Given the user is logged in

    Scenario: Create a board
        When the user sends the boards name "CreateBoardExample"
        Then the board is created

    Scenario: Update board title
        When the user goes to board "CreateBoardExample"
        And the user sends the new board name "UpdateBoardExample"
        Then the board is updated
        
    Scenario: Delete board
        When the user goes to board "UpdateBoardExample"
        And the user deletes the board
        Then the board should not be displayed