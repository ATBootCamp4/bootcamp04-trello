Feature: Trello API Checklists
    As a user
    I want "Checklists" API endpoints
    In order to manipulate checklists

    Scenario Outline: GET all checklists on a card
        Given I created a checklist on a card with id:"<card_id>"
        When I send a GET request to /cards/"<card_id>"/checklists
        Then I receive a list with at least one checklist
        And the status code is 200

        Examples:
            | card_id                  |
            | 6281250ff6f1e04b7edd712c |
    
    Scenario Outline: GET a checklist by id
        Given there is an already created checklist
        When I send a GET request to /checklists/"<checklist_id>"
        Then I receive a response with id:"<checklist_id>"
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
        When I send a PUT request to /checklists/"<checklist_id>"
        And the payload contains "<name>" and "<pos>"
        Then the checklist is updated
        And the status code is 200

        Examples:
            | checklist_id             | name       | pos    |
            | 628134e46a25c3826ba7e345 | updated    | top    |
    
    Scenario Outline: DELETE a checklist
        Given there is an already created checklist
        When I send a DELETE request to /checklists/"<checklist_id>"
        Then the checklist is deleted
        And the status code is 200

        Examples:
            | checklist_id             |
            | 62865f12a0f63a6e324d465c |
    
    Scenario Outline: GET all completed checklist items on a card
        Given there is a card with completed checklist items
        When I send a GET request to /cards/"<card_id>"/checkItemStates
        Then I receive a list with at least one completed checklist item
        And the status code is 200

        Examples:
            | card_id                  |
            | 6281250ff6f1e04b7edd712c |

    Scenario Outline: GET all checklist items on a checklist
        Given there is an already created checklist containing items
        When I send a GET request to /checklists/"<checklist_id>"/checkItems
        Then I receive a list with at least one checklist item
        And the status code is 200

        Examples:
            | checklist_id             |
            | 628134e46a25c3826ba7e345 |

    Scenario Outline: POST a new checklist item to a checklist
        Given there is an already created checklist
        When I send a POST request to /checklists/"<checklist_id>"/checkItems
        And the payload contains "<name>","<pos>", and "<checked>"
        Then the checklist item is created on the checklist
        And the status code is 200

        Examples:
            | checklist_id             | name       | pos    | checked |
            | 628134e46a25c3826ba7e345 | item1      | bottom | false   |
            | 628134e46a25c3826ba7e345 | item2      | top    | true    |

    Scenario Outline: GET a checklist item by its id
        Given there is an already created checklist item
        When I send a GET request to checklists/"<checklist_id>"/checkItems/"<checkItem_id>"
        Then I receive a response with id:"<checkItem_id>"
        And the status code is 200

        Examples:
            | checklist_id             | checkItem_id             |
            | 628134e46a25c3826ba7e345 | 62865f12a0f63a6e324d465c |

    Scenario Outline: Update a checklist item
        Given there is an already created checklist item
        When I send a PUT request to /cards/"<card_id>"/checkItems/"<checkItem_id>"
        And the payload contains "<name>", "<state>" and "<pos>"
        Then the checklist item is updated
        And the status code is 200

        Examples:
            | card_id                  | checkItem_id             | name       | state    | pos    |
            | 6281250ff6f1e04b7edd712c | 628134ecb6de363a8c43fbb0 | updated    | complete | top    |

    Scenario Outline: DELETE a checklist item
        Given there is an already created checklist item
        When I send a DELETE request to /checklists/"<checklist_id>"/checkItems/"<checkItem_id>"
        Then the checklist item is deleted
        And the status code is 200

        Examples:
            | checklist_id             | checkItem_id             |
            | 628134e46a25c3826ba7e345 | 628134ecb6de363a8c43fbb0 |

    Scenario Outline: Create a checklist with two incomplete items, and then complete one of them
        Given I created a new checklist
        And I send two POST requests to /checklists/:checklist_id/checkItems
        And the payloads contains "<name>", "<checked>" and "<pos>"
        When I send a PUT request to /checklists/:checklist_id/checkItems/:checkItem_id
        And the payload contains "<state>"
        Then the checklist item is updated
        And the status code is 200

        Examples:
            | name       | checked      | pos    | state    |
            | item       | incomplete   | bottom | complete |