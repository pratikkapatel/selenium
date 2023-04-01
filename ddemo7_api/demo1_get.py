import requests
from assertpy import assert_that


class TestPetStoreAPI:
    END_POINT = "https://petstore.swagger.io/v2"

    # def test_find_valid_pet_by_id(self):
    #     pet_id=1001
    #     resource=f"/pet/{pet_id}"
    #     response= requests.get(TestPetStoreAPI.END_POINT+resource)
    #     print(response)
    #     print(response.status_code)
    #     print(response.json())
    #         print(response.json())
    #         print(response.json()["id"])
    #         print(response.json()["name"])
    #         print(response.json()["category"])
    #         print(response.json()["category"]["name"])

    """Get-Path parameter - This request should fetch valid pet details based on pet id"""

    def test_find_valid_pet_by_id(self):
        pet_id = 9805
        resource = f"/pet/{pet_id}"
        response = requests.get(TestPetStoreAPI.END_POINT + resource)
        assert_that(200).is_equal_to(response.status_code)
        assert_that(pet_id).is_equal_to(response.json()["id"])
        # assert_that("doggie-5001").is_equal_to(response.json()["name"])

    def test_find_invalid_pet_by_id(self):
        pet_id = 602
        resource = f"/pet/{pet_id}"
        response = requests.get(TestPetStoreAPI.END_POINT + resource)
        assert_that(404).is_equal_to(response.status_code)
        assert_that("Pet not found").is_equal_to(response.json()["message"])
        # print(response.json()["message"])

    """Get-Query parameter - This request should fetch valid pet details based on pet id"""

    def test_find_pet_by_valid_status(self):
        status = "sold"
        resource = f"/pet/findByStatus?status={status}"
        response = requests.get(TestPetStoreAPI.END_POINT + resource)
        # print(response.status_code)
        # print(response.json())
        assert_that(200).is_equal_to(response.status_code)
        print(response.json())
        print(response.json()[0])
        print(len(response.json()))
        print(response.json()[0]['status'])
        # validating all pet details received is having status - sold
        for i in range(0, len(response.json())):
            print(response.json()[i]['id'])
            print(response.json()[i]['status'])
            assert_that(status).is_equal_to(response.json()[i]['status'])

    def test_find_pet_by_invalid_status(self):
        status = "sold123"
        resource = f"/pet/findByStatus?status={status}"
        response = requests.get(TestPetStoreAPI.END_POINT + resource)
        assert_that(400).is_equal_to(response.status_code)