Feature: Trello Boards API
    As a user I want to use Boards API and perform Get,Post And Delete operations
   
   Scenario: Get all information of board 
        When I send a "GET" request to "/boards/{board}"
        Then the status code is "200"
        And I receive a response with the "board" schema

    Scenario: Get members of board 
        When I send a "GET" request to "/boards/{board}/members"
        Then the status code is "200"
        And verify there is at least 1 member
    
    Scenario: Updating information of a Board
        When I send a "PUT" request to "/boards/{board}"
            | Key         | Value                      |
            | name        | testingnicolasv            |
            | desc        | a valid data table         |
        Then the status code is "200"
        And verify the new object contains the following info
            | Key         | Value                      |
            | name        | testingnicolasv            |
            | desc        | a valid data table         | 


     Scenario Outline: CREATE and DELETE a board 
        Given the user creates a board with "<field>" to be "<value>"
        Then the status code is "200"
        And I receive a response with the "board" schema
        Then the user deletes the board "<value>"
        And the status code is "200"

    Examples:
        | field | value     |
        | name  | kiara     |
        | name  | jose      |