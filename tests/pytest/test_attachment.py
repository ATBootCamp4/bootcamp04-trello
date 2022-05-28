from main.trello.api.attachments_manager import AttachmentsManager


class TestAttachments():

    @classmethod
    def setup_class(cls):
        cls.attachments_manager = AttachmentsManager()

    def test_create_attachment_from_url(self):

        name = "Attachment from PyTest"
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Pytest_logo.svg/640px-Pytest_logo.svg.png"
        card_id = "6281250ff6f1e04b7edd712c"

        status_code, response = self.attachments_manager.create_attachment_from_url(url=url, card_id=card_id, name=name)
        # 1. Verify the status code
        assert status_code == 200, f"Expected status code 200, but received: {status_code}"
        # 2. Verify the attachment exists
        attachment_id = response.get('id')
        status_code, response = self.attachments_manager.get_attachment(card_id, attachment_id)
        assert status_code == 200, f"Expected status code 200, but received: {status_code}"
        # 3. Verify the attachment has the correct name
        attachment_name = response.get('name')
        assert attachment_name == name, f"Expected name: {name}, but received: {attachment_name}"
        # 4. Verify the attachment can be deleted
        status_code, _ = self.attachments_manager.delete_attachment(card_id, attachment_id)
        assert status_code == 200, f"Expected status code 200, but received: {status_code}"

    def test_create_attachment_from_file(self):

        name = "File attachment from PyTest"
        path = "C:\\Users\\mefe\\Documents\\API Testing\\repo\\requirements.txt"
        card_id = "6281250ff6f1e04b7edd712c"

        response = self.attachments_manager.create_attachment_from_file(path=path, card_id=card_id, name=name)
        assert response.status_code == 200, f"Expected status code 200, but received: {response.status_code}"
