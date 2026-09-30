import requests
from playwright.sync_api import expect
from pages.products_page import ProductsPage

def test_search_with_page_object(page, base_url):
    requests.post(f"{base_url}/api/reset")
    products = ProductsPage(page, base_url).goto().search("keyboard")

    expect(products.cards).to_have_count(1)