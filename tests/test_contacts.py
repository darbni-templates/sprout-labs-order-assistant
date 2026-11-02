from order_bot.contacts import clean_contact


def test_email_is_lowercased():
    assert clean_contact({"name": "x", "email": " Lina@Example.COM ", "phone": ""})["email"] == (
        "lina@example.com"
    )


def test_missing_phone_is_none():
    assert clean_contact({"name": "x", "email": "", "phone": ""})["phone"] is None
