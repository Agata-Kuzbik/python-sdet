
def test_update_new_product(reset_db, base_url, api):
    new_product = api.post(
        f"{base_url}/api/products",
        json={"name": "Testowy", "price" : 10.11, "category": "electronics"}
    )

    product = new_product.json()
    id_product = product["id"]

    assert new_product.status_code == 201
    assert "id" in product


    update_product = api.put(
        f"{base_url}/api/products/{id_product}",
        json= {"price": 1}
    )
    updated_product = update_product.json()

    assert update_product.status_code == 200
    assert updated_product["price"] == 1