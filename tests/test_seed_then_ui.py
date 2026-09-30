import requests
from playwright.sync_api import expect

def test_products_page_shows_the_seed(page, base_url):
    requests.post(f"{base_url}/api/reset")


    page.goto(f"{base_url}/products")
    expect(page.get_by_test_id("product-card")).to_have_count(15)