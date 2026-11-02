from order_bot.search import find_orders

ORDER = {
    "order_id": "SP-10001",
    "customer": "Lina Haddad",
    "status": "shipped",
    "price_cents": 1250,
    "order_date": "2024-05-02",
}


def test_no_orders():
    assert find_orders([], {}) == []


def test_empty_query_finds_everything():
    assert find_orders([ORDER], {}) == ["SP-10001"]
