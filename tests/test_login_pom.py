from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login_with_page_object(page, base_url):
    #login_page = LoginPage(page, base_url)
    #login_page.goto()
    #login_page.login("customer@test.io", "customer123")

    #shorter 
    LoginPage(page, base_url).goto().login("customer@test.io", "customer123")

    expect(page.get_by_test_id("nav-logout")).to_be_visible()