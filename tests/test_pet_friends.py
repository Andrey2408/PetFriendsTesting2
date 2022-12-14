from api import PetFriends
from settigs import valid_email, valid_password


pf = PetFriends()


def test_get_api_key_for_valid(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_valid_data(name='Бусик', animal_type='Бенгальская', age='6', pet_photo='images/kot1.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo )
    assert status == 200
    assert result['name'] == name
