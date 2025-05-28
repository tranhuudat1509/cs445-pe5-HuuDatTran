import unittest
import json
from main_app import app

class TestTaskAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_1_get_tasks_details(self):
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), dict)

    def test_2_post_tasks_details(self):
        payload = {
            "4": {"title": "New task", "done": False}
        }
        response = self.client.post('/tasks', 
                                    data=json.dumps(payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("4", response.get_json())

if __name__ == '__main__':
    unittest.main()
