from pyscript import document, when

# Keep these prices in sync with order.py and the menu in index.html
MENU = {"Tocilog": 65, "Hamsilog/Chicksilog": 65, "Tapsilog": 70, "Bangsilog": 75}
CHEAPEST = min(MENU.values())


@when("input", "#allowance")
def check_budget(event):
    """Runs on every keystroke in the allowance box."""
    result = document.querySelector("#budget-result")
    chips = document.querySelector("#budget-list")
    chips.innerHTML = ""
    result.className = "msg"

    try:
        allowance = float(document.querySelector("#allowance").value)
    except ValueError:
        result.textContent = ""
        return

    if allowance < CHEAPEST:
        short = CHEAPEST - allowance
        result.textContent = f"You need ₱{short:.0f} more for our cheapest combo (₱{CHEAPEST})."
        result.className = "msg error"
        return

    combos = int(allowance // CHEAPEST)
    change = allowance - combos * CHEAPEST
    result.textContent = (
        f"With ₱{allowance:.0f} you can buy {combos} combo(s) at ₱{CHEAPEST} and keep ₱{change:.0f}."
    )

    # Show every meal this allowance can cover, with the leftover for each
    for meal, price in MENU.items():
        if price <= allowance:
            item = document.createElement("li")
            item.textContent = f"{meal}: ₱{price} (left ₱{allowance - price:.0f})"
            chips.appendChild(item)
