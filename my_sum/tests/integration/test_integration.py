import unittest

class TestBasic(unittest.TestCase):
    def setUp(self):
        self.app = App(database='fixtures/cards.json')
    
    def test_card_count(self):
        self.assertEqual(len(self.app.cards), 100)

    def test_existance_of_customer(self):
        card = self.app.get_card(id='60cc383898d4f9382c70c49f')
        self.assertEqual(card.cardType, 'Encounter')

if __name__ == '__main__':
    unittest.main()