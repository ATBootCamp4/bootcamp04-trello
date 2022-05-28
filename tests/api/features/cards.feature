Feature: Trello Card API
	As a user I want to use Cards Members API and perform Get,Post,Put and Delete operations
	
	Scenario: Create a Card on a List
		When I send a "POST" request to "cards"
			| Key    | Value           |
			| name   | TestCardUpdate  |
			| desc   | Testdescupdated |
			| idList | {id}:list       |
		Then the status code is "200"
		And I receive a response with the "cards" schema
		And The item "cards/{response}" is created

	Scenario: Modify information of a Card
		Given I created a new card
		When I send a "PUT" request to "cards/{card}"
			| Key    | Value           |
			| name   | TestCardUpdate  |
			| desc   | Testdescupdated |
		Then the status code is "200"
		And The item is updated
			| Key    | Value           |
			| name   | TestCardUpdate  |
			| desc   | Testdescupdated |
		And I receive a response with the "cards" schema

	Scenario: Create a comment on a Card
		Given I created a new card
		When I send a "POST" request to "cards/{card}/actions/comments"
			| Key    | Value             |
			| text   | Commenttext       |
		Then the status code is "200"
		And I receive a response with the "comment_on_card" schema
		And verify the comment has been added
		
	Scenario: Delete a Card
		Given I created a new card
		When I send a "DELETE" request to "cards/{card}" 
		Then the status code is "200"
		And The item "cards/{card}" is deleted

	Scenario: Modify a Comment in a Card
		Given I created a new card
		And I created a comment in the card
		When I send a "PUT" request to "cards/{card}/actions/{comment}/comments"
			| Key    | Value             		 |
			| text   | UpdatedCommenttext        |
		Then the status code is "200"
	
	Scenario: Delete a Comment in a card
		Given I created a new card
		And I created a comment in the card
		When I send a "DELETE" request to "cards/{card}/actions/{comment}/comments"
		Then the status code is "200"
		And verify the comment has been deleted