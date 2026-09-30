import pytest


@pytest.mark.parametrize(
    "payload, expected_status",
    [
        ({"name": "Agata", "email": "agata@test.io", "password": "customer123"}, 201),     # new emial valid (control)
        ({"name": "Jakub","email": "customer@test.io", "password": "customer123"}, 409),  # duplicate email
        ({"name": "Paweł", "email": "customer@test.io", "password": "abc"}, 400),          # shrort password
        ({"name": "Wera", "email": "ghost@test.io"}, 400),                                # missing password
                                    
    ],
    ids= ["valid", "duplicated", "too_short_password","missing-password"]
)

def test_register_validation(reset_db, base_url, api, payload, expected_status):
    response = api.post(f"{base_url}/api/auth/register", json=payload)

    assert response.status_code == expected_status