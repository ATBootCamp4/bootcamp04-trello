Feature: Trello Organizations API
    As a user I want to use the Organizations API and consume the responses
    
    Background: Create organization
        Given the user defines a "POST" request to "/organizations"
            | Key         | Value                      |
            | displayName | TestDelete41               |
        When the user sends the request
        Then verify the status code is "200"
        And validate the schema of "organizations"

    Scenario: PUT request to Organizations        
        Given the user defines a "PUT" request to "/organizations/{organizations}"
            | Key         | Value                      |
            | displayName | TestDelete71               | 
        When the user sends the request
        Then verify the status code is "200"
        And verify the new object contains the following info
            | Key         | Value                      |
            | displayName | TestDelete71               | 
        When the user defines a "Delete" request to "/organizations/{organizations}"
        And the user sends the request
        
    Scenario: Delete request to Organizations        
        Given the user defines a "Delete" request to "/organizations/{organizations}"
        When the user sends the request
        Then verify the status code is "200"
        When the user defines a "Get" request to "/organizations/{organizations}"
        And the user sends the request
        Then verify the status code is "404"
