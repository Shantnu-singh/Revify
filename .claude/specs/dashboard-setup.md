# Revify — Business Dashboard Frontend Spec
> **For agent use.** Build frontend only. All data is hardcoded. No DB, no auth logic, no API calls.

---

## Stack
- Flask + Jinja2 templates
- Vanilla CSS (no framework) — follow the design tokens below
- Vanilla JS only where needed (search filter, wizard steps, toast)
- Fonts via Google Fonts: `Instrument Serif`, `Syne`, `DM Sans`

---

## Design Tokens
```css
:root {
  --bg:        #07080a;
  --surface:   #0e1014;
  --border:    rgba(255,255,255,0.07);
  --accent:    #c8f55a;   /* lime — primary CTA */
  --accent2:   #3dffc0;   /* mint — secondary highlights */
  --text:      #e8eaed;
  --muted:     #6b7280;
  --card-bg:   rgba(255,255,255,0.03);
  --radius:    12px;
}
```
**Fonts:** Syne 700/800 for headings/labels. Instrument Serif for large display numbers/titles. DM Sans 300/400 for body.

---

## Shell Layout

Every dashboard page shares one base template: `base_dashboard.html`.

```
┌──────────────────────────────────────────────────┐
│  SIDEBAR (240px fixed)  │  MAIN CONTENT (flex-1) │
│                         │  ┌──────────────────┐  │
│  Logo                   │  │ TOPBAR           │  │
│  ──────                 │  └──────────────────┘  │
│  Nav links              │                         │
│                         │  <page content>         │
│  ──────                 │                         │
│  User info + Logout     │                         │
└──────────────────────────────────────────────────┘
```

### Sidebar
- Background: `var(--surface)`, right border: `1px solid var(--border)`
- Logo: `Revify.` — Syne 800, accent dot
- Nav links (see routes below) — DM Sans, color `var(--muted)` default
- **Active link:** lime left border `3px solid var(--accent)`, background `rgba(200,245,90,0.05)`, text `var(--text)`
- Bottom: user name (bold), plan badge pill (Free / Growth / Pro), Logout link

### Topbar
- Background: `var(--bg)`, bottom border: `1px solid var(--border)`, padding `1rem 2rem`
- Left: page title — Instrument Serif, ~1.5rem
- Right: one primary CTA button (context-dependent per page)

### Buttons
```
.btn-primary  → background: var(--accent), color: #07080a, Syne 700
.btn-ghost    → background: transparent, border: 1px solid var(--border), color: var(--muted)
.btn-danger   → background: transparent, border: 1px solid #ef4444, color: #ef4444
border-radius: 8px, padding: 0.6rem 1.4rem
```

### Inputs / Selects / Textareas
```
background: rgba(255,255,255,0.04)
border: 1px solid var(--border)
border-radius: 8px
color: var(--text)
font: DM Sans 14px
focus: border-color: rgba(200,245,90,0.5), outline: none
```

---

## Routes & Templates

| Route | Template | Topbar Title | Topbar CTA |
|-------|----------|-------------|------------|
| `/dashboard` | `dashboard/overview.html` | Overview | `+ New Campaign` |
| `/dashboard/campaigns` | `dashboard/campaigns.html` | My Campaigns | `+ New Campaign` |
| `/dashboard/campaigns/new` | `dashboard/wizard.html` | New Campaign | — |
| `/dashboard/campaigns/<id>` | `dashboard/campaign_detail.html` | Campaign Detail | `⬇ Download QR` |
| `/dashboard/qrcodes` | `dashboard/qrcodes.html` | All QR Codes | — |

All routes are GET only for now. Forms use POST but just redirect back (stub).

---

## Page 1 — Overview (`/dashboard`)

### Stat Cards Row
4 cards in a horizontal row. Each card:
- Background `var(--surface)`, border `1px solid var(--border)`, border-radius `var(--radius)`, padding `1.5rem`
- Top: icon (emoji) + label (DM Sans, `var(--muted)`, 0.75rem uppercase)
- Middle: big number — Instrument Serif, 2.5rem, `var(--text)`
- Bottom: small caption — DM Sans 300, `var(--muted)`, 0.75rem

