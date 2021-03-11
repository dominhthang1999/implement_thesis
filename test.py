import unittest
import main
import json


class Testing(unittest.TestCase):
    def test_get_coordinate(self):
        center = {
            'x': 0,
            'y': 0
        }
        size = {
            'x': 10,
            'y': 10
        }
        top_left, bottom_right = main.get_coordinates(center, size)

        # Testing 
        self.assertEqual(top_left[0], -5)
        self.assertEqual(top_left[1], 5)
        self.assertEqual(bottom_right[0], 5)
        self.assertEqual(bottom_right[1], -5)

    def test_connect_db(self):
        # Test check type data input
        path = 3
        self.assertEqual(None, main.get_database(path))
        path_url = "mongodb+srv://user:ye1gkjKBIWGxjVEpUFxCoAjNnAdEeRYpiLeE4guhP4FxUHtGYCPMzdd11TtoJAyA" \
                   "@multidisciplinary-lt0bz.azure.mongodb.net/<dbname>?authSource=admin&replicaSet=Multidisciplinary" \
                   "-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true "
        db = main.get_database(path_url)
        self.assertTrue(db)

    def test_get_default_size_for_roi(self):
        with open('input_json.json') as input_json:
            input_json = json.load(input_json)
            DEFAULT_SIZE = main.get_default_size_for_roi(input_json['json_file']['labels'])
            self.assertEqual(31, DEFAULT_SIZE)
