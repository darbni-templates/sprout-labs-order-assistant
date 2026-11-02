from order_bot.delivery import estimate_delivery


def test_within_the_week():
    assert estimate_delivery("2024-05-06", 1) == "2024-05-07"  # Monday -> Tuesday


def test_three_days_from_monday():
    assert estimate_delivery("2024-05-06", 3) == "2024-05-09"  # Monday -> Thursday
