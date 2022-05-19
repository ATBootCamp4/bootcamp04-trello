Feature: Trello Card API
	As a user I want to use Cards Members API and perform Get,Post And Delete operations
	
	Scenario: POST request to Cards
		Given the user defines a POST request with name,desc and idList to 1/cards
		When the user sends the request
		Then verify the status code is 200
		And verify the card is listed on its list
	
	Scenario: DELETE request to Cards
		Given the user defines a DELETE request to 1/cards/{ID} with an existing ID
		When the user sends the request
		Then verify status code is 200