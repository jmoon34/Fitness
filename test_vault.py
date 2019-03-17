import json
import unittest
from Food import Food
from Vault import Vault



class TestVault(unittest.TestCase):
    def test_date_to_string(self):
        self.assertEqual(Vault.date_to_string(2018, 1, 1), "2018-01-01")
        self.assertEqual(Vault.date_to_string(2018, 4, 21), "2018-04-21")
        self.assertEqual(Vault.date_to_string(2018, 10, 1), "2018-10-01")
        self.assertEqual(Vault.date_to_string(2018, 12, 12), "2018-12-12")

    def test_get_dict_from_file(self):
        v = Vault()
        v.get_food_dict_from_file()
        self.assertTrue(v.food_dict)

    def test_write_dict_to_file(self):
        v = Vault()
        v.get_food_dict_from_file()
        v.write_food_dict_to_file()

    def test_add_food_entry(self):
        food1 = Food("Apple", 100)
        food2 = Food("Egg", 50)
        vault = Vault()
        vault.add_food_journal_dict_entry("test", food1)
        vault.add_food_journal_dict_entry("test", food2)
        with open("FoodJournal/FoodJournaltest.json", 'r') as fp:
            test_dict = json.load(fp)
        self.assertEqual(test_dict[0]["Apple"], 100)
        self.assertEqual(test_dict[0]["Egg"], 50)


