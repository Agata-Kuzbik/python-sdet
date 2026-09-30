
def test_create_delete_and_verufy_product(reset_db, base_url, api):
    add_product = api.post(
        f"{base_url}/api/products",
        json={"name": "Testowy", "price" : 10.11, "category": "electronics"}
    )
    new_product = add_product.json()
    id_new_product = new_product["id"]
    assert add_product.status_code == 201
    assert "id" in new_product

    delete_product = api.delete(
        f"{base_url}/api/products/{id_new_product}"
    )

    assert delete_product.status_code == 200

    follow_up = api.get(
        f"{base_url}/api/products/{id_new_product}"
    )

    assert follow_up.status_code == 404