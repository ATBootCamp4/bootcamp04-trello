Feature: Trello API Lists
    As a user
    I want "Lists" API endpoints
    In order to manipulate lists

    @smoke
    Scenario: GET all lists in a board
        Given A board is created
        And I created a list on the board with name "list 22"
        When I send a "GET" request to "boards/{board}/lists"
        Then I receive a list with at least "1" "list"
        And the status code is "200"

    Scenario: GET a list by id
        Given A board is created
        And I created a list on the board with name "list 22"
        When I send a "GET" request to "/lists/{list}"
        Then I receive a response with the "list" "id"
        And the status code is "200"

    @smoke
    Scenario: POST a new list to a board
        Given A board is created
        When I send a "POST" request to "/lists"
            | Key       | Value        |
            | name      | list 1       |
            | idBoard   | {id}:board   |
        Then I receive a response with the "list" schema
        And the status code is "200"
        When I send a "GET" request to "/lists/{response}"
        Then I check the data is
            | Key       | Value        |
            | name      | list 1       |
            | idBoard   | {id}:board   |

    Scenario: Update a list name
        Given I created a list on the board with name "list 22"
        When I send a "PUT" request to "/lists/{list}"
            | Key       | Value        |
            | name      | list33       |
        Then I check the data is
            | Key       | Value        |
            | name      | list33       |
        And the status code is "200"

    Scenario: Archive a list
        Given I created a list on the board with name "list 22"
        When I send a "PUT" request to "/lists/{list}"
            | Key       | Value        |
            | closed    | true         |
        Then I check the data is
            | Key       | Value        |
            | closed    | true         |
        And the status code is "200"
