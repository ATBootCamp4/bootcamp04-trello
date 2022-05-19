"""
Test module used to verify that an user can work with Boards

Classes:
    TestBoards
"""

from main.trello.api.members_manager import MembersManager
from main.trello.api.boards_manager import BoardsManager


class TestBoards():
    
    @classmethod
    def setup_class(cls):
        """ Initialze the managers used to interact with the API """
        cls.boards_manager = BoardsManager()
        cls.members_manager = MembersManager()

    def test_create_board(self):
        """Test to verify boards can be created, listed and deleted
        
        STEPS:
        1. Create a new Board
        2. Verify the API response comes with the status code 200 an Board's data
        3. Verify the new Board exists
        4. Verify the board can be deleted
        """
        name = "TestBoard"
        description = "Test the creation of a board"
        status_code, created_board = self.boards_manager.create_board(name, description=description)
        # 1. verify status code
        assert status_code == 200, f"Couldn't create a board with name '{name}' and description '{description}'"
        # 2. verify can new board exists
        status_code, board = self.boards_manager.get_board(created_board['id'])
        assert created_board['name'] == name, f"Board name is {created_board['name']} but it was expected {name}"
        assert created_board['desc'] == description, f"Board name is {created_board['desc']} " \
                                                     f"but it was expected {description}"
        # 3. verify member can see it in the list
        status_code, board_list = self.members_manager.get_boards(fields='name')
        for member_board in board_list:
            if member_board['id'] == created_board['id']:
                break
        else:
            raise AssertionError("Member cannot see listed the board {} " \
                                 "with name '{}'".format(created_board['id'], created_board['name']))
        # 4. Delete created board
        status_code, _ = self.boards_manager.delete_board(created_board['id'])
        assert status_code == 200, f"Board {created_board['id']} with '{name}' couldn't be deleted"

    def test_copy_board(self):
        
        name1 = "boardToBeCloned1"
        name2 = "boardCloned1"
        
        status_code, board_to_be_cloned = self.boards_manager.create_board(name1 )
        assert status_code == 200, f"Couldn't create a board with name '{name1}'"
        assert board_to_be_cloned['name'] == name1, f"Board name is {board_to_be_cloned['name']} but it was expected {name1}"
        #create the board to be cloned and assert its name and status code response 
        
        status_code1, created_board = self.boards_manager.copy_board(name2, board_to_be_cloned['id'] )
        assert status_code1 == 200, f"Couldn't copy the board with name '{name2}'"
        assert created_board['name'] == name2, f"Board name is {created_board['name']} but it was expected {name2}"
        #copy the board to be cloned and create the cloaned board with the copied information and asserted its name and status code
        
        status_code3, _ = self.boards_manager.delete_board(created_board['id'])
        assert status_code3 == 200, f"Board {created_board['id']}  couldn't be deleted"
        status_code4, _ = self.boards_manager.delete_board(board_to_be_cloned['id'])
        assert status_code4 == 200, f"Board {board_to_be_cloned['id']}  couldn't be deleted"
        #delete the created boards and assert their status code response 

    def test_update_boards_name(self):
        
        name1 = "boardToUpdated"
        informationToUpdate = { "name": "updatedName" }
        
        
        status_code, board_to_be_updated = self.boards_manager.create_board(name1 )
        assert status_code == 200, f"Couldn't create a board with name '{name1}'"
        assert board_to_be_updated['name'] == name1, f"Board name is {board_to_be_updated['name']} but it was expected {name1}"
        #create the board to be updated and assert its name and status code response

        status_code2, updated_board = self.boards_manager.update_board(board_to_be_updated['id'], informationToUpdate )
        assert status_code2 == 200, f"Board {board_to_be_updated['id']}  couldn't be updated"
        assert board_to_be_updated['id'] == updated_board['id'], f"updated Board id is {updated_board['id']} but it was expected {board_to_be_updated['id']} "
        assert updated_board['name'] == informationToUpdate['name'], f"Board name is {updated_board['name']} but it was expected { informationToUpdate['name']} "
        #updates the board and verifies that has the same id but the name was chanched 

        status_code3, _ = self.boards_manager.delete_board(updated_board['id'])
        assert status_code3 == 200, f"Board {updated_board['id']}  couldn't be deleted"
        #delete the created boards and assert their status code response 

    def test_update_boards_description(self):
        
        description1 = "this is the old description"
        informationToUpdate = { "desc": "new description" }
        
        
        status_code, board_to_be_updated = self.boards_manager.create_board("name1" , description1 )
        assert status_code == 200, f"Couldn't create a board with name name1"
        assert board_to_be_updated['desc'] == description1, f"Board description is {board_to_be_updated['desc']} but it was expected {description1}"
        #create the board to be updated and assert its name and status code response

        status_code2, updated_board = self.boards_manager.update_board(board_to_be_updated['id'], informationToUpdate )
        assert status_code2 == 200, f"Board {board_to_be_updated['id']}  couldn't be updated"
        assert board_to_be_updated['id'] == updated_board['id'], f"updated Board id is {updated_board['id']} but it was expected {board_to_be_updated['id']} "
        assert updated_board['desc'] == informationToUpdate['desc'], f"Board description is {updated_board['desc']} but it was expected { informationToUpdate['desc']} "
        #updates the board and verifies that has the same id but the name was chanched 

        status_code3, _ = self.boards_manager.delete_board(updated_board['id'])
        assert status_code3 == 200, f"Board {updated_board['id']}  couldn't be deleted"
        #delete the created boards and assert their status code response 

