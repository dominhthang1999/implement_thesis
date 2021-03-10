import unittest
import main


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
