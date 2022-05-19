Feature: Trello Members API
    As a user I want to use the Members API and consume the responses

    Scenario: GET request to Members
        Given the user defines a "GET" request to "/boards/6281405050ec165192c2f521/members"
        When the user sends the request
        Then verify the status code is "200"
        And verify there is at least 1 member

    