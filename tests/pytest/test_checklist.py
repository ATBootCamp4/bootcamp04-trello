from main.trello.api.checklists_manager import ChecklistsManager

class TestChecklists():

    @classmethod
    def setup_class(cls):
        cls.checklists_manager = ChecklistsManager()

    def test_create_checklist(self):

        name = "Checklist from PyTest"
        card_id = "6281250ff6f1e04b7edd712c"

        status_code, response = self.checklists_manager.create_checklist(name=name, card_id=card_id)
        # 1. Verify the status code
        assert status_code == 200, f"Expected status code 200, but received: {status_code}"
        # 2. Verify the checklist exists
        checklist_id = response.pop('id')
        status_code, response = self.checklists_manager.get_checklist(checklist_id)
        assert status_code == 200, f"Expected status code 200, but received: {status_code}"
        # 3. Verify the checklist has the correct name
        checklist_name = response.pop('name')
        assert checklist_name == name, f"Expected name: {name}, but received: {checklist_name}"
        # 4. Verify the checklist can be deleted
        status_code, _ = self.checklists_manager.delete_checklist(checklist_id)
        assert status_code == 200, f"Expected status code 200, but received: {status_code}"

    def test_get_checklist(self):

        c_id = "628134e46a25c3826ba7e345"

        status_code, response = self.checklists_manager.get_checklist(c_id, check_items='all', checkitem_fields='name,pos,state', fields='all')
        # 1. Verify the status code
        assert status_code == 200, f"Expected status code 200, but received: {status_code}"
        # 2. Verify it is the correct checklist
        checklist_id = response.pop('id')
        assert checklist_id == c_id, f"Expected id: {c_id}, but received: {checklist_id}"