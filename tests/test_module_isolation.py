
def test_add_product(base_url, api):
    response = api.post(
        f"{base_url}/api/products",
        json= {"name": "Testowy", "price" : 10.11, "category": "electronics"}
    )

    new_product = response.json()

    assert response.status_code == 201
    assert "id" in new_product
    assert new_product["name"] == "Testowy"
    

def test_product_count_is_15_after_reset(reset_db, base_url, api):
    response = api.get(
        f"{base_url}/api/products"
    )
    products = response.json()

    assert len(products) == 15