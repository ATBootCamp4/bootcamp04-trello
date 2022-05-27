from urllib import response
from main.trello.api.rest_base_manager import RESTBaseManager

"""
Module to manage Trello Lists through the API

Classes:
    ListsManager
"""
class ListsManager(RESTBaseManager):
    """Class which can be used to manage Trello Lists through the API"""

    def __init__(self, request_method=None):
        super().__init__(request_method)
        """ Construct the necessary attributes for the ListsManager

        :param method: obj  RequestManager object which is used to handle the API requests
        """
    
    def create_list(self, name, idBoard):
        """ Create a List in a Board

        :param name: str   Name of the List
        :param idBoard:  str   ID of the Board to which the List belongs
        :return: Tuple that contains the status code and the response.
        """
        endpoint = f"lists/?name={name}&idBoard={idBoard}"
        payload = { "name": name}
        status_code, response = self.method.post_request(endpoint, payload)
        return status_code, response

    def get_list(self, idList):
        """ Get a List by ID

        :param idList: str   ID of the List
        :return: Tuple that contains the status code and the response.
        """
        endpoint = f"lists/{idList}"
        status_code, response = self.method.get_request(endpoint)
        return status_code, response
        
    def get_board_list_is_on(self, idList):
        """ Get the Board to which the List belongs by List ID

        :param idList: str   ID of the List
        :return: Tuple that contains the status code and the response.
        """
        endpoint = f"lists/{idList}/board"
        status_code, response = self.method.get_request(endpoint)
        return status_code, response
    
    def get_all_list(self, idBoard):
        """ Get all Lists by ID

        :param idBoard: str   ID of the Board to which the Lists belongs
        :return: Tuple that contains the status code and the response.
        """
        endpoint = f"boards/{idBoard}/lists"
        status_code, response = self.method.get_request(endpoint)
        return status_code, response
