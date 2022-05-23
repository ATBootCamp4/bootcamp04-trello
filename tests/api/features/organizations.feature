Feature: Trello Organizations API
    As a user I want to use the Organizations API and consume the responses

    # Scenario: POST request to Organizations
    #     Given the user defines a "POST" request to "/organizations"
    #         | Key         | Value                      |
    #         | displayName | TestDelete4                | 
    #         | name        | testDelete004sd             |
    #         | desc        | a valid data table         |
    #         | website     | https://www.bootcamp04.xyz |  
    #     When the user sends the request
    #     Then verify the status code is "200"        
    #     And verify the new object contains the following info
    #         | Key         | Value                      |
    #         | displayName | TestDelete4                | 
    #         | name        | testDelete004sd            |
    #         | desc        | a valid data table         |
    #         | website     | https://www.bootcamp04.xyz |           
    Scenario Outline: POST request to Organizations Negative (Name)
        Given the user defines a "POST" request to "/organizations"
        And the user sets "<fieldName1>" to be "<value1>"
        And the user sets "<fieldName2>" to be "<value2>"
        When the user sends the request
        Then verify the status code is "<status_code>"
        And validate the schema of "organizations"

    Examples:
        | fieldName1   | value1         | fieldName2 | value2         | status_code |
        | displayName  | TestDelete001  | name       | D              |  200        |
        # | displayName  | TestDelete002  | name       | d@@@           |  200        |
        # | displayName  | TestDelete003  | website    | smtp://ddd.com |  200        |

    # Scenario: POST request to Organizations Negative (website)
    #     Given the user defines a "POST" request to "/organizations"
    #     And the user sets "displayName" to be "TestDelete001"
    #     And the user sets "website" to be "smtp://ddd.com"
    #     When the user sends the request
    #     Then verify the status code is "200"