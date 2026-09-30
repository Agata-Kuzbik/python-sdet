import pytest
import requests

@pytest.fixture
def base_url():
    return "http://localhost:3000"

def test_products(base_url):
    response = requests.get(f"{base_url}/api/products")
    assert response.status_code== 200