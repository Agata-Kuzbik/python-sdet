import requests
from playwright.sync_api import expect

def test_check_num_of_products(reset_db, page, base_url):

    page.goto(f"{base_url}/products")
    expect(page.get_by_test_id("product-card")).to_have_count(15)

    requests.post(
        f"{base_url}/api/products",
        json= {
            "name": "Test Product",
            "price": 10.99,
            "category": "electronics"
        }
    )

    page.goto(f"{base_url}/products")
    expect(page.get_by_test_id("product-card")).to_have_count(16)