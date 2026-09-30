import json
from pathlib import Path

import pytest
#import requests

#BASE_URL = "http://localhost:3000"
CASES = json.loads((Path(__file__).parent /"data"/"login_cases.json").read_text())

@pytest.mark.parametrize("case", 
                         CASES,
                         ids=[f"{c['email'].strip() or 'empty'}->{c['expected']}" for c in CASES]
                         )
def test_login_from_json(case, base_url, api):
    response = api.post(
        f"{base_url}/api/auth/login",
        json = {"email" : case["email"], "password" : case["password"]}
    )

    assert response.status_code == case["expected"]