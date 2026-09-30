import pytest


def test_duplicate_users(reset_db, base_url, api):
    payload = {
        "name": "Agata",
        "email": "agata@test.pl",
        "password": "electronics"
    }

    # pierwszy user - przygotowujemy dane
    api.post(
        f"{base_url}/api/auth/register",
        json=payload
    )

    # drugi raz ten sam produktuser
    duplicate = api.post(
        f"{base_url}/api/auth/register",
        json=payload
    )

    # oczekujemy, że API poprawnie zgłosi konflikt (409)
    assert duplicate.status_code == 409