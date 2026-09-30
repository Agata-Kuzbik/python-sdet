

def test_delete_product(reset_db, base_url, api):
    created = api.post(
        f"{base_url}/api/products", json = {"name": "Disposable", "price": 1.00, "category": "accessories"}
    ).json()

    

    product_id = created["id"]

    response = api.delete(f"{base_url}/api/products/{product_id}")

    assert response.status_code == 200

    #it's really gone

    follow_up = api.get(f"{base_url}/api/products/{product_id}")
    assert follow_up.status_code == 404
 
