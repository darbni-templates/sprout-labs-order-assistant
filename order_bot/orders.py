"""Orders come from the shop platform as a CSV export (one row per order)."""


def load_orders(csv_text: str) -> list[dict]:
    """Read the CSV export. The first line is the header.

    Columns: order_id, customer, email, item, category, price_cents, status,
    order_date, delivered_date, ship_method. price_cents becomes an int.
    """
    lines = csv_text.strip().split("\n")
    header = lines[0].split(",")
    orders = []
    for line in lines[1:]:
        values = line.split(",")
        order = dict(zip(header, values))
        order["price_cents"] = int(order["price_cents"])
        orders.append(order)
    return orders
