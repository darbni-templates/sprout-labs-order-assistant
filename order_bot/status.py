def status_message(status: str, eta: str | None) -> str:
    """What the bot says about an order's status. eta: expected arrival date or None."""
    if status == "pending":
        return "Order pending."
    if status == "shipped":
        return "Order shipped."
    if status == "delivered":
        return "Order delivered."
    if status == "cancelled":
        return "Order cancelled."
    return "Unknown status."
