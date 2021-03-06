Feature: Trello API Checklists
    As a user
    I want "Checklists" API managers
    In order to manipulate checklists

    @smoke
    Scenario: GET all checklists on a card
        Given I created a new card
        And I created a checklist on the card
        When I send a "GET" request to "/cards/{card}/checklists"
        Then I receive a list with at least "1" "checklist"
        And the status code is "200"

    Scenario: GET a checklist by id
        Given I created a new card
        And I created a checklist on the card
        When I send a "GET" request to "/checklists/{checklist}"
        Then I receive a response with the "checklist" "id"
        And the status code is "200"

    @negative
    Scenario: GET a checklist by unexisting id
        Given I created a new card
        And I created a checklist on the card
        When I send a "GET" request to "/checklists/X"
        Then the status code is "400"

    @smoke
    Scenario: POST a new checklist to a card
        Given I created a new card
        When I send a "POST" request to "/checklists"
            | Key    | Value        | 
            | name   | Checklist 1  |
            | pos    | bottom       |
            | idCard | {id}:card    | 
        Then the checklist is created on the card
        And the status code is "200"

    @negative
    Scenario: POST a new checklist with an invalid pos to a card
        Given I created a new card
        When I send a "POST" request to "/checklists"
            | Key    | Value        | 
            | name   | name         |
            | pos    | right        |
            | idCard | {id}:card    |
        Then the response contains the message "invalid"
        And the status code is "400"

    Scenario: Update a checklist
        Given I created a new card
        And I created a checklist on the card
        When I send a "PUT" request to "/checklists/{checklist}"
            | Key    | Value        | 
            | name   | Checklist 1  |
            | pos    | bottom       |
        Then the checklist is updated
        And the status code is "200"

    @negative
    Scenario: Update a checklist with invalid position
        Given I created a new card
        And I created a checklist on the card
        When I send a "PUT" request to "/checklists/{checklist}"
            | Key    | Value        | 
            | name   | Checklist 1  |
            | pos    | right        |
        Then the response contains the message "invalid"
        And the status code is "400"

    @smoke
    Scenario: DELETE a checklist
        Given I created a new card
        And I created a checklist on the card
        When I send a "DELETE" request to "/checklists/{checklist}"
        Then the checklist is deleted
        And the status code is "200"

    Scenario: GET all completed checklist items on a card
        Given I created a new card
        And I created a checklist on the card
        And I created a completed item on the checklist
        When I send a "GET" request to "/cards/{card}/checkItemStates"
        Then I receive a list with at least "1" "checklist item"
        And the status code is "200"

    @smoke
    Scenario: GET all checklist items on a checklist
        Given I created a new card
        And I created a checklist on the card
        And I created a completed item on the checklist
        When I send a "GET" request to "/checklists/{checklist}/checkItems"
        Then I receive a list with at least "1" "checklist item"
        And the status code is "200"

    @smoke
    Scenario: POST a new checklist item to a checklist
        Given I created a new card
        And I created a checklist on the card
        When I send a "POST" request to "/checklists/{checklist}/checkItems"
            | Key     | Value |
            | name    | item1 |
            | pos     | top   |
            | checked | false |
        Then the checklist item is created on the checklist
        And the status code is "200"

    Scenario: GET a checklist item by its id
        Given I created a new card
        And I created a checklist on the card
        And I created a completed item on the checklist
        When I send a "GET" request to "checklists/{checklist}/checkItems/{checkitem}"
        Then I receive a response with the "checkitem" "id"
        And the status code is "200"

    Scenario: Update a checklist item
        Given I created a new card
        And I created a checklist on the card
        And I created a completed item on the checklist
        When I send a "PUT" request to "/cards/{card}/checkItem/{checkitem}"
            | Key   | Value      |
            | name  | updated    |
            | state | incomplete |
            | pos   | top        |
        Then the checklist item is updated
        And the status code is "200"

    @negative
    Scenario: Update a checklist item with invalid state
        Given I created a new card
        And I created a checklist on the card
        And I created a completed item on the checklist
        When I send a "PUT" request to "/cards/{card}/checkItem/{checkitem}"
            | Key   | Value      |
            | name  | updated    |
            | state | something  |
            | pos   | top        |
        Then the response contains the message "invalid"
        And the status code is "400"

    @smoke
    Scenario: DELETE a checklist item
        Given I created a new card
        And I created a checklist on the card
        And I created a completed item on the checklist
        When I send a "DELETE" request to "/checklists/{checklist}/checkItems/{checkitem}"
        Then the checklist item is deleted
        And the status code is "200"