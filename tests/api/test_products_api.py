import requests
import pytest



def get_json(base_url,path):
    return requests.get(f"{base_url}{path}").json()

@pytest.mark.smoke
def test_products_returns_a_nonempty_list(base_url):
    response = requests.get(f"{base_url}/api/products")
    assert response.status_code == 200
    products = response.json()
    assert isinstance(products, list)
    assert len(products) > 0


def test_each_product_has_core_fields(base_url):
    products = get_json(base_url,"/api/products")
    assert products                      # guard: an empty list would pass the loop vacuously
    for product in products:
        assert "id" in product
        assert "name" in product
        assert "price" in product


def test_category_filter_returns_only_that_category(base_url):
    response = requests.get(
        f"{base_url}/api/products", params={"category": "electronics"}
    )
    assert response.status_code == 200
    products = response.json()
    assert len(products) > 0
    assert all(p["category"] == "electronics" for p in products)



def test_category_filter_returns_only_category_accessories(base_url):
    response = requests.get(
        f"{base_url}/api/products", params={"category": "accessories"}
    )
    assert response.status_code == 200
    products = response.json()
    assert len(products) > 0
    assert all(p["category"] == "accessories" for p in products)

def test_search_returns_keyboard_product(base_url):
    response = requests.get(
        f"{base_url}/api/products", params={"search": "keyboard"}
    )
    assert response.status_code == 200
    products = response.json()
    assert len(products) > 0
    assert any( "keyboard" in p["name"].lower() for p in products)


def test_session_for_two_requests(api,base_url):
    response_1 = api.get(f"{base_url}/api/products")
    response_2 = api.get(f"{base_url}/api/products/1")

    assert response_1.status_code == 200
    assert response_2.status_code == 200

def test_add_product(reset_db, api, base_url):
    products_before = api.get(f"{base_url}/api/products").json()
    print(len(products_before))
    response = api.post(f"{base_url}/api/products",
        json={
            "name": "Test Product",
            "price": 10.99,
            "category": "electronics"
        })
    products_after = api.get(f"{base_url}/api/products").json()
    print(len(products_after))
    

    assert response.status_code == 201
    assert len(products_after) == 16


def test_reset_restores_initial_product_count(reset_db, api, base_url):
    products_before = api.get(f"{base_url}/api/products").json()
    print(len(products_before))

    assert len(products_before) == 15

    
@pytest.mark.xfail
def test_assert():
    assert 2 == 3