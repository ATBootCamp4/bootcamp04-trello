Feature: Trello Card API
	As a user I want to use Cards Members API and perform Get,Post,Put and Delete operations
	
	Scenario: Create a Card on a List
		Given I created a new card
		Then the status code is "200"
	
	Scenario: Modify information of a Card
		Given I created a new card
		When I send a "PUT" request to "cards/{card}"
			| Key    | Value           |
			| name   | TestCardUpdate  |
			| desc   | Testdescupdated |
		Then the status code is "200"
		And the card is updated
			| Key    | Value           |
			| name   | TestCardUpdate  |
			| desc   | Testdescupdated |

	Scenario: Create a comment on a Card
		Given I created a new card
		When I send a "POST" request to "cards/{card}/actions/comments"
			| Key    | Value             |
			| text   | Commenttext       |
		Then the status code is "200"
		And verify the comment has been added
			| Key    | Value             |
			| text   | Commenttext       |

	Scenario: Delete a Card
		Given I created a new card
		When I send a "DELETE" request to "cards/{card}" 
		Then the status code is "200"