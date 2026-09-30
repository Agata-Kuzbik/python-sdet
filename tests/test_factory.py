
def test_factory_makes_distinct_product(make_product):

    first = make_product()
    second = make_product(price=2.99)
    third = make_product(category="testowy")

    assert len({first["id"], second["id"], third["id"]}) == 3
    assert second["price"] == 2.99
    assert third["category"] == "testowy"