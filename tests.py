import unittest
import json

from main import get_data


class TestGeneral(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)

    def test_json_decoding(self):
        # Checks whether get_data() returns valid JSON
        # that matches expected results
        data = json.loads(get_data())
        self.assertIsInstance(data, dict)
        self.assertEqual(data["tiam"], "bibendum")
        self.assertEqual(data["lacus"], 23.5)
        self.assertEqual(data["sellus"], False)