| Icon | Label | Hardcoded value |
|------|-------|-----------------|
| 📣 | Total Campaigns | 3 |
| ⭐ | Reviews Collected | 47 |
| 📈 | Avg. Star Rating | 4.6 |
| 📲 | QR Scans | 123 |

### Recent Campaigns Strip
Heading: "Recent Campaigns" (Syne 700, 1rem). Then 3 campaign cards in a row (see Campaign Card spec below). Below the row: a "View all campaigns →" link.

### Empty State (render this if `campaigns|length == 0`)
Centred panel, large emoji `📣`, heading "No campaigns yet", subtext "Create your first campaign and get a QR code in 2 minutes.", button `+ Create Campaign`.

---

## Page 2 — Campaigns List (`/dashboard/campaigns`)

### Toolbar
Horizontal bar above cards, `display: flex, gap: 1rem, align-items: center`:
- Text input — placeholder "Search campaigns..." — JS filters cards client-side by campaign name
- Select — "All Tags" + each tag from the tag list below
- Select — "All Platforms" / "Google" / "Yelp"
- (pushed right) `+ New Campaign` button

### Campaign Card (reused on Overview too)
Full-width card, `var(--surface)` bg, `1px solid var(--border)` border, `var(--radius)` radius, padding `1.5rem`.

Layout:
```
[Avatar circle] [Campaign Name — Syne 700]  [Platform badge]  [Status badge]
                [Business name · Category · City]
                [Tag pills row]
                ─────────────────────────────────────────────────────
                Created: Jan 12 2025  ·  Scans: 38  ·  Reviews: 12    [Manage →]  [QR ↓]
```

**Avatar circle:** 44px, background `rgba(200,245,90,0.12)`, text `var(--accent)`, Syne 700, first letter of campaign name.

**Platform badge:**
- Google → `background: #dbeafe; color: #1d4ed8`
- Yelp → `background: #fee2e2; color: #b91c1c`

**Status badge:**
- Active → `background: #dcfce7; color: #15803d`
- Draft → `background: #fef9c3; color: #854d0e`
- Paused → `background: #1f2937; color: #9ca3af`

All badges: `font-size: 0.65rem`, `font-weight: 600`, `text-transform: uppercase`, `letter-spacing: 0.08em`, `padding: 0.2rem 0.6rem`, `border-radius: 100px`.

**Tag pills:** same small pill style, colours from tag table below.

### Hardcoded Campaigns (render these 3)

**Campaign 1**
- Name: `Sharma's Bakery — Main Branch`
- Platform: Google · Status: Active
- Business: Sharma's Bakery · Bakery · Lajpat Nagar, Delhi
- Tags: `food`, `bakery`, `delhi`
- Stats: Created Jan 12 2025 · Scans 38 · Reviews 12

**Campaign 2**
- Name: `Delhi Dental Clinic`
- Platform: Google · Status: Active
- Business: Delhi Dental Clinic · Dental · Karol Bagh, Delhi
- Tags: `health`, `clinic`, `delhi`
- Stats: Created Feb 3 2025 · Scans 51 · Reviews 22

**Campaign 3**
- Name: `Spice Garden Restaurant`
- Platform: Yelp · Status: Draft
- Business: Spice Garden · Restaurant · Connaught Place, Delhi
- Tags: `food`, `restaurant`
- Stats: Created Mar 1 2025 · Scans 0 · Reviews 0

### Tag Library & Colours

| Tag | Colour |
|-----|--------|
| food, bakery, restaurant, café | Green pill: `bg #dcfce7 · text #15803d` |
| health, clinic | Blue pill: `bg #dbeafe · text #1d4ed8` |
| salon, beauty | Purple pill: `bg #ede9fe · text #6d28d9` |
| retail, services | Yellow pill: `bg #fef9c3 · text #854d0e` |
| delhi, mumbai, bangalore | Gray pill: `bg #1f2937 · text #9ca3af` |

