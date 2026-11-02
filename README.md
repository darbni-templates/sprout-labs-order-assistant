# Sprout Labs order assistant

The order assistant answers shoppers' questions about their orders ("where is SP-10234?",
"can I still return it?"). It is already live for a few shops: the code in this repo runs in
production today. Your job is to improve it without breaking what works.

## Your tasks
**Your exact task is in Darbni.** Open the task there and read its description: it has the
rules for YOUR version. Every intern gets their own version of each task, so a solution
copied from someone else will fail the tests.

Read the existing code before you change it. Some of it has bugs, some of it is messy, and
all of it is used by real shops.

## Where things are
| File | What it does |
|---|---|
| `order_bot/orders.py` | reads the shop platform's CSV export |
| `order_bot/delivery.py` | estimates when an order arrives |
| `order_bot/status.py` | what the bot says about an order's status |
| `order_bot/assistant.py` | answers a shopper's question about an order |
| `order_bot/contacts.py` | cleans customer names, emails and phone numbers |
| `order_bot/search.py` | finds orders for the support team |
| `order_bot/privacy.py` | hides personal data in logs |
| `order_bot/reports.py` | the late-orders report |
| `order_bot/returns.py` | the return rules |
| `order_bot/api.py` | the order-lookup endpoint for shop websites |

## Run the tests
Only the Python standard library is used. You need pytest:
```
pip install pytest
pytest tests/test_orders.py      # the tests of the file your task is about
pytest                           # everything (tests for tasks you haven't done yet fail)
```
The tests in `tests/` are only a few examples that work for every version. Darbni runs
more tests, made for your version, when you submit.

## Submitting
Commit and push your work, then submit your repo URL and the full commit SHA in Darbni.
