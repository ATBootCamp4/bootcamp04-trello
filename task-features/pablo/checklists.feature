Feature: Trello API Checklists
    As a user
    I want "Checklists" API endpoints
    In order to manipulate checklists

    Scenario Outline: GET all checklists on a card
        Given there is a card with checklists
        When I send a GET request to /cards/<card_id>/checklists
        Then I receive a list with at least one checklist
        And the status code is 200

        Examples:
            | card_id                  |
            | 6281250ff6f1e04b7edd712c |
    
    Scenario Outline: GET a checklist by id
        Given there is an already created checklist
        When I send a GET request to /checklists/<checklist_id>
        Then I receive a response with id:<checklist_id>
        And the status code is 200

        Examples:
            | checklist_id             |
            | 628134e46a25c3826ba7e345 |

    Scenario: POST a new checklist to a card
        Given there is an already created card
        When I send a POST request to /checklists with the following payload:
            | name       | idCard                   | pos    |
            | checklist1 | 6281250ff6f1e04b7edd712c | bottom |
        Then the checklist is created on the card
        And the status code is 200

    Scenario Outline: Update a checklist
        Given there is an already created checklist
        When I send a PUT request to /checklists/<checklist_id>
        And the payload contains <name> and <pos>
        Then the checklist is updated
        And the status code is 200

        Examples:
            | checklist_id             | name       | pos    |
            | 628134e46a25c3826ba7e345 | updated    | top    |
    
    Scenario Outline: DELETE a checklist
        Given there is an already created checklist
        When I send a DELETE request to /checklists/<checklist_id>
        Then the checklist is deleted
        And the status code is 200

        Examples:
            | checklist_id             |
            | 62865f12a0f63a6e324d465c |
    