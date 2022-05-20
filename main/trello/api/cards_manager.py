from main.trello.api.rest_base_manager import RESTBaseManager


LISTS = 'lists'
CARDS = 'cards'
ID_LIST = '62819bac13025107d7d01cf8'


class CardsManager(RESTBaseManager):

    def __init__(self, method=None):
        super().__init__(method)

    def get_cards_from_list(self, list_id, **kwargs):

        endpoint = f"{LISTS}/{list_id}/{CARDS}"

        status_code, response = self.method.get_request(endpoint, **kwargs)

        return status_code, response

    def get_card(self, idCard, fields='all', **kwargs):

        endpoint = f"{CARDS}/{idCard}"
        if isinstance(fields, str):
            kwargs = {**kwargs, 'fields': fields}

        status_code, response = self.method.get_request(endpoint, **kwargs)

        return status_code, response

    def create_card_on_list(self, idList, name="TestWithPython", description="This is a test from python", **kwargs):

        endpoint = f"{CARDS}"

        payload = {
            "name": name,
            "desc": description,
            "idList": idList,
        }

        if kwargs:
            payload = {**kwargs, **payload}

        status_code, response = self.method.post_request(
            endpoint, payload=payload)

        return status_code, response

    def delete_card_from_list(self, idCard):

        endpoint = f"{CARDS}/{idCard}"

        return self.method.delete_request(endpoint)

    def update_card_from_list(self, idCard, name="TestWithPython", description="This is a test from python", **kwargs):

        endpoint = f"{CARDS}/{idCard}"

        payload = {
            "name": name,
            "desc": description,
        }

        if kwargs:
            payload = {**kwargs, **payload}

        status_code, response = self.method.put_request(
            endpoint, payload=payload)

        return status_code, response
