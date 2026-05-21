# Spec: Registration

## Overview
Wire up the existing registration form to create real user accounts in SQLite. This is the first backend step — it establishes the database, the users table, password hashing, and session-based auth. After this step, a visitor can sign up, get auto-logged-in, and land on the dashboard.

## Depends on
- Step 01 (Dashboard Setup) — dashboard routes and templates must exist so we can redirect new users there.

## Routes
- `POST /register` — create a new user account — public

(The `GET /register` route and template already exist. No new routes needed.)

## Database changes
New table: `users`

| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| first_name | TEXT | NOT NULL |
| last_name | TEXT | NOT NULL |
| email | TEXT | NOT NULL UNIQUE |
| business_name | TEXT | NOT NULL |
| password_hash | TEXT | NOT NULL |
| created_at | TEXT | NOT NULL DEFAULT CURRENT_TIMESTAMP |

## Templates
- **Modify:** `templates/auth/register.html` — add flash message display block for validation errors (email already taken, password too short, etc.)

## Files to change
- `app.py` — wire up `POST /register` logic (validate, hash password, insert user, set session, redirect)
- `database/db.py` — add `init_db()` function to create tables, add `create_user()` and `get_user_by_email()` helper functions
- `templates/auth/register.html` — add flash message rendering

## Files to create
- None

## New dependencies
No new dependencies (werkzeug is already bundled with Flask).

## Rules for implementation
- No SQLAlchemy or ORMs — use `sqlite3` directly
- Parameterised queries only — never f-string or format strings in SQL
- Passwords hashed with `werkzeug.security.generate_password_hash` and checked with `check_password_hash`
- Use CSS variables — never hardcode hex values
- All templates extend `landing.html` (the register template is standalone with inline styles — keep it that way for now; full base template migration is a later step)
- On successful registration: set `session["user_id"]` and `session["user_name"]`, then redirect to `/dashboard`
- On duplicate email: flash an error and re-render the register page (do not redirect)
- Password minimum length: 8 characters — validate server-side
- `init_db()` must be called on app startup (in `app.py` at module level or in `__main__`) and must use `CREATE TABLE IF NOT EXISTS` so it's safe to run repeatedly
- Keep `database/db.py` as the single source for all DB functions — `app.py` imports from it, never writes raw SQL

## Definition of done
- [ ] Running `python app.py` creates `database/revify.db` with the `users` table
- [ ] Submitting the registration form with valid data creates a row in `users` and redirects to `/dashboard`
- [ ] Submitting with an email that already exists shows "Email already registered" flash message
- [ ] Submitting with a password shorter than 8 characters shows a validation error
- [ ] After registration, `session["user_id"]` is set and the user can access `/dashboard`
- [ ] Password is stored as a hash, not plaintext
