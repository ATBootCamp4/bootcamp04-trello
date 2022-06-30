@lists_gui @fixture.after.delete.board @fixture.before.create.board
Feature: Trello UI Lists
    As a User I want to be able to make CRUD operations with lists

    
    Background: The user is logged in
        Given the user is logged in
        When the user goes to board "CreateBoardExample"

    @lists @create_list @fixture.after.delete.list
    Scenario: Create list
        And the user sends the list name "ListTest"
        Then the list is displayed
        And the list appears in the API


    @lists @update_list @fixture.before.create.list @fixture.after.delete.list 
    Scenario: Update list name
        And the user updates the list name "ListTest" to "ListUpdate"
        Then the list is displayed
        And the list appears in the API

    @lists @delete_list @fixture.before.create.list
    Scenario: Delete list
        And the user deletes the list "ListTest"
        Then the list should not be displayed
        And the list should not appear in the API