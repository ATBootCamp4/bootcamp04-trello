from main.trello.api.cards_manager import CardsManager


class TestCards():

    @classmethod
    def setup_class(cls):

        cls.cards_manager = CardsManager()

    def test_card_requests(self):

        name = "CardForTest"
        description = "Card created for testing"
        idList = '62819bac13025107d7d01cf8'
        status_code, created_card = self.cards_manager.create_card_on_list(
            idList, name=name, description=description)

        assert status_code == 200, f"Couldn't create a card with name '{name}' and description '{description}' on list '{idList}'"

        status_code, card = self.cards_manager.get_card(created_card['id'])
        assert created_card['name'] == name, f"Card name is {created_card['name']} but it was expected {name}"
        assert created_card['desc'] == description, f"Card name is {created_card['desc']} but it was expected {description}"

        status_code, cards_list = self.cards_manager.get_cards_from_list(
            idList)
        for card in cards_list:
            if card['id'] == created_card['id']:
                break
        else:
            raise AssertionError("Card cannot be seen in the list {} "
                                 "with name '{}'".format(idList, created_card['name']))

        status_code, _ = self.cards_manager.delete_card_from_list(
            created_card['id'])
        assert status_code == 200, f"Card {created_card['id']} with '{name}' couldn't be deleted"
