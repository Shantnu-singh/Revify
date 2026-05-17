from flask import Flask, render_template, redirect, url_for, flash, request, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "change-this-in-production"  # TODO: use env variable


# ─────────────────────────────────────────
#  Context processors (available in all templates)
# ─────────────────────────────────────────
@app.context_processor
def inject_globals():
    return {
        "app_name": "Revify",
        "year": datetime.now().year,
    }


# ─────────────────────────────────────────
#  Public routes
# ─────────────────────────────────────────
@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        # TODO: real auth against DB
        flash("Login coming soon — backend not wired yet.", "info")
        return redirect(url_for("landing"))
    return render_template("auth/login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # TODO: create user in DB
        flash("Registration coming soon!", "info")
        return redirect(url_for("landing"))
    return render_template("auth/register.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("landing"))


# ─────────────────────────────────────────
#  Protected dashboard (placeholder)
# ─────────────────────────────────────────
@app.route("/dashboard")
def dashboard():
    # TODO: add login_required decorator
    return render_template("dashboard.html")


# ─────────────────────────────────────────
#  Customer review page (scanned from QR)
# ─────────────────────────────────────────
@app.route("/review/<business_slug>")
def review_page(business_slug):
    # TODO: look up business by slug in DB
    business = {"name": business_slug.replace("-", " ").title(), "slug": business_slug}
    return render_template("review.html", business=business)


# ─────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)