from pyscript import document, when

# Keep these prices in sync with budget.py and the menu in index.html
PRICES = {"Tocilog": 65, "Tapsilog": 70, "Hamsilog/Chicksilog": 65, "Bangsilog": 75}
BULK_MIN = 5      # combos needed for the discount
BULK_OFF = 5      # pesos off per combo

order = []


def q(selector):
    return document.querySelector(selector)


def show(message, error=False):
    box = q("#order-message")
    box.textContent = message
    box.className = "msg error" if error else "msg"


def calculate():
    count = sum(item["qty"] for item in order)
    subtotal = sum(PRICES[item["meal"]] * item["qty"] for item in order)
    discount = count * BULK_OFF if count >= BULK_MIN else 0
    return subtotal, discount, subtotal - discount


def refresh():
    rows = ""
    for index, item in enumerate(order):
        cost = PRICES[item["meal"]] * item["qty"]
        rows += (
            f"<li><span>{item['qty']} x {item['meal']}<br><small>{item['drink']}</small></span>"
            f"<span>₱{cost} <button class='remove' data-index='{index}'>Remove</button></span></li>"
        )
    if not rows:
        rows = "<li class='empty'>Your tray is empty. Pick a meal to start.</li>"
    q("#order-list").innerHTML = rows

    subtotal, discount, total = calculate()
    q("#subtotal").textContent = f"₱{subtotal}"
    q("#discount").textContent = f"-₱{discount}"
    q("#total").textContent = f"₱{total}"


@when("input", ".live")
def update_hint(event):
    """Runs every time the meal or quantity changes."""
    meal = q("#meal").value
    try:
        qty = int(q("#qty").value)
    except ValueError:
        q("#price-hint").textContent = ""
        return
    q("#price-hint").textContent = f"₱{PRICES[meal]} x {qty} = ₱{PRICES[meal] * qty}"


@when("click", "#add-btn")
def add_item(event):
    try:
        qty = int(q("#qty").value)
    except ValueError:
        qty = 0
    if qty < 1 or qty > 20:
        show("Enter a quantity from 1 to 20.", error=True)
        return

    meal, drink = q("#meal").value, q("#drink").value
    for item in order:                      # same meal + drink: add to the existing row
        if item["meal"] == meal and item["drink"] == drink:
            item["qty"] += qty
            break
    else:
        order.append({"meal": meal, "drink": drink, "qty": qty})

    show(f"Added {qty} x {meal} to your tray.")
    refresh()


@when("click", "#order-list")
def remove_item(event):
    """One listener for the whole list; works for buttons added later."""
    button = event.target.closest("button")
    if button is None:
        return
    order.pop(int(button.dataset.index))
    show("Item removed.")
    refresh()


@when("click", "#clear-btn")
def clear_tray(event):
    order.clear()
    show("Tray cleared.")
    refresh()


@when("click", "#submit-btn")
def place_order(event):
    name = q("#customer").value.strip()
    if not name:
        show("Please enter your name first.", error=True)
        return
    if not order:
        show("Add at least one meal to your tray.", error=True)
        return

    _, _, total = calculate()
    pickup = q("#pickup").value
    ref = q("#gcash-ref").value.strip()

    if q("#payment").value == "gcash":
        if not (ref.isdigit() and 10 <= len(ref) <= 13):
            show("Enter the GCash reference number (10 to 13 digits) after you send the payment.", error=True)
            return
        status = "Pending payment confirmation"
        note = f"We start preparing once we confirm your ₱{total} GCash payment (ref {ref})."
    else:
        status = "Reserved: pay at pick-up"
        note = f"Pay ₱{total} at the booth. Orders not picked up within 15 minutes of {pickup} are cancelled."

    show(f"Order received, {name}! Pick-up: {pickup}. {note}")
    q("#order-status").textContent = f"Status: {status}"
    q("#order-status").className = "status pending"
    q("#gcash-ref").value = ""
    order.clear()
    refresh()


@when("change", "#payment")
def toggle_payment(event):
    """Show the GCash fields only when GCash is selected."""
    q("#gcash-box").hidden = q("#payment").value != "gcash"


refresh()