---

## Page 3 — New Campaign Wizard (`/dashboard/campaigns/new`)

One page with a **step indicator** at top and **one step visible at a time** toggled by JS (no page reload).

### Step Indicator
5 numbered circles in a row connected by a line.
- Done steps: filled `var(--accent)`, checkmark inside
- Current step: filled `var(--accent)`, step number inside, slight glow
- Future steps: `var(--border)` border, `var(--muted)` number

### Step 1 — Campaign Basics
Fields:
- **Campaign Name** — text input, placeholder `e.g. Sharma's Bakery — Main Branch`
- **Platform** — two large radio cards side by side:
  - Google card: Google logo emoji 🔵, "Google Reviews", description "Most widely used in India"
  - Yelp card: Yelp logo emoji ⭕, "Yelp Reviews", description "Popular for restaurants & services"
  - Selected card gets `border-color: var(--accent)` and subtle lime background
- **Tags** — grid of clickable pill checkboxes from the tag library. Selected pills fill with accent colour.

### Step 2 — Business Link
Fields:
- **Platform URL** — text input (full width), placeholder changes based on step 1 platform selection:
  - Google: `https://maps.google.com/...`
  - Yelp: `https://yelp.com/biz/...`
- Helper tip box (styled callout, green border): "To find your Google link, search your business on Google Maps → Share → Copy link."

### Step 3 — Business Details
Fields (all full-width, stacked):
- **Business Name** — text input
- **Category** — `<select>` with option groups:
  - Food & Beverage: Bakery, Restaurant, Café, Catering
  - Health: Dental, General Physician, Pharmacy, Gym
  - Beauty: Hair Salon, Spa, Nail Studio
  - Retail: Clothing, Electronics, Grocery
  - Services: Tailor, Photographer, Travel Agent
  - Education: Tuition Centre, Coaching Institute
  - Other
- **Description** — textarea, 4 rows, placeholder `What makes your business special? Customers will see this.`, char counter `0/400`
- **City / Locality** — text input, placeholder `e.g. Lajpat Nagar, Delhi`
- **USP** — text input (optional), placeholder `e.g. Best sourdough in South Delhi`

### Step 4 — Sample Reviews
Heading: "Here are some recent reviews from your platform" (these are hardcoded examples to show the owner context).

Show 3 review cards (read-only). Each card:
- Star row (filled ⭐ emojis)
- Review text (italic)
- Reviewer name + platform + time ago (muted)
- Background `var(--card-bg)`, border `1px solid var(--border)`, radius `var(--radius)`, padding `1rem`

**Hardcoded reviews:**
1. ⭐⭐⭐⭐⭐ — "The pastries here are exceptional — flaky, buttery, and made with care. Will definitely be back!" — Priya M. · Google · 2 weeks ago
2. ⭐⭐⭐⭐ — "Fresh bread and friendly staff. The sourdough was great. Will come back." — Rohan D. · Google · 1 month ago
3. ⭐⭐⭐⭐⭐ — "Ordered a custom cake and they nailed every detail. Great price, beautiful work." — Anjali K. · Google · 3 weeks ago

Below reviews, one optional textarea:
- **Note to AI** — placeholder `e.g. "Mention our free delivery" or "Don't mention parking"`, 2 rows, `0/200` char counter

### Step 5 — Review & Launch
Read-only summary of all entered data, displayed as label-value rows grouped in cards:
- Card 1: Campaign name, Platform, Tags
- Card 2: Business URL
- Card 3: Business name, Category, Description, City, USP
- Card 4: Note to AI (if any)

Each card has an `Edit ✏` link in the top-right that sets the active step back via JS.

Primary button: **🚀 Launch Campaign** (full-width, `.btn-primary`).

