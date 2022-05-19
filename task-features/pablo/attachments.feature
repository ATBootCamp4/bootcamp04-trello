Feature: Trello API attachments
    As a user
    I want "Attachments" API endpoints
    In order to manipulate attachments

    Scenario: GET all attachments from a card
        Given there is a card with attachments
        When I request to GET all attachments from that card
        Then I receive a list that contains at least one attachment
        And the status code is 200

    Scenario: GET an attachment from a card
        Given there is a card with attachments
        When I request to GET a specific attachment from that card
        Then I receive a single attachment
        And the status code is 200

    Scenario: POST an attachment to a card from an url
        Given there is a card
        And I have an attachment url
        When I request to POST that url to that card
        Then the attachment is created in the card
        And the status code is 200

    Scenario: POST an attachment to a card from a file
        Given there is a card
        And I have an attachment file
        When I request to POST that file to that card
        Then the attachment is created in the card
        And the status code is 200

    Scenario: DELETE an attachment from a card
        Given there is a card with attachments
        When I request to DELETE an attachment from that card
        Then the attachment is deleted from the card
        And the status code is 200

    Scenario: POST a cover image to a card
        Given there is a card
        And I have an image's url
        When I send a POST request to the attachment endpoint with the following payload:
            | name  | url                                    | setCover |
            | cover | https://source.unsplash.com/user/c_v_r | true     |
        Then the cover image is created in the card
        And the status code is 200