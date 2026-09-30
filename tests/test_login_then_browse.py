import requests
from playwright.sync_api import expect
from pages.products_page import ProductsPage
from pages.login_page import LoginPage


def test_login_then_browse(page, base_url):
    requests.post(f"{base_url}/api/reset")

    LoginPage(page, base_url).goto().login("customer@test.io", "customer123")
    expect(page.get_by_test_id("nav-logout")).to_be_visible()

    products = ProductsPage(page, base_url).goto()
    expect(products.cards.first).to_be_visible()