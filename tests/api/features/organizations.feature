Feature: Trello Organizations API
    As a user I want to use the Organizations API and consume the responses

    Scenario: POST request to Organizations
        Given the user defines a "POST" request to "/organizations"
            | Key         | Value                      |
            | displayName | TestDelete4                | 
            | name        | testdelete004              |
            | desc        | a valid data table         |
            | website     | https://www.bootcamp04.xyz |  
        When the user sends the request
        Then verify the status code is "200"
        And verify the new object contains the following info
            | Key         | Value                      |
            | displayName | TestDelete4                | 
            | name        | testdelete004              |
            | desc        | a valid data table         |
            | website     | https://www.bootcamp04.xyz |
        When the user defines a "Delete" request to "/organizations/{organizations}"
        And the user sends the request
        Then verify the status code is "200"
        When the user defines a "Get" request to "/organizations/{organizations}"
        And the user sends the request
        Then verify the status code is "404"

    # Scenario Outline: Create organization with parameterized values
    #     Given the user defines a "POST" request to "/organizations"
    #     And the user sets "<fieldName1>" to be "<value1>"
    #     And the user sets "<fieldName2>" to be "<value2>"
    #     When the user sends the request
    #     Then verify the status code is "<status_code>"
    #     And validate the schema of "organizations"
    #     When the user defines a "Delete" request to "/organizations/{organizations}"
    #     And the user sends the request
    #     Then verify the status code is "200"
    #     When the user defines a "Get" request to "/organizations/{organizations}"
    #     And the user sends the request
    #     Then verify the status code is "404"

    # Examples:
    #     | fieldName1   | value1         | fieldName2 | value2         | status_code |
    #     | displayName  | TestDelete001  | name       | def            |  200        |
    #     | displayName  | TestDelete002  | name       | parsd          |  200        |
    #     | displayName  | TestDelete003  | website    | smtp://ddd.com |  200        |