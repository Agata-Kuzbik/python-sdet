import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:3000"


@pytest.fixture
def api():
    session = requests.Session()
    yield session
    session.close()


@pytest.fixture
def reset_db(base_url):
    requests.post(f"{base_url}/api/reset")
    yield

@pytest.fixture
def make_product(reset_db, base_url, api):
    count = 0

    def _make(**overrides):
        nonlocal count
        count += 1

        payload = {
            "name": f"Product {count}",
            "price": 1.99,
            "category": "electronics"
        }

        payload.update(overrides)

        return api.post(
            f'{base_url}/api/products',
            json= payload
        ).json()

    return _make

@pytest.fixture
def product(reset_db, base_url, api):
    response = api.post(
        f"{base_url}/api/products",
        json= {"name": "Testowy", "price" : 10.11, "category": "electronics"}
    )
    product = response.json()

    return product


@pytest.fixture
def product_without_reset(base_url, api):
    # SETUP
    response = api.post(
        f"{base_url}/api/products",
        json={
            "name": "Temporary Product",
            "price": 10.00,
            "category": "electronics"
        }
    )
    product = response.json()

    # przekazujemy produkt do testu
    yield product

    # TEARDOWN
    api.delete(
        f"{base_url}/api/products/{product['id']}"
    )
