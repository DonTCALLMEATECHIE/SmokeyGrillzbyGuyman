from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "smokey_secret"

MENU = [
    {
        "id": 1,
        "name": "CHICKEN PLATTER",
        "desc": ["3 pcs Large Chicken Lap", "3 pcs Roast Plantain/Bole", "Coleslaw"],
        "image": "chicken_platter.jpg",
        "price": 18500,
    },
    {
        "id": 2,
        "name": "TURKEY PLATTER",
        "desc": ["4 pcs Large Turkey Lap", "Yam chips (1 side)", "Potato chips (1 side)", "Coleslaw (1 side)"],
        "image": "turkey_platter.jpg",
        "price": 18500,
    },
    {
        "id": 3,
        "name": "BOLE PLATTER",
        "desc": ["Roast Fish (Titus)", "3 pcs Roast Plantain/Bole", "3 pcs Roast Yam"],
        "image": "bole_platter.jpg",
        "price": 10000,
    },
    {
        "id": 4,
        "name": "FISH PLATTER",
        "desc": ["Fish (Large/Medium) (Croaker/Catfish)", "Potato chips (1 side)", "Coleslaw (1 side)"],
        "image": "fish_platter.jpg",
        "price": 10000,
    },
    {
        "id": 5,
        "name": "ASUN PLATTER",
        "desc": ["1 Portion of Asun", "Potato Chips (1 side)", "Coleslaw"],
        "image": "asun_platter.jpg",
        "price": 8500,
    }
]

@app.route("/")
def index():
    return render_template("index.html", menu=MENU)

@app.route("/menu")
def menu():
    return render_template("menu.html", menu=MENU)

@app.route("/add_to_cart/<int:item_id>", methods=["POST"])
def add_to_cart(item_id):
    qty = int(request.form.get("qty", 1))
    item = next((item for item in MENU if item["id"] == item_id), None)
    if not item:
        flash("Menu item not found.", "danger")
        return redirect(url_for("menu"))
    session['cart'] = {
        "item_id": item_id,
        "qty": qty
    }
    return redirect(url_for("checkout"))

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    cart = session.get('cart')
    if not cart:
        flash("Your cart is empty.", "danger")
        return redirect(url_for("menu"))
    item = next((item for item in MENU if item["id"] == cart["item_id"]), None)
    qty = cart["qty"]
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        address = request.form.get("address")
        notes = request.form.get("notes")
        session.pop('cart', None)
        return render_template(
            "confirmation.html",
            item=item,
            name=name,
            phone=phone,
            qty=qty,
            notes=notes,
            address=address
        )
    return render_template("checkout.html", item=item, qty=qty)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)