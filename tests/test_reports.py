from order_bot.reports import late_orders


def test_no_orders():
    assert late_orders([], "2024-05-20") == []


def test_delivered_orders_are_never_late():
    order = {"order_id": "SP-1", "status": "delivered", "order_date": "2024-01-01", "ship_method": "standard"}
    assert late_orders([order], "2024-05-20") == []
