Feature: Trello Card API
	As a user I want to use Cards Members API and perform Get,Post And Delete operations
	
	Scenario: POST request to Cards to create one
		Given the user defines a POST request with name,desc and idList to 1/cards
		When the user sends the request
		Then verify the status code is 200
		And verify the card is listed on its list
	
	Scenario: PUT request to Card
		Given the user defines a PUT request with name and desc to 1/cards/{id}
		When the user sends the request
		Then verify the status code is 200
		And verify the card name and desc is updated

	Scenario: POST request to create Comment on Card
		Given the user defines a POST request to /1/cards/{id}/actions/comments with text for a comment
		When the user sends the request
		Then verify the status code is 200
		And verify the comment has been added to the card

	Scenario: DELETE request to Cards
		Given the user defines a DELETE request to 1/cards/{ID} with an existing ID
		When the user sends the request
		Then verify status code is 200