import pytest
import requests


@pytest.mark.parametrize(
    "email, password, expected_status",
    [
        ("customer@test.io", "customer123", 200),
        ("customer@test.io", "wrongpass", 401),
        ("", "", 400),
        ("unknown@test.io", "customer123", 401),
    ])


def test_login_states(api, base_url, email, password, expected_status):
    response = api.post(
    f"{base_url}/api/auth/login",
    json={"email": email, "password": password}
    )

    assert response.status_code == expected_status
