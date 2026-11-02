from order_bot.delivery import estimate_delivery


def answer(question: str, orders: list[dict]) -> str:
    """Answer a shopper's question about one of their orders."""
    q = question.lower()
    # find the order number
    order_id = None
    for word in q.replace("?", " ").replace(",", " ").replace(".", " ").replace("!", " ").split():
        if word.startswith("sp-") and len(word) == 8 and word[3:].isdigit():
            order_id = word.upper()
            break
    # what do they want to know
    if "when" in q or "arrive" in q or "eta" in q:
        wants = "eta"
    elif "price" in q or "cost" in q or "how much" in q:
        wants = "price"
    elif "status" in q or "where" in q:
        wants = "status"
    else:
        wants = "unknown"
    if order_id is None:
        return "Please send your order number (like SP-12345)."
    order = None
    for o in orders:
        if o["order_id"] == order_id:
            order = o
    if order is None:
        return "I can't find order " + order_id + "."
    if wants == "eta":
        days = 1 if order["ship_method"] == "express" else 4
        return "Order " + order_id + " should arrive by " + estimate_delivery(order["order_date"], days) + "."
    if wants == "price":
        return "Order " + order_id + " cost " + str(order["price_cents"] / 100) + "."
    if wants == "status":
        return "Order " + order_id + " is " + order["status"] + "."
    return "What would you like to know about order " + order_id + "?"
