def test_login_empty_body(base_url,api):
    response = api.post(
        f"{base_url}/api/auth/login", 
        json= {}
    )

    assert response.status_code == 400

def test_add_product_missing_full_data(base_url, api):
    response = api.post(
        f"{base_url}/api/products",
        json= {"name": "Testowy"}
    )
    assert response.status_code == 400

def test_register_missing_name(base_url, api):
    response = api.post(
        f"{base_url}/api/auth/register",
        json= {"password": "whatever",
               "email": "agata@post.pl"}
    )

    assert response.status_code == 400


def test_wrong_password(base_url, api):
    response = api.post(
        f"{base_url}/api/auth/login",
        json= {
            "email": "customer@test.io",
            "password": "wrongpass"
        }
    )

    assert response.status_code == 401

def test_unknown_email(base_url, api):
    response = api.post(
        f"{base_url}/api/auth/login",
        json= {
            "email": "ghost@test.io",
            "password": "whatever"
        }
    )
    assert response.status_code == 401


def test_get_not_existed_product(base_url, api):
    response = api.get(
        f"{base_url}/api/products/99999"
    )

    assert response.status_code == 404

def test_update_not_existed_product(base_url, api):
    response = api.put(
        f"{base_url}/api/products/99999",
        json= {
            "name": "Update product"
        }
    )

    assert response.status_code == 404

def test_delete_not_existed_product(base_url, api):
    response = api.delete(
        f"{base_url}/api/products/99999"
    )

    assert response.status_code == 404

def test_password_too_short(base_url, api):
    response = api.post(
        f"{base_url}/api/auth/register",
        json={
            "email": "customer@test.io",
            "password": "abc"
        }
    )

    assert response.status_code == 400
    assert "password" in response.json()["error"].lower()

   