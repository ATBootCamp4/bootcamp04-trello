Feature: Trello Card API
	As a user I want to use Cards Members API and perform Get,Post And Delete operations
	
	Scenario: POST request to Cards to create one
		Given the user defines a "POST" request to "cards"
			| Key    | Value     |
			| name   | TestCard  |
			| desc   | Testdesc  |
			| idList | {idList}  |
		When the user sends the request
		Then verify the status code is "200"
	
	Scenario: PUT request to Card
		Given the user defines a "PUT" request with name and desc to "cards/{idCard}"
			| Key    | Value           |
			| name   | TestCardUpdate  |
			| desc   | Testdescupdated |
		When the user sends the request for updating
		Then verify the status code is "200" for updating
		And verify the card name and desc is updated

	Scenario: POST request to create Comment on Card
		Given the user defines a "POST" request to "cards/{idCard}/actions/comments" with text for a comment
			| Key    | Value             |
			| text   | Commenttext       |
		When the user sends the request for creating comment
		Then verify the status code is "200" for commenting
		And verify the comment has been added to the card

	Scenario: DELETE request to Cards
		Given the user defines a "DELETE" request to "cards/{idCard}" with an existing ID
		When the user sends the request for deleting
		Then verify status code is "200" for deleting