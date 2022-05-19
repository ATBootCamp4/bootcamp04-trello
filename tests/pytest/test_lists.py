#from main.trello.api.members_manager import MembersManager
from main.trello.api.lists_manager import ListsManager
from main.utils.common_globals import ID_LIST, NAME_LIST, NAME_BOARD

class TestLists():

    @classmethod
    def setup_class(cls):
        cls.lists_manager = ListsManager()
    
    def test_create_list(self):
        name = 'List 123'
        status_code = self.lists_manager.create_list(name)
        # 1. verify status code
        assert status_code[0] == 200
    
    def test_get_list(self):
        status_code = self.lists_manager.get_list(ID_LIST)
        # 1. verify list name
        assert status_code[1]['name'] == NAME_LIST, f"List name is {status_code[1]['name']} but it was expected {NAME_LIST}"
    
    def test_get_board_list_is_on(self):
        status_code = self.lists_manager.get_board_list_is_on(ID_LIST)
        # 1. verify the board name the list is on
        assert status_code[1]['name'] == NAME_BOARD, f"Board name is {status_code[1]['name']} but it was expected {NAME_BOARD}"