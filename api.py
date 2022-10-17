import requests


class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"
    def get_api_key(self, email, password):


        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""

        try:
           result = res.json()
        except:
            result = res.text
        return status, result
    def post_information_about_new_pet_without_photo(self, auth_key, name, animal_type, age, pet_photo):
        string = {'auth_key': auth_key, 'name': name,'animal_type': animal_type}
        number = {'age': age}
        file = {'pet_photo': pet_photo}
        res = requests.post(self.base_url+'/api/create_pet_simple', string=string, number=number)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except:
            result = res.text
        return status, result