### Wizard Navigation
- Back / Next buttons at the bottom of each step
- Step 1 has no Back. Step 5 has no Next (replaced by Launch button).
- "Next →" validates required fields in the current step before advancing (JS, just check not-empty).

---

## Page 4 — Campaign Detail (`/dashboard/campaigns/<id>`)

Use Campaign 1 (Sharma's Bakery) as the hardcoded detail page.

### Hero Row
```
[Avatar 56px]  Sharma's Bakery — Main Branch         [Google badge]  [Active badge]
               Sharma's Bakery · Bakery · Lajpat Nagar, Delhi
               [food pill] [bakery pill] [delhi pill]          Created Jan 12, 2025
```

### Two-column layout below hero
**Left column (flex ~60%):** Business details + Stats + Danger Zone

**Right column (flex ~40%):** QR Code panel

### QR Code Panel (right column)
- Card, centered content
- Label: "Your QR Code" (Syne 700)
- Large QR code image placeholder — render a dummy 200×200 grey box with text "QR Code" or use a real `qrcode` generated PNG at `/dashboard/campaigns/1/qr`
- URL display box (read-only input): `revify.app/review/sharmas-bakery` with a 📋 copy button
- Button row: `⬇ Download PNG` · `🖨 Print QR`

### Business Details Panel (left column)
Label-value list:
- Business Name: Sharma's Bakery
- Category: Bakery
- Platform: Google
- Platform URL: (truncated link)
- City: Lajpat Nagar, Delhi
- USP: Best sourdough in South Delhi
- Description: (full text)
- Note to AI: Mention our free home delivery

`Edit details` button (`.btn-ghost`) at the bottom of this panel.

### Stats Row (left column)
3 small stat cards in a row: **QR Scans — 38** · **Reviews Posted — 12** · **Avg. Stars — 4.8**

### Danger Zone (left column, bottom)
Section with `border: 1px solid rgba(239,68,68,0.3)`, `border-radius: var(--radius)`, padding `1.5rem`, heading "Danger Zone" in `#ef4444`.
- `Pause Campaign` button (`.btn-ghost`)
- `Delete Campaign` button (`.btn-danger`)
- Short muted description under each button

---

## Page 5 — QR Codes (`/dashboard/qrcodes`)

Simple grid (3 columns) of QR code cards. One card per campaign.

Each card:
- Campaign name (Syne 700)
- Platform badge
- QR image placeholder (150×150)
- `⬇ Download` button (full-width, `.btn-ghost`)

Hardcoded: 3 cards (one per campaign from the list).

---

## Toast Notification
A fixed bottom-right toast component (hidden by default):
```
position: fixed; bottom: 1.5rem; right: 1.5rem;
background: var(--surface); border: 1px solid var(--border);
border-radius: var(--radius); padding: 1rem 1.5rem;
display: flex; align-items: center; gap: 0.75rem;
```
- Green left border for success, red for error
- Auto-hides after 4s via JS
- On wizard launch → show success toast "🎉 Campaign launched! Your QR code is ready."

---

## File Structure to Create
```
templates/
  base_dashboard.html        ← shell with sidebar + topbar
  dashboard/
    overview.html
    campaigns.html
    wizard.html
    campaign_detail.html
    qrcodes.html
static/
  css/
    dashboard.css            ← all dashboard styles
  js/
    dashboard.js             ← search filter + wizard steps + toast + copy button
```

---

## Notes for Agent
- `base_dashboard.html` uses `{% block title %}`, `{% block topbar_title %}`, `{% block topbar_cta %}`, `{% block content %}`.
- All pages `{% extends "base_dashboard.html" %}`.
- No real form submission needed — wizard "Next" and "Launch" can be JS-only for now.
- Client-side campaign search on campaigns page: filter `.campaign-card` elements by `data-name` attribute on keyup.
- Wizard steps: hide all `.wizard-step` divs, show only the one matching `currentStep` variable in JS.
- The QR code on the detail page can be a placeholder grey box — no actual QR generation needed for frontend spec.