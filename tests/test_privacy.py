from order_bot.privacy import mask_pii


def test_nothing_to_hide():
    assert mask_pii("order shipped today") == "order shipped today"


def test_email_is_hidden():
    assert "lina.haddad@example.com" not in mask_pii("mail lina.haddad@example.com now")
