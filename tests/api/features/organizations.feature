Feature: Trello Organizations API
    As a user I want to use the Organizations API and consume the responses

    Scenario: POST request to Organizations
        Given the user defines a "POST" request to "/organizations"
            | Key         | Value                      |
            | displayName | TestDelete4                | 
            | name        | testDelete004sd             |
            | desc        | a valid data table         |
            | website     | https://www.bootcamp04.xyz |  
        When the user sends the request
        Then verify the status code is "200"        
        And verify the new object contains the following info
            | Key         | Value                      |
            | displayName | TestDelete4                | 
            | name        | testDelete004sd            |
            | desc        | a valid data table         |
            | website     | https://www.bootcamp04.xyz |           
        