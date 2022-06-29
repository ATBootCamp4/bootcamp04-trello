@boards_gui
Feature: Trello UI Boards
    As a User I want to be able to make CRUD and other operations with boards


    Background: The user is logged in
        Given the user is logged in

    @boards @create_board @fixture.after.delete.board
    Scenario: Create a board
        When the user sends the boards name "CreateBoardExample"
        Then the board "CreateBoardExample" is displayed
        And the board appears in the API

    @boards @update_board @fixture.before.create.board @fixture.after.delete.board
    Scenario: Update board title
        When the user goes to board "CreateBoardExample"
        And the user sends the new board name "UpdateBoardExample"
        Then the board "CreateBoardExample" is updated with name "UpdateBoardExample"
        And the board appears in the API

    @boards @delete_board @fixture.before.create.board
    Scenario: Delete board
        When the user goes to board "CreateBoardExample"
        And the user deletes the board
        Then the board should not be displayed
        And the board should not appear in the API