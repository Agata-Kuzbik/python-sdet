import re
from playwright.sync_api import expect


def test_check_titlt_and_product_card(page, base_url):

    page.goto(f"{base_url}/products")
    expect(page).to_have_title(re.compile("TestMarket Lab"))
    expect(page.get_by_test_id("product-card").first).to_be_visible()