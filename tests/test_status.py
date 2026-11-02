from order_bot.status import status_message


def test_shipped_mentions_the_date():
    assert "2024-06-01" in status_message("shipped", "2024-06-01")


def test_unknown_statuses_get_the_same_text():
    assert status_message("bogus", None) == status_message("weird", None)
