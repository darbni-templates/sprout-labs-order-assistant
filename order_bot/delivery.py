from datetime import date, timedelta


def estimate_delivery(order_date: str, business_days: int) -> str:
    """The date an order should arrive: business_days working days (Mon-Fri) after
    order_date. Dates are "YYYY-MM-DD" strings."""
    start = date.fromisoformat(order_date)
    return (start + timedelta(days=business_days)).isoformat()
