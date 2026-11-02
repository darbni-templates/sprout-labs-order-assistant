from order_bot.assistant import parse_order_question


def test_status_question():
    assert parse_order_question("What is the status of SP-10001?") == {
        "order_id": "SP-10001",
        "wants": "status",
    }
