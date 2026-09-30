import pytest

def test_create_order(reset_db, base_url, api):
    create_order = api.post(
        f"{base_url}/api/orders",
        json= {"email": "customer@test.io", "items": [{"product_id": 1, "quantity": 3}]}
    )


    order = create_order.json()

    get_order = api.get(
        f"{base_url}/api/orders"
    )
    check_order = get_order.json()
    

    assert create_order.status_code == 201
    assert order["total"] == pytest.approx(29.99 * 3)
    assert get_order.status_code == 200
    assert any(o["total"] == pytest.approx(29.99 * 3) for o in check_order)

