import requests



def test_products(base_url):
    response = requests.get(f"{base_url}/api/products")
    assert response.status_code== 200