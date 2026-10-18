from pyscript import document, when

feedbacks = []


def render():
    fb_list = document.querySelector("#fb-list")
    fb_list.innerHTML = ""
    for fb in feedbacks:
        li = document.createElement("li")
        li.textContent = f"{fb['name']} ({fb['rating']}/5): {fb['comment']}"
        fb_list.appendChild(li)

    average = sum(fb["rating"] for fb in feedbacks) / len(feedbacks)
    document.querySelector("#fb-average").textContent = (
        f"Average rating: {average:.1f}/5 from {len(feedbacks)} review(s)"
    )


@when("click", "#fb-submit")
def submit_feedback(event):
    message = document.querySelector("#fb-message")
    name = document.querySelector("#fb-name").value.strip() or "Anonymous"
    comment = document.querySelector("#fb-comment").value.strip()
    rating = int(document.querySelector("#fb-rating").value)

    if not comment:
        message.textContent = "Please write a comment first."
        return

    feedbacks.append({"name": name, "rating": rating, "comment": comment})
    message.textContent = "Thank you for your feedback!"
    document.querySelector("#fb-comment").value = ""
    document.querySelector("#fb-name").value = ""
    render()
