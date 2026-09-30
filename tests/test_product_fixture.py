def test_new_product_is_listed(product, base_url, api):
    response = api.get(
        f"{base_url}/api/products"
    )
    print(response.json())
    assert product["id"] in [p["id"] for p in response.json()]


def test_temporary_product_exists(product_without_reset, base_url, api):
    response = api.get(
        f"{base_url}/api/products/{product_without_reset['id']}"
    )

    assert response.status_code == 200