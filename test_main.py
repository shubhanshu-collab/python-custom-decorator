import unittest
from main import api_call_function

# Unit test cases
class TestDecoratorFunction(unittest.TestCase):
    def test_application_json(self):
        result = api_call_function("application.json")
        self.assertEqual(result, "This function is used to call custom decorator with name: application.json and version: 2.0")

    def test_application_xml(self):
        result = api_call_function("application.xml")
        self.assertEqual(result, "This function is used to call custom decorator with name: application.xml and version: 3.0")

    def test_default(self):
        result = api_call_function("")
        self.assertEqual(result, "This function is used to call custom decorator with name: None and version: None")

if __name__ == '__main__':
    unittest.main()