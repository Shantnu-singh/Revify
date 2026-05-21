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
#  Hardcoded campaign data (frontend stub)
# ─────────────────────────────────────────
CAMPAIGNS = [
    {
        "id": 1,
        "name": "Sharma's Bakery — Main Branch",
        "platform": "Google",
        "status": "Active",
        "business_name": "Sharma's Bakery",
        "category": "Bakery",
        "city": "Lajpat Nagar, Delhi",
        "tags": ["food", "bakery", "delhi"],
        "created": "Jan 12, 2025",
        "scans": 38,
        "reviews": 12,
        "avg_stars": 4.8,
        "url": "https://maps.google.com/sharmas-bakery",
        "usp": "Best sourdough in South Delhi",
        "description": "A family-run bakery known for fresh breads, custom cakes, and warm service.",
        "note_to_ai": "Mention our free home delivery",
    },
    {
        "id": 2,
        "name": "Delhi Dental Clinic",
        "platform": "Google",
        "status": "Active",
        "business_name": "Delhi Dental Clinic",
        "category": "Dental",
        "city": "Karol Bagh, Delhi",
        "tags": ["health", "clinic", "delhi"],
        "created": "Feb 3, 2025",
        "scans": 51,
        "reviews": 22,
        "avg_stars": 4.7,
        "url": "https://maps.google.com/delhi-dental-clinic",
        "usp": "Painless dental care",
        "description": "Modern dental clinic offering general and cosmetic dentistry with gentle care.",
        "note_to_ai": "",
    },
    {
        "id": 3,
        "name": "Spice Garden Restaurant",
        "platform": "Yelp",
        "status": "Draft",
        "business_name": "Spice Garden",
        "category": "Restaurant",
        "city": "Connaught Place, Delhi",
        "tags": ["food", "restaurant"],
        "created": "Mar 1, 2025",
        "scans": 0,
        "reviews": 0,
        "avg_stars": 0,
        "url": "https://yelp.com/biz/spice-garden",
        "usp": "Authentic North Indian cuisine",
        "description": "Fine dining restaurant serving authentic North Indian and Mughlai dishes.",
        "note_to_ai": "",
    },
]


# ─────────────────────────────────────────
#  Dashboard routes (all GET, frontend stub)
# ─────────────────────────────────────────
@app.route("/dashboard")
def dashboard_overview():
    return render_template("dashboard/overview.html", campaigns=CAMPAIGNS, active_page="overview")


@app.route("/dashboard/campaigns")
def dashboard_campaigns():
    return render_template("dashboard/campaigns.html", campaigns=CAMPAIGNS, active_page="campaigns")


@app.route("/dashboard/campaigns/new")
def dashboard_campaign_new():
    return render_template("dashboard/wizard.html", active_page="campaigns")


@app.route("/dashboard/campaigns/<int:campaign_id>")
def dashboard_campaign_detail(campaign_id):
    campaign = next((c for c in CAMPAIGNS if c["id"] == campaign_id), CAMPAIGNS[0])
    return render_template("dashboard/campaign_detail.html", campaign=campaign, active_page="campaigns")


@app.route("/dashboard/qrcodes")
def dashboard_qrcodes():
    return render_template("dashboard/qrcodes.html", campaigns=CAMPAIGNS, active_page="qrcodes")


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