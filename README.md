# Silog & Sips Express

Affordable Filipino silog meals and refreshing drinks for students, packaged for quick pick-up. This is an interactive business website built with **PyScript** for our Event-Driven Programming final project at Cebu Eastern College.

**Live site:** (paste the GitHub Pages link here)
**Video presentation:** (paste the link here)

## Business Concept

Silog & Sips Express sells budget-friendly, ready-to-eat silog rice bowls (Tocilog, Tapsilog, Hamsilog/Chicksilog, Bangsilog) with local drinks like Sago't Gulaman and Samalamig. Students pre-order on the website, pay first through GCash, and pick up their meals at a campus booth without waiting in long queues. See [docs/business-process.md](docs/business-process.md) for the full process.

## Features

- **Pre-order form** (`order.py`): choose meal, drink, quantity, pick-up time, and payment method; live price hint, tray with remove and clear buttons, and a P5-per-combo discount for 5 or more combos.
- **GCash payment step** (`order.py`): reference number check and a "Pending payment confirmation" status.
- **Budget checker** (`budget.py`): type your allowance and instantly see how many combos you can afford.
- **Customer feedback** (`feedback.py`): submit a rating and comment, saved in the browser, with an average rating.

## Event-Driven Programming

| Event | Where | Python function | File |
|---|---|---|---|
| `input` | Meal and quantity fields | `update_hint` | order.py |
| `click` | Add to tray button | `add_item` | order.py |
| `click` | Remove buttons in the tray | `remove_item` | order.py |
| `click` | Clear tray button | `clear_tray` | order.py |
| `change` | Payment dropdown | `toggle_payment` | order.py |
| `click` | Place order button | `place_order` | order.py |
| `input` | Allowance field | `check_budget` | budget.py |
| `click` | Send feedback button | `submit_feedback` | feedback.py |

The page updates dynamically: the tray, totals, status, budget results, and feedback list change without reloading.

## Project Structure

| File | Purpose |
|------|---------|
| `index.html` | Page structure and content |
| `style.css` | Design and layout |
| `order.py` | Pre-order and payment logic |
| `budget.py` | Budget checker |
| `feedback.py` | Feedback form |
| `docs/` | Business process notes and video script |

## How to Run

Open the project folder in VS Code and run it with the **Live Server** extension, or visit the GitHub Pages link above. Opening `index.html` directly from your files will not load the Python files.

## Group Members and Contributions

| Member | GitHub Username | Contribution |
|--------|-----------------|--------------|
| Jerriel Delos Reyes | | |
| Jomari Labay | | |
| Louise Chermaine Marañon | | |
| Roland Segunla Jr | | |
| Ramjun Torremocha | | |
