Feature: Trello API Lists
    As a user
    I want "Lists" API endpoints
    In order to manipulate lists

    Scenario: GET all lists in a board
        Given I created a list in a board with id:"<id_board>"
        When I send a GET request to /boards/"<id_board>"/lists
        Then I receive a list with at least one list
        And the status code is 200

        Examples:
            | id_board                 |
            | 627c0cb01e98336259fa1ae2 |
    
    Scenario: GET a list by id
        Given there is an already created list
        When I send a GET request to lists/"<id_list>"
        Then I receive a response with id:"<id_list>"
        And the status code is 200

        Examples:
            | id_list                  |
            | 627c0cb01e98336259fa1ae4 |

            