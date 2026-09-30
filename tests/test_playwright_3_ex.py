from playwright.sync_api import expect

def test_search_with_filter(reset_db, page, base_url):

    page.goto(f"{base_url}/products")
    page.get_by_test_id("search-input").fill("keyboard")
    page.get_by_test_id("apply-filters").click()


    expect(page.get_by_test_id("product-card")).to_have_count(1)
    expect(page.get_by_text("Mechanical Keyboard")).to_be_visible()

    

