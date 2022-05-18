Feature: Trello Members API
    As a user I want to use the Members API and consume the responses

    Scenario: GET request to Members
        Given the user defines a GET request to /boards/id/members
        When the user sends the request
        Then verify the status code is 200
        And verify there is at least 1 member

    Scenario: GET request to Members
        Given the user asked list of members in board NSNSN        
        Then verify there is at least 1 member
        When the user selected the firt member
        And the user updated the member name to DDDD
        Then verify name name is DDD

branch format: nicolas/task-feature-labels-boards

branch trainer: task-features
     task-features
        nicolas
            labels.feature
            boards.feature
        pablo
            load.features