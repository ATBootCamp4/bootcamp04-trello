Feature: Trello Members API
    As a user I want to use Boards API and perform Get,Post And Delete operations

    Scenario: GET boards of id
        Given the user defines a "GET" request to "members/me/boards"
        When the user sends the request
        Then verify the status code is "200"
        And verify the user recives a "7" lengt item 
   
   
    Scenario: Get all information of board 
        Given the user defines a "GET" request to "/boards/623cd8eef6a5ea0970e67c12"
        When the user sends the request
        Then verify the status code is "200"
        And verify the user recives a "12" lengt item 


    Scenario: GET memebers of board
        Given the user defines a "GET" request to "/boards/623cd8eef6a5ea0970e67c12/members"
        When the user sends the request
        Then verify the status code is "200"
        And verify there is at least 1 member

    Scenario: Updating information of a Board
        Given the user defines a "PUT" request to "/boards/6287b012e56fca6695059571"
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
        Given the user defines a "PUT" request to "/boards/6287b012e56fca6695059571"
            | Key         | Value                      |
            | name        | testingnicolasv            |
            | desc        | a valid data table         |
        When the user sends the request
        Then verify the status code is "200"
        And verify the board contains the following info
            | Key         | Value                      |
            | name        | testingnicolasv            |
            | desc        | a valid data table         |

    Scenario: CREATE and DELETE a board
        Given the user defines a "POST" request to "/boards"
            | Key         | Value                      |
            | name        | testingnicolasv            |
            | desc        | a valid data table         |
        When the user sends the request
        Then verify the status code is "200"
        And verify the new object contains the following info
            | Key         | Value                      |
            | name        | testingnicolasv            |
            | desc        | a valid data table         | 
        And DELETE a Board

      

    Scenario: CREATE and DELETE a board2
        Given the user defines a create_board function
            | Key         | Value                      |
            | name        |kiarajose12                 |
           
        When the user calls the create_board function
        Then verify the status code is "200"
        And verify the new object contains the following info
            | Key         | Value                      |
            | name        | kiarajose12            |
        And DELETE a Board

    
    
    Scenario: Duplicate a Board and DELETE it
        Given the user defines a duplicate function with id "6287b86ed19bf5054179cb2f" and new name "NewName"
        When the user sends the copy_board function
        Then verify the status code is "200"
        And DELETE a Board


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

      
       
    