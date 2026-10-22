# Business Process: Silog & Sips Express

## The business
Silog & Sips Express sells budget-friendly silog bowls (Tocilog, Tapsilog, Hamsilog/Chicksilog, Bangsilog) with a drink, priced from P65 to P75. Our customers are students who have short breaks and do not want to queue. The website lets them order ahead and pick up at the campus booth.

## How the business operates

| Step | What happens | What the website does |
|---|---|---|
| 1. Order ahead | The customer picks a meal, drink, quantity, and pick-up time (morning, lunch, or afternoon break). | The pre-order form shows a live price hint, builds a tray, and calculates the subtotal, discount, and total (`order.py`). |
| 2. Pay first | The customer sends the total through GCash and enters the reference number. | The form only appears for GCash, checks that the reference is 10 to 13 digits, and sets the status to "Pending payment confirmation". |
| 3. Verify payment | A group member checks the transaction in the GCash app (reference number, amount, sender) and marks the order confirmed in our order log. | The website cannot verify payments by itself; this step is manual. |
| 4. Prepare | We cook and pack the order only after payment is confirmed, in time for the chosen break. | The status line and policy text tell the customer when preparation starts. |
| 5. Pick up | The customer shows their name at the booth and receives the meal. | Pay-at-booth orders are reserved and cancelled if not picked up within 15 minutes of the pick-up time. |
| 6. Feedback | The customer rates the meal and leaves a comment. | The feedback form shows the average rating and the list of reviews (`feedback.py`). |

## Policies
- **Bulk discount:** 5 or more combos in one order save P5 on each combo.
- **Pay first:** GCash orders are prepared only after payment is confirmed. This limits losses from no-shows.
- **Late pay-at-booth orders:** cancelled 15 minutes after the pick-up time.
- **Out of stock:** we offer a substitute at the same price or cheaper, or a different pick-up time. If the customer declines, we refund in full after checking the payment in the app.
- **Payment safety:** we never ask for an MPIN or OTP. Payments go only to the official GCash number shown on the site and at the booth.

## Budget checker
Students can type their allowance and instantly see how many combos they can buy and which meals they can afford (`budget.py`). This helps them decide before ordering.

## Limitations of the website
The site runs only in the browser (PyScript on GitHub Pages) and has no server or database. Orders are not saved, stock is not shared between visitors, and payments cannot be verified automatically. A real launch would add a backend, such as a database, to store orders, track stock, and record confirmed payments.
