from playwright.sync_api import expect


def test_login_succeeds(page, base_url):
    page.goto(f"{base_url}/auth/login")
    page.get_by_label("Email").fill("customer@test.io")
    page.get_by_label("Password").fill("customer123")
    page.get_by_test_id("login-submit").click()

    expect(page).to_have_url(f"{base_url}/")                       # redirected home
    expect(page.get_by_test_id("flash-success")).to_contain_text("Logged in")
    expect(page.get_by_test_id("nav-logout")).to_be_visible()     # now signed in