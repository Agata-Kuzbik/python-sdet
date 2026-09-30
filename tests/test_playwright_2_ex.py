from playwright.sync_api import expect

def test_check_email_label_in_three_ways(page, base_url):

    page.goto(f"{base_url}/auth/login")
    
    expect(page.get_by_label("Email")).to_be_visible()
    expect(page.get_by_role("textbox", name= "Email")).to_be_visible()
    expect(page.locator("#email")).to_be_visible()