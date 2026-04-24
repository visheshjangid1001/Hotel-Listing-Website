from datetime import date, datetime
from decimal import Decimal

from flask import Blueprint, flash, g, jsonify, redirect, render_template, request, url_for
from sqlalchemy import or_

from app.extensions import db
from app.models import Amenity, Booking, Hotel, Review
from app.utils import login_required


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    return redirect(url_for("main.hotel_list"))


@main_bp.route("/hotels")
def hotel_list():
    search_query = request.args.get("q", "").strip()
    city = request.args.get("city", "").strip()
    min_price = request.args.get("min_price", type=float)
    max_price = request.args.get("max_price", type=float)
    min_rating = request.args.get("rating", type=float)
    selected_amenities = request.args.getlist("amenity")

    hotels_query = Hotel.query

    if search_query:
        like_query = f"%{search_query}%"
        hotels_query = hotels_query.filter(
            or_(Hotel.name.ilike(like_query), Hotel.city.ilike(like_query))
        )

    if city:
        hotels_query = hotels_query.filter(Hotel.city.ilike(city))

    if min_price is not None:
        hotels_query = hotels_query.filter(Hotel.price_per_night >= min_price)

    if max_price is not None:
        hotels_query = hotels_query.filter(Hotel.price_per_night <= max_price)

    if selected_amenities:
        hotels_query = hotels_query.filter(
            Hotel.amenities.any(Amenity.name.in_(selected_amenities))
        )

    hotels = hotels_query.order_by(Hotel.city.asc(), Hotel.price_per_night.asc()).all()
    if min_rating is not None:
        hotels = [hotel for hotel in hotels if hotel.average_rating >= min_rating]

    cities = [row[0] for row in db.session.query(Hotel.city).distinct().order_by(Hotel.city).all()]
    amenities = Amenity.query.order_by(Amenity.name).all()

    return render_template(
        "main/hotel_list.html",
        hotels=hotels,
        cities=cities,
        amenities=amenities,
        filters={
            "q": search_query,
            "city": city,
            "min_price": request.args.get("min_price", ""),
            "max_price": request.args.get("max_price", ""),
            "rating": request.args.get("rating", ""),
            "amenity": selected_amenities,
        },
    )


@main_bp.route("/api/hotel-suggestions")
def hotel_suggestions():
    search_query = request.args.get("q", "").strip()
    if len(search_query) < 2:
        return jsonify([])

    like_query = f"%{search_query}%"
    hotels = (
        Hotel.query.filter(or_(Hotel.name.ilike(like_query), Hotel.city.ilike(like_query)))
        .order_by(Hotel.name.asc())
        .limit(6)
        .all()
    )
    suggestions = []
    for hotel in hotels:
        suggestions.append({"label": hotel.name, "type": "hotel"})
        suggestions.append({"label": hotel.city, "type": "city"})

    deduped = []
    seen = set()
    for item in suggestions:
        key = (item["label"], item["type"])
        if key not in seen:
            seen.add(key)
            deduped.append(item)
    return jsonify(deduped)


@main_bp.route("/hotels/<int:hotel_id>")
def hotel_detail(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    reviews = (
        Review.query.filter_by(hotel_id=hotel.id)
        .order_by(Review.created_at.desc())
        .all()
    )
    return render_template("main/hotel_detail.html", hotel=hotel, reviews=reviews, today=date.today())


@main_bp.route("/hotels/<int:hotel_id>/book", methods=["POST"])
@login_required
def book_hotel(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    check_in_raw = request.form.get("check_in", "")
    check_out_raw = request.form.get("check_out", "")

    try:
        check_in = datetime.strptime(check_in_raw, "%Y-%m-%d").date()
        check_out = datetime.strptime(check_out_raw, "%Y-%m-%d").date()
    except ValueError:
        flash("Please select valid booking dates.", "danger")
        return redirect(url_for("main.hotel_detail", hotel_id=hotel.id))

    nights = (check_out - check_in).days
    if check_in < date.today():
        flash("Check-in date cannot be in the past.", "danger")
    elif nights <= 0:
        flash("Check-out must be after check-in.", "danger")
    else:
        total_price = Decimal(hotel.price_per_night) * nights
        booking = Booking(
            user_id=g.user.id,
            hotel_id=hotel.id,
            check_in=check_in,
            check_out=check_out,
            total_price=total_price,
        )
        db.session.add(booking)
        db.session.commit()
        flash("Booking confirmed successfully.", "success")
        return redirect(url_for("main.my_bookings"))

    return redirect(url_for("main.hotel_detail", hotel_id=hotel.id))


@main_bp.route("/hotels/<int:hotel_id>/reviews", methods=["POST"])
@login_required
def add_review(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    rating = request.form.get("rating", type=int)
    comment = request.form.get("comment", "").strip()

    if rating is None or rating < 1 or rating > 5:
        flash("Please select a rating between 1 and 5.", "danger")
    elif not comment:
        flash("Please write a review before submitting.", "danger")
    else:
        existing_review = Review.query.filter_by(user_id=g.user.id, hotel_id=hotel.id).first()
        if existing_review:
            existing_review.rating = rating
            existing_review.comment = comment
            flash("Your review has been updated.", "success")
        else:
            review = Review(user_id=g.user.id, hotel_id=hotel.id, rating=rating, comment=comment)
            db.session.add(review)
            flash("Your review has been added.", "success")
        db.session.commit()

    return redirect(url_for("main.hotel_detail", hotel_id=hotel.id))


@main_bp.route("/bookings")
@login_required
def my_bookings():
    bookings = (
        Booking.query.filter_by(user_id=g.user.id)
        .order_by(Booking.created_at.desc())
        .all()
    )
    return render_template("main/my_bookings.html", bookings=bookings)
