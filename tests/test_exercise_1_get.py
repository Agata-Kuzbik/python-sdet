
def test_read_single_product_exist(base_url,api):
    response = api.get(
        f"{base_url}/api/products/1"
    )

    product = response.json()

    assert response.status_code == 200
    assert isinstance(product, dict)
    assert "id" in product
    assert "name" in product
    assert "price" in product

def test_read_single_product_doesnt_exist(base_url, api):
    response = api.get(
            f"{base_url}/api/products/99999"
        )

    assert response.status_code == 404
