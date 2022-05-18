from main.trello.api.label_manager import LabelsManager


class TestLabels():
    
    @classmethod
    def setup_class(cls):
        cls.labels_manager = LabelsManager()
    
    def test_create_label(self):
    # 1. verify status code    
        status_code, created_label = self.labels_manager.create_label('yellow','yellow')
        assert status_code == 200, f"Couldn't create a label"

     # 2. verify new label existance
        status_code, label = self.labels_manager.get_label(created_label['id'])
        assert created_label['id'] == label['id']

    # 3. Delete created label
        status_code, _ = self.labels_manager.delete_label_board(created_label['id'])
        assert status_code == 200, f"Label {created_label['id']} couldn't be deleted" 
 

