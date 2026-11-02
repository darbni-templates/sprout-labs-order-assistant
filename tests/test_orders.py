from order_bot.orders import load_orders

CSV = """order_id,customer,email,item,category,price_cents,status,order_date,delivered_date,ship_method
SP-10001,Lina Haddad,lina@example.com,Blue mug,kitchen,1250,shipped,2024-05-02,,standard"""


def test_one_order():
    [order] = load_orders(CSV)
    assert order["order_id"] == "SP-10001"
    assert order["price_cents"] == 1250
