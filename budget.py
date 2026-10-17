
CHEAPEST_COMBO = 65


def check_budget(allowance):
    try:
        allowance = float(allowance)
    except ValueError:
        return "Please enter a valid amount."

    if allowance < CHEAPEST_COMBO:
        return (
            f"₱{allowance:.0f} isn't enough for a combo yet. "
            f"Our cheapest starts at ₱{CHEAPEST_COMBO}."
        )

    combos = int(allowance // CHEAPEST_COMBO)
    change = allowance - combos * CHEAPEST_COMBO

    return (
        f"With ₱{allowance:.0f}, you can buy {combos} "
        f"combo(s) at ₱{CHEAPEST_COMBO} each, "
        f"with ₱{change:.0f} left over."
    )
