from order_bot.returns import can_return


def test_not_delivered_yet():
    order = {"status": "shipped", "category": "kitchen", "order_date": "2024-05-01", "delivered_date": ""}
    assert can_return(order, "2024-05-03") == {"eligible": False, "reason": "not_delivered"}
