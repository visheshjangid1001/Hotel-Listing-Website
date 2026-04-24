from app.extensions import db


hotel_amenities = db.Table(
    "hotel_amenities",
    db.Column("hotel_id", db.Integer, db.ForeignKey("hotel.id"), primary_key=True),
    db.Column("amenity_id", db.Integer, db.ForeignKey("amenity.id"), primary_key=True),
)


class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), nullable=False, index=True)
    city = db.Column(db.String(80), nullable=False, index=True)
    location = db.Column(db.String(180), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price_per_night = db.Column(db.Numeric(10, 2), nullable=False)
    main_image_url = db.Column(db.String(500), nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)

    images = db.relationship("HotelImage", back_populates="hotel", cascade="all, delete-orphan")
    amenities = db.relationship("Amenity", secondary=hotel_amenities, back_populates="hotels")
    bookings = db.relationship("Booking", back_populates="hotel", cascade="all, delete-orphan")
    reviews = db.relationship("Review", back_populates="hotel", cascade="all, delete-orphan")

    @property
    def average_rating(self):
        if not self.reviews:
            return 0
        return round(sum(review.rating for review in self.reviews) / len(self.reviews), 1)

    @property
    def review_count(self):
        return len(self.reviews)


class HotelImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey("hotel.id"), nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    caption = db.Column(db.String(150), nullable=True)

    hotel = db.relationship("Hotel", back_populates="images")


class Amenity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False, index=True)

    hotels = db.relationship("Hotel", secondary=hotel_amenities, back_populates="amenities")
