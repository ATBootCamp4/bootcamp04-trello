from main.trello.api.rest_base_manager import RESTBaseManager

CARD_ID = "6281250ff6f1e04b7edd712c"
ATTACHMENT_ID = "6282795810f9624276d93713"

class AttachmentsManager(RESTBaseManager):

    def __init__(self, method=None):
        super().__init__(method)

    def get_all_attachments(self, card_id=CARD_ID):
        """ Get all attachments of a card by its ID,
        :param card_id: str   ID of the card
        :return: Tuple that contains the status code and the response."""

        endpoint = f'cards/{card_id}/attachments'
        status_code, response = self.method.get_request(endpoint)

        return status_code, response

    def get_attachment(self, card_id=CARD_ID ,attachment_id=ATTACHMENT_ID):
        """ Get a specific attachment from a specific card,
        :param card_id:       str    ID of the card
        :param attachment_id: str    ID of the attachment
        :return:              Tuple  that contains the status code and the response."""

        endpoint = f'cards/{card_id}/attachments/{attachment_id}'
        status_code, response = self.method.get_request(endpoint)

        return status_code, response

    def create_attachment_from_url(self, url='https://freeiconshop.com/wp-content/uploads/edd/jpg-solid.png', 
                                    card_id='6281250ff6f1e04b7edd712c', 
                                    name='Attachment from API', 
                                    set_cover=False):
        """ Create a new attachment from an URL,
        :param card_id:       str    ID of the card
        :param name:          str    Name of the attachment
        :param set_cover:     bool   If True, the attachment will be set as the cover of the card
        :param url:           str    URL of the attachment
        :return:              Tuple  that contains the status code and the response."""

        endpoint = f'cards/{card_id}/attachments'
        payload = {
            "url": url, 
            "name": name,
            "setCover": set_cover
        }
        status_code, response = self.method.post_request(endpoint, payload=payload)

        return status_code, response

    def create_attachment_from_file(self, path="C:\\Users\\mefe\\Downloads\\240px-Stoned_Fox.jpg", 
                                    card_id='6281250ff6f1e04b7edd712c', 
                                    name='Attachment from API', 
                                    set_cover=False):
        """ Create a new attachment from a file,
        :param card_id:       str    ID of the card
        :param name:          str    Name of the attachment
        :param set_cover:     bool   If True, the attachment will be set as the cover of the card
        :param path:          str    Path of the file
        :return:              Tuple  that contains the status code and the response."""
        pass

    def delete_attachment(self, card_id=CARD_ID, attachment_id=ATTACHMENT_ID):
        """ Delete a specific attachment from a specific card,
        :param card_id:       str    ID of the card
        :param attachment_id: str    ID of the attachment
        :return:              Tuple  that contains the status code and the response."""

        endpoint = f'cards/{card_id}/attachments/{attachment_id}'
        status_code, response = self.method.delete_request(endpoint)

        return status_code, response
