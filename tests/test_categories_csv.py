import csv
from pathlib import Path

import pytest

def load_rows(name):
    with open(Path(__file__).parent /"data"/name, newline="") as f:
        return list(csv.DictReader(f))

ROWS = load_rows("categories.csv")

@pytest.mark.parametrize("row", ROWS, ids = [r["category"] for r in ROWS])
def test_category_presence(row,base_url, api):
    products = api.get(f"{base_url}/api/products", params= {"category": row["category"]}).json()
    present = row["present"] == "true"

    assert (len(products) > 0) is present