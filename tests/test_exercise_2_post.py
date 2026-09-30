
def test_add_product_and_verify(reset_db, base_url, api):
    response = api.post(
        f"{base_url}/api/products", 
        json={"name": "Testowy", "price" : 10.11, "category": "electronics"}
    )
    new_product = response.json()

    assert response.status_code == 201
    assert "id" in new_product
    assert new_product["name"] == "Testowy"
    assert new_product["price"] == 10.11