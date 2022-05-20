Feature: Trello API attachments
    As a user
    I want "Attachments" API endpoints
    In order to manipulate attachments

    Scenario: GET all attachments from a card
        Given I created a new card
        And the card has an attachment
        When I send a "GET" request to "/cards/{card}/attachments"
        Then I receive a list with at least one attachment
        And the status code is "200"

    Scenario: GET an attachment from a card
        Given I created a new card
        And the card has an attachment
        When I send a "GET" request to "/cards/{card}/attachments/{attachment}"
        Then I receive a response with the "attachment" id
        And the status code is "200"

    Scenario: POST an attachment to a card from an url
        Given I created a new card
        When I send a "POST" request to "/cards/{card}/attachments"
            | Key      | Value                                          |
            | url      | https://www.svgrepo.com/show/354463/trello.svg |
            | name     | Trello logo                                    |
            | setCover | False                                          |
        Then the attachment is created on the card
        And the status code is "200"