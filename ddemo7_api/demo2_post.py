import requests
from assertpy import assert_that
import json


class TestPetStoreAPI:
    END_POINT = "https://petstore.swagger.io/v2"

    """Post reques - add pet to store"""

    def get_key(self):
        response=requests.post("https://kbfszrxx5vacidgrgdhqzu25r40vyyuw.lambda-url.eu-central-1.on.aws/api/learners")
        return response.json()['id']

    def generate_token(self):
        header_dic = {"api-token": "78787338ydyhhd"}
        response = requests.post("http://localhost:8080/api/auth/token", headers=header_dic)
        return response.json()['token']

    def test_add_valid_pet(self):
        resource = "/pet"
        json_body = json.load(open("../test_data/add_pet.json"))
        header_dic = {"Content-Type": "application/json"}
        response = requests.post(url=TestPetStoreAPI.END_POINT + resource, headers=header_dic, json=json_body)
        print(response.json())
        assert_that(200).is_equal_to(response.status_code)
        assert_that(json_body["id"]).is_equal_to(response.json()["id"])

    def test_add_valid_pet2(self):
        resource = "/pet"
        json_body = json.load(open("../test_data/add_pet.json"))
        token = self.generate_token()
        header_dic = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        response = requests.post(url=TestPetStoreAPI.END_POINT + resource, headers=header_dic, json=json_body)
        print(response.json())
        assert_that(200).is_equal_to(response.status_code)
        assert_that(json_body["id"]).is_equal_to(response.json()["id"])

    def test_update_valid_pet(self):
        resource = "/pet"
        json_body = json.load(open("../test_data/update_pet.json"))
        header_dic = {"Content-Type": "application/json"}
        response = requests.put(url=TestPetStoreAPI.END_POINT + resource, headers=header_dic, json=json_body)
        print(response.json())
        assert_that(200).is_equal_to(response.status_code)
        assert_that(json_body["name"]).is_equal_to(response.json()["name"])

    def test_delete_valid_pet(self):
        pet_id = 9805
        resource = f"/pet/{pet_id}"
        header_dic = {"api_key": self.get_key()}
        response = requests.delete(TestPetStoreAPI.END_POINT + resource, headers=header_dic)
        print(response.json())
        assert_that(200).is_equal_to(response.status_code)

    def test_delete_invalid_pet(self):
        pet_id = 980555
        resource = f"/pet/{pet_id}"
        header_dic = {"api_key": "89898989sfjhjh"}
        response = requests.delete(TestPetStoreAPI.END_POINT + resource, headers=header_dic)
        print(response.json())
        assert_that(400).is_equal_to(response.status_code)