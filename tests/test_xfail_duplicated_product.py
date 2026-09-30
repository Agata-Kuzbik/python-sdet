import pytest


@pytest.mark.xfail(
    reason="BUG: duplicate product name returns 500 instead of 409",
    strict=True
)
def test_duplicate_product_name_should_conflict(reset_db, base_url, api):
    payload = {
        "name": "Repeat Item",
        "price": 9.99,
        "category": "electronics"
    }

    # pierwszy produkt - przygotowujemy dane
    api.post(
        f"{base_url}/api/products",
        json=payload
    )

    # drugi raz ten sam produkt
    duplicate = api.post(
        f"{base_url}/api/products",
        json=payload
    )

    # oczekujemy, że API poprawnie zgłosi konflikt
    assert duplicate.status_code == 409