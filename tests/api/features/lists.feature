Feature: Trello API Lists
    As a user
    I want "Lists" API endpoints
    In order to manipulate lists

    Scenario: GET all lists in a board
        Given I created a board
        And I created a list on the board with name "list 22"
        When I send a "GET" request to "boards/{board}/lists"
        Then I receive a list with at least "1" "list"
        And the status code is "200"

    Scenario: GET a list by id
        Given I created a board
        And I created a list on the board with name "list 22"
        When I send a "GET" request to "/lists/{list}"
        Then I receive a response with the "list" id
        And the status code is "200"

    Scenario: POST a new list to a board
        Given I created a board
        When I send a "POST" request to "/lists"
            | Key     | Value        | 
            | name    | list 1       |
            | idBoard | {id}:board   | 
        Then I receive a response with the "list" schema
        And the status code is "200"
        When I send a "GET" request to "/lists/{response}"
        Then I check the data is
            | Key     | Value        | 
            | name    | list 1       |
            | idBoard | {id}:board   | 
