def test_product_crud_lifecycle(reset_db, base_url, api):

    #CREATE
    created = api.post(
        f"{base_url}/api/products", 
        json = {"name": "Lifecycle Lamp", "price": 39.99, "category": "furniture"}
    )

    assert created.status_code == 201
    prodcut_id = created.json()["id"]

    #READ
    read = api.get(
        f"{base_url}/api/products/{prodcut_id}"
    )

    assert read.status_code == 200
    assert read.json()["name"] == "Lifecycle Lamp"

    #UPDATE
    update = api.put(
        f"{base_url}/api/products/{prodcut_id}", json = {"price": 2.00}
    )

    assert update.status_code == 200
    assert update.json()["price"] == 2.00

    #DELETE
    delete = api.delete(
        f"{base_url}/api/products/{prodcut_id}"
    )

    assert delete.status_code == 200

    #CONFIRM GONE
    gone = api.get(
        f"{base_url}/api/products/{prodcut_id}"
    )

    assert gone.status_code == 404