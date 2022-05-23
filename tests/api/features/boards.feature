Feature: Trello Members API
    As a user I want to use Boards API and perform Get,Post And Delete operations

    Scenario: GET boards of id
        Given the user defines a "GET" request to "members/me/boards"
        When the user sends the request
        Then verify the status code is "200"
        And verify the user recives a "13" lengt item 
   
   
    Scenario: Get all information of board 
        Given the user defines a "GET" request to "/boards/623cd8eef6a5ea0970e67c12"
        When the user sends the request
        Then verify the status code is "200"
        And verify the user recives a "12" lengt item 


    Scenario: GET memebers of board
        Given the user defines a "GET" request to "/boards/628bac3b8c7a64298edf2b72/members"
        When the user sends the request
        Then verify the status code is "200"
        And verify there is at least 1 member

    Scenario: Updating information of a Board
        Given the user defines a "PUT" request to "/boards/628bac3b8c7a64298edf2b72"
            | Key         | Value                      |
            | name        | testingnicolasv            |
            | desc        | a valid data table         |
        When the user sends the request
        Then verify the status code is "200"
        And verify the new object contains the following info
            | Key         | Value                      |
            | name        | testingnicolasv            |
            | desc        | a valid data table         | 

    Scenario: Updating information of a Board and verify the board
        Given the user defines a "PUT" request to "/boards/628bac3b8c7a64298edf2b72"
            | Key         | Value                      |
            | name        | testingnicolasv            |
            | desc        | a valid data table         |
        When the user sends the request
        Then verify the status code is "200"
        And verify the board contains the following info
            | Key         | Value                      |
            | name        | testingnicolasv            |
            | desc        | a valid data table         |

   

    Scenario Outline: CREATE and DELETE a board 
        Given the user creates a board with "<field>" to be "<value>"
        Then verify the status code is "200"
        And validate the schema of "board"
        When the user deletes the board "<value>"
        And verify the board "<value>" doesnt exist

    Examples:
        | field | value     |
        | name  | kiara     |
        | name  | jose      |
        
        
        
      

    
    
    Scenario Outline: Duplicate a Board and DELETE it
        
        Given  the user copy the board with "<id>" and new "<name>"
        Then verify the status code is "200"
        Then verify the duplicated board and the "<id>" have same info
        When the user deletes the board "<name>"
        And verify the board "<name>" doesnt exist
    Examples:
        | id | name    |
        | 628bac3b8c7a64298edf2b72 | kiara12     |
       
        


    Scenario: GET actions of board
        Given the user defines a "GET" request to "/boards/623cd8eef6a5ea0970e67c12/actions"
        When the user sends the request
        Then verify the status code is "200"
        And verify the user recives a "50" lengt item 

    Scenario: GET checklist of board
        Given the user defines a "GET" request to "/boards/627c0cb01e98336259fa1ae2/checklists"
        When the user sends the request
        Then verify the status code is "200"
        And verify the user recives a "1" lengt item 

    

    Scenario: GET labels of board
        Given the user defines a "GET" request to "/boards/627c0cb01e98336259fa1ae2/labels"
        When the user sends the request
        Then verify the status code is "200"
        And verify the user recives a "9" lengt item 


    Scenario: CREATE label of board
        Given the user defines a "POST" request to "/boards/627c0cb01e98336259fa1ae2/labels"
        | Key         | Value                      |
        | name        |kiarajose12                 |
        | color        |orange                |
        When the user sends the request
        Then verify the status code is "200"
        And verify the new object contains the following info
        | Key         | Value                      |
        | name        |kiarajose12                 |	
        | color       |orange               |	

      
       
    