Feature: Trello Card API
	As a user I want to use Boards API and perform Get,Post And Delete operations


    Scenario: GET boards of id
		Given the user defines a GET request to members/{id}/boards
		When the user sends the request
		Then verify the status code is 200
		And verify the user recives all the boards linked to their account 

	Scenario: Get all information of board 
		Given the user defines a GET request to boards/{idBoard}
		When the user sends the request
		Then verify the status code is 200
		And verify the information agrees

	Scenario: Get specific information of board 
		Given the user defines a GET request to boards/{idBoard} with fields that wants to retrive
		When the user sends the request
		Then verify the status code is 200
		And verify the fields agree 

    Scenario: Uptdate specific information of board 
		Given the user defines a PUT request to boards/{idBoard} with fields that wants to update
		When the user sends the request
		Then verify the status code is 200
		And verify the fields were updated

    Scenario: Create a board 
		Given the user defines a POST request to boards/ with fields that wants to create
		When the user sends the request
		Then verify the status code is 200
		And verify the board was created

     Scenario: Delete a board 
		Given the user defines a DELETE request to boards/{idBoard} 
		When the user sends the request
		Then verify the status code is 200
		And verify the board was deleted 

     Scenario: GET membership of Board
		Given the user defines a GET request to /boards/{id}/memberships
		When the user sends the request
		Then verify the status code is 200
		And verify the user recives the memberships

    Scenario: Get Actions of a Board
		Given the user defines a GET request to boards/{boardId}/action
		When the user sends the request
		Then verify the status code is 200
		And verify the user recives the actions

    Scenario: Get card of a Board
		Given the user defines a GET request to boards/{id}/cards/{idCard}
		When the user sends the request
		Then verify the status code is 200
		And verify the user recives the cards

    Scenario: Get boardStars on a Board
		Given the user defines a GET request to boards/{boardId}/boardStars
		When the user sends the request
		Then verify the status code is 200
		And verify the user recives the board stars

    Scenario: Get Checklists on a Board
		Given the user defines a GET request to boards/{id}/checklists
		When the user sends the request
		Then verify the status code is 200
		And verify the user recives the checklists

    Scenario: Create Checklist on a Board
		Given the user defines a POST request to boards/{id}/checklists
		When the user sends the request
		Then verify the status code is 200
		And verify the checklist is created

    Scenario: Create a Label on a Board
		Given the user defines a POST request to boards/{id}/labels
		When the user sends the request
		Then verify the status code is 200
		And verify the label is created

    Scenario: Get Lists on a Board
		Given the user defines a POST request to boards/{id}/lists
		When the user sends the request
		Then verify the status code is 200
		And verify the user recives the lists
