import json
from pathlib import Path

import pytest

from playwright.sync_api import expect
from pages.login_page import LoginPage

CASES = json.loads((Path(__file__).parent /"data"/"login_cases.json").read_text())

@pytest.mark.parametrize("case",
                         CASES,
                         ids=[f"{c['email'].strip() or 'empty'}->{c['expected']}" for c in CASES])

def test_login_from_json_ui(case, base_url, page):
    LoginPage(page, base_url).goto().login(case["email"], case["password"])
    
    if case["expected"] == 200:
        expect(page.get_by_test_id("nav-logout")).to_be_visible()

    elif case["email"].strip() == "":
        expect(page.get_by_label("Email")).to_have_attribute("required", "")

    elif case["expected"] == 401:
        expect(page.get_by_test_id("flash-error")).to_be_visible()