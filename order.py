
from pyscript import document, when

PRICES = {"Tocilog": 65, "Tapsilog": 70, "Hamsilog/Chicksilog": 65, "Bangsilog": 75}
order = []


def refresh():
    order_list = document.querySelector("#order-list")
    order_list.innerHTML = ""
    total = 0
    for item in order:
        li = document.createElement("li")
        li.textContent = f"{item['qty']} x {item['meal']} + {item['drink']} = ₱{item['subtotal']}"
        order_list.appendChild(li)
        total += item["subtotal"]
    document.querySelector("#total").textContent = f"Total: ₱{total}"


@when("click", "#add-btn")
def add_item(event):
    message = document.querySelector("#order-message")
    meal = document.querySelector("#meal").value
    drink = document.querySelector("#drink").value
    try:
        qty = int(document.querySelector("#qty").value)
    except ValueError:
        qty = 0
    if qty < 1:
        message.textContent = "Quantity must be at least 1."
        return
    order.append({"meal": meal, "drink": drink, "qty": qty, "subtotal": PRICES[meal] * qty})
    message.textContent = ""
    refresh()


@when("click", "#submit-btn")
def place_order(event):
    message = document.querySelector("#order-message")
    name = document.querySelector("#customer").value.strip()
    if not name or not order:
        message.textContent = "Please enter your name and add at least one item."
        return
    message.textContent = f"Thanks, {name}! Your order is reserved for pick-up."
    order.clear()
    refresh()
