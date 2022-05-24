Feature: Trello API Lists
    As a user
    I want "Lists" API endpoints
    In order to manipulate lists

    Scenario Outline: GET all lists in a board
        Given I send a GET request to /boards/"<id_list>"/lists
        When I receive a response with at least one list
        Then the status code is "<code>"

        Examples:
            | id_list                   | code|
            | 627c0cb01e98336259fa1ae4  | 200 |
    
    Scenario Outline: GET a list by id
        Given I send a GET request to lists/"<id_list>"
        When I receive a response with id: "<id_list>"
        Then status code is "<code>"
    
    Examples:
            | id_list                   | code|
            | 627c0cb01e98336259fa1ae4  | 200 |
            | 627c0cb01e98336259fa1ae5  | 200 |
