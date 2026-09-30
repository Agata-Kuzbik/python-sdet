
class LoginPage:

    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

        # locators — the page's selectors, in ONE place
        self.email = page.get_by_label("Email")
        self.password = page.get_by_label("Password")
        self.submit = page.get_by_test_id("login-submit")

    def goto(self):
        self.page.goto(f"{self.base_url}/auth/login")
        return self

    def login(self, email, password):
        self.email.fill(email)
        self.password.fill(password)
        self.submit.click()
