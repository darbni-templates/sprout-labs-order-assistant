from order_bot.api import handle_lookup


def test_missing_order_id_is_400():
    assert handle_lookup({}, [])["status"] == 400


def test_unknown_order_is_404():
    assert handle_lookup({"order_id": "SP-00000", "email": "a@b.co"}, [])["status"] == 404
