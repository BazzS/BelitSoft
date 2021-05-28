import requests
import json
import unittest

class TestPetStoreUser(unittest.TestCase):

    def payload_create(self):
        return { "id": 12349, "username": "BigBob", "firstName": "Bob", "lastName": "Dilan", "email": "BobDilan@gmail.com", "password": "123pass", "phone": "+7954324656", "userStatus":0}

    def header(self):
        return {'Content-Type': 'application/json'}

    def test1_create_user(self):
        res = requests.post('https://petstore.swagger.io/v2/user', data=json.dumps(self.payload_create()), headers=self.header())
        self.assertEqual(res.status_code, 200)
        print("Test 1 complete")

    def test2_read_user(self):
        res = requests.get('http://petstore.swagger.io/v2/user/BigBob')
        self.assertEqual(res.status_code, 200)
        print("Test 2 complete")

    def test3_update_user(self):
        res = requests.put('https://petstore.swagger.io/v2/user/BigBob', data=json.dumps(self.payload_create()), headers=self.header())
        self.assertEqual(res.status_code, 200)
        print("Test 3 complete")

    def test4_delete_user(self):
        res = requests.delete('https://petstore.swagger.io/v2/user/BigBob')
        self.assertEqual(res.status_code, 200)
        print("Test 4 complete")


if __name__ == '__main__':
    unittest.main()
