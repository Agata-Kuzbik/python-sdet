
class ProductsPage:

    def __init__(self,page, base_url):
        self.page = page
        self.base_url = base_url

        self.search_input = page.get_by_test_id("search-input")
        self.apply = page.get_by_test_id("apply-filters")
        self.cards = page.get_by_test_id("product-card")

    def goto(self):
        self.page.goto(f"{self.base_url}/products")
        return self

    def search(self, term):
        self.search_input.fill(term)
        self.apply.click()
        return self