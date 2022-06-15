Feature: Trello Boards API
    As a user I want to use Boards API and perform Get,Post And Delete operations
   
   @smoke @get_board_info
   Scenario: Get all information of board 
        Given A board is created
        When I send a "GET" request to "/boards/{board}"
        Then the status code is "200"
        And I receive a response with the "board" schema
        
        
    @smoke 
    Scenario: Get members of board 
        Given A board is created
        When I send a "GET" request to "/boards/{board}/members"
        Then the status code is "200"
        And I receive a list with at least "1" "member"
        
        
    @smoke
    Scenario: Updating information of a Board
        Given A board is created
        When I send a "PUT" request to "/boards/{board}"
            | Key         | Value                      |
            | name        | testingnicolasv            |
            | desc        | a valid data table         |
        Then the status code is "200"
        And verify the new object contains the following info
            | Key         | Value                      |
            | name        | testingnicolasv            |
            | desc        | a valid data table         | 

    
    @smoke
    Scenario Outline: CREATE and DELETE a board 
        Given the user creates a board with "<field>" to be "<value>"
        Then the status code is "200"
        And I receive a response with the "board" schema
        Then the user deletes the board "<value>"
        When I send a "GET" request to "/boards/{response}"
        Then the status code is "404"

    Examples:
        | field | value     |
        | name  | kiara     |
        | name  | jose      |
        | name  | Nicolas   |
        | name  | keila     |
        | name  | Vallejo   |
        | name  | pabon     |


    @negative
    Scenario: Updating information of a Board negative
        Given A board is created
        When I send a "PUT" request to "/boards/{board}"
            | Key         | Value              |
            | nagrsgsgsdg | testxcasv          |
            | dvcv        | a vxxtable         |
        Then the status code is "200"
        

    @negative 
    Scenario: Get members of board negative
        Given A board is created
        When I send a "GET" request to "/boards/{board}/dgzdgz"
        Then the status code is "404"


    @negative
    Scenario Outline: Get a board negative
        Given I send a "GET" request to "<endpoint>"
        Then the status code is "<status_code>"

         Examples:
        | endpoint                               | status_code |
        | /boards/6290f7ea8abc4849607f0a52       | 404         |
        | /boards/6290f7ea8abc484                | 400         |
        | /boards/628bb6a0f8621c367f942e6b       | 404         |
        | /boards/6290f7ea8abc4H4                | 400         |
        | /boards/6290f7ea8abc4H4                | 400         |

