# StayAtlas Hotel Listing Website

Modular hotel listing website built with Python, Flask, MySQL, HTML, CSS, and JavaScript.

## Features

- Hotel listing page with search and filters for city, price, rating, and amenities
- Hotel detail page with gallery, amenities, reviews, average rating, and embedded Google Maps view
- Session-based user authentication with signup, login, and logout
- Booking system with check-in, check-out, total price calculation, and booking dashboard
- Reviews and ratings with update support for the same user
- Modular Flask structure using blueprints and SQLAlchemy models

## Project Structure

```text
app/
  auth/
  main/
  models/
  static/
  templates/
run.py
seed.py
requirements.txt
```

## Setup and Run

1. Create a MySQL database:

```sql
CREATE DATABASE hotel_listing;
```

2. Open PowerShell in the project folder and create a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

This project uses `PyMySQL` against MySQL 8 style authentication, so `cryptography` must be installed too. It is already included in `requirements.txt`.

4. Copy the environment template:

```powershell
Copy-Item .env.example .env
```

5. Open `.env` and update the MySQL credentials:

```env
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=hotel_listing
```

If your password contains special characters such as `#`, `@`, `:`, or `/`, keep using `DB_PASSWORD`. The app will encode it safely for the MySQL connection string.

6. Seed the database:

```powershell
py seed.py
```

7. Run the Flask app:

```powershell
py run.py
```

8. Open the website in your browser:

```text
http://127.0.0.1:5000
```

If `py` does not work on your machine, use:

```powershell
python seed.py
python run.py
```

## Demo Login

- Email: `demo@stayatlas.com`
- Password: `demo123`
