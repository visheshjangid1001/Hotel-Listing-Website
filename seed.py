from app import create_app
from app.extensions import db
from app.models import Amenity, Hotel, HotelImage, Review, User


app = create_app()


IMAGE_POOL = [
    "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1496417263034-38ec4f0b665a?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1444201983204-c43cbd584d93?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1566665797739-1674de7a421a?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1445019980597-93fa8acb246c?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1455587734955-081b22074882?auto=format&fit=crop&w=1200&q=80",
]


def build_hotel(
    name,
    city,
    location,
    price_per_night,
    description,
    latitude,
    longitude,
    amenities,
    reviews,
    image_indexes,
):
    main_image = IMAGE_POOL[image_indexes[0]]
    gallery = [IMAGE_POOL[index] for index in image_indexes[1:5]]
    if len(gallery) < 4:
        gallery.extend(IMAGE_POOL[: 4 - len(gallery)])

    return {
        "name": name,
        "city": city,
        "location": location,
        "price_per_night": price_per_night,
        "description": description,
        "main_image_url": main_image,
        "latitude": latitude,
        "longitude": longitude,
        "images": gallery,
        "amenities": amenities,
        "reviews": [{"rating": rating, "comment": comment} for rating, comment in reviews],
    }


HOTEL_DATA = [
    build_hotel(
        "The Imperial Horizon",
        "Delhi",
        "Connaught Place",
        9500,
        "Luxury business hotel close to central Delhi landmarks with rooftop dining, concierge support, and elegant rooms for city travellers.",
        28.6315,
        77.2167,
        ["WiFi", "Pool", "AC", "Breakfast", "Parking", "Gym"],
        [
            (5, "Very polished service and excellent central location."),
            (4, "Comfortable rooms and easy check-in for a short business stay."),
        ],
        [0, 3, 4, 5, 6],
    ),
    build_hotel(
        "Pink City Palace Stay",
        "Jaipur",
        "Bani Park",
        6200,
        "Boutique heritage hotel blending Rajasthani interiors, courtyard dining, and fast access to Jaipur attractions.",
        26.9278,
        75.7997,
        ["WiFi", "AC", "Breakfast", "Spa", "Restaurant"],
        [
            (5, "Beautiful decor and the staff were warm throughout the trip."),
            (4, "Good value, calm area, and clean rooms."),
        ],
        [2, 10, 11, 4, 8],
    ),
    build_hotel(
        "Lakeview Retreat",
        "Udaipur",
        "Fateh Sagar Road",
        7800,
        "Scenic hotel overlooking the lake with spacious balconies, family-friendly facilities, and curated local dining recommendations.",
        24.6005,
        73.6957,
        ["WiFi", "Pool", "AC", "Parking", "Restaurant", "Breakfast"],
        [
            (5, "Excellent lake view and a strong breakfast spread."),
            (5, "Relaxed ambience with a polished booking experience."),
        ],
        [1, 7, 4, 8, 9],
    ),
    build_hotel(
        "Marine Drive Atelier",
        "Mumbai",
        "Nariman Point",
        11200,
        "High-rise stay with Arabian Sea views, modern business facilities, and a lounge suited for short premium city breaks.",
        18.9257,
        72.8234,
        ["WiFi", "Breakfast", "Gym", "Airport Shuttle", "Work Lounge"],
        [
            (5, "The sea-facing rooms and lobby design feel premium."),
            (4, "Great for a work trip with strong service standards."),
        ],
        [6, 0, 3, 5, 4],
    ),
    build_hotel(
        "Bandra Bloom Suites",
        "Mumbai",
        "Bandra West",
        8600,
        "Design-forward boutique hotel with compact luxury rooms, cafe-style common areas, and fast access to shopping and nightlife.",
        19.0596,
        72.8295,
        ["WiFi", "AC", "Breakfast", "Parking", "Pet Friendly"],
        [
            (4, "Stylish rooms and a much better location than expected."),
            (5, "Easy check-in and a lively neighborhood for evenings."),
        ],
        [3, 11, 5, 10, 4],
    ),
    build_hotel(
        "Bengaluru Sky Deck",
        "Bengaluru",
        "Indiranagar",
        7200,
        "Contemporary city hotel built for founders, remote teams, and guests who want polished rooms near food and nightlife districts.",
        12.9719,
        77.6412,
        ["WiFi", "Gym", "Breakfast", "Work Lounge", "Parking"],
        [
            (5, "Fast internet and clean work-friendly spaces."),
            (4, "Smart choice for a business stay in the city."),
        ],
        [5, 3, 0, 6, 7],
    ),
    build_hotel(
        "Cubbon Park House",
        "Bengaluru",
        "Ashok Nagar",
        6800,
        "Quiet upscale stay near central green spaces with warm interiors, reliable service, and smooth airport transfer options.",
        12.9716,
        77.5946,
        ["WiFi", "Breakfast", "AC", "Airport Shuttle", "Restaurant"],
        [
            (4, "Calm setting with dependable service and clean rooms."),
            (5, "Very convenient for central Bengaluru meetings."),
        ],
        [10, 4, 5, 8, 9],
    ),
    build_hotel(
        "Coromandel Coastline",
        "Chennai",
        "ECR",
        7400,
        "Sea-breeze resort stay with large rooms, poolside dining, and a leisure-focused vibe just outside the city rush.",
        12.9318,
        80.2676,
        ["WiFi", "Pool", "Breakfast", "Beach Access", "Parking"],
        [
            (4, "Relaxed atmosphere and generous breakfast options."),
            (5, "Perfect for a weekend reset with family."),
        ],
        [8, 1, 9, 7, 4],
    ),
    build_hotel(
        "Mylapore Courtyard",
        "Chennai",
        "Mylapore",
        5900,
        "Compact heritage-inspired hotel with local dining nearby, practical rooms, and an easier stay for temple and culture circuits.",
        13.0339,
        80.2619,
        ["WiFi", "AC", "Breakfast", "Restaurant"],
        [
            (4, "Nice balance of comfort and local character."),
            (4, "Helpful staff and smooth check-in."),
        ],
        [11, 10, 4, 3, 5],
    ),
    build_hotel(
        "Salt Lake Signature",
        "Kolkata",
        "Salt Lake",
        6100,
        "Refined urban stay with generous rooms, modern finishes, and practical business conveniences near Sector V.",
        22.5765,
        88.4318,
        ["WiFi", "Breakfast", "Gym", "Parking", "Work Lounge"],
        [
            (4, "Functional, clean, and well-run for business travel."),
            (5, "Large rooms and a very easy booking experience."),
        ],
        [0, 6, 3, 5, 7],
    ),
    build_hotel(
        "Howrah Riverside Grand",
        "Kolkata",
        "Strand Road",
        6700,
        "Classic riverside hotel with spacious suites, polished dining, and a slower luxury mood for longer stays.",
        22.5726,
        88.3639,
        ["WiFi", "Breakfast", "Restaurant", "Airport Shuttle", "AC"],
        [
            (5, "The river views and old-world scale were excellent."),
            (4, "A comfortable base with strong food service."),
        ],
        [7, 0, 4, 8, 9],
    ),
    build_hotel(
        "Charminar House",
        "Hyderabad",
        "Banjara Hills",
        6900,
        "Comfortable modern hotel with polished rooms, late-night dining, and a central base for both old city visits and business travel.",
        17.4239,
        78.4483,
        ["WiFi", "Breakfast", "Gym", "Parking", "Restaurant"],
        [
            (4, "Reliable service and good food options late in the evening."),
            (5, "The rooms feel newer than many similarly priced hotels."),
        ],
        [4, 6, 3, 0, 5],
    ),
    build_hotel(
        "Hussain Sagar Vista",
        "Hyderabad",
        "Somajiguda",
        7600,
        "Lakeside-feel business hotel with conference-ready spaces, efficient service, and strong city access.",
        17.4264,
        78.4564,
        ["WiFi", "Pool", "Breakfast", "Work Lounge", "Airport Shuttle"],
        [
            (5, "Great layout for meetings and a comfortable overnight stay."),
            (4, "Good service and easy transport connections."),
        ],
        [1, 7, 8, 9, 4],
    ),
    build_hotel(
        "Candolim Wave Resort",
        "Goa",
        "Candolim",
        8300,
        "Beach-driven resort with sunlit rooms, breezy decks, and relaxed leisure amenities built for longer vacation stays.",
        15.5186,
        73.7622,
        ["WiFi", "Pool", "Breakfast", "Beach Access", "Spa", "Parking"],
        [
            (5, "Easy walk to the beach and the pool area is excellent."),
            (5, "One of the smoother family stays we have had in Goa."),
        ],
        [9, 8, 1, 7, 4],
    ),
    build_hotel(
        "Old Goa Veranda",
        "Goa",
        "Panaji",
        7100,
        "Portuguese-inspired boutique stay mixing local character, airy verandas, and a quieter stay near Panaji's cultural core.",
        15.4909,
        73.8278,
        ["WiFi", "Breakfast", "Restaurant", "Parking", "AC"],
        [
            (4, "Charming design and a peaceful neighborhood."),
            (5, "Good blend of style, comfort, and local feel."),
        ],
        [10, 11, 4, 8, 9],
    ),
    build_hotel(
        "Malabar Bay Escape",
        "Kochi",
        "Fort Kochi",
        6400,
        "Relaxed coastal stay with heritage textures, curated seafood dining, and easy access to Kochi's arts and waterfront district.",
        9.9654,
        76.2420,
        ["WiFi", "Breakfast", "Restaurant", "Airport Shuttle", "AC"],
        [
            (4, "Pleasant ambience and very good local recommendations."),
            (5, "Ideal base for a slower Fort Kochi trip."),
        ],
        [8, 9, 1, 10, 11],
    ),
    build_hotel(
        "Backwater Pavilion",
        "Kochi",
        "Marine Drive",
        7900,
        "Contemporary waterfront hotel with large glass-front rooms, poolside views, and a polished upscale feel for couples and families.",
        9.9816,
        76.2760,
        ["WiFi", "Pool", "Breakfast", "Gym", "Parking"],
        [
            (5, "Fantastic views and the rooms feel spacious."),
            (4, "Service stayed consistent throughout the visit."),
        ],
        [1, 8, 7, 4, 5],
    ),
    build_hotel(
        "Shimla Cedar Lodge",
        "Shimla",
        "Mall Road",
        6800,
        "Hill stay with warm wood interiors, valley-facing balconies, and an easy walking distance to central attractions.",
        31.1048,
        77.1734,
        ["WiFi", "Breakfast", "Heating", "Parking", "Restaurant"],
        [
            (5, "Great mountain mood and attentive staff."),
            (4, "Comfortable rooms for a quick hill station trip."),
        ],
        [4, 7, 8, 9, 10],
    ),
    build_hotel(
        "Snowline Terrace",
        "Manali",
        "Old Manali",
        6200,
        "Casual premium retreat with rooftop fireside seating, generous mountain views, and flexible rooms for groups.",
        32.2432,
        77.1892,
        ["WiFi", "Breakfast", "Heating", "Parking", "Pet Friendly"],
        [
            (4, "The rooftop vibe and valley views were the highlight."),
            (5, "Friendly service and a very scenic setting."),
        ],
        [7, 4, 8, 10, 11],
    ),
    build_hotel(
        "Varanasi Ghat Residency",
        "Varanasi",
        "Assi Ghat",
        5600,
        "Quiet boutique stay near the river with simple luxury rooms, early breakfast service, and a practical base for temple routes.",
        25.2820,
        83.0032,
        ["WiFi", "Breakfast", "AC", "Airport Shuttle"],
        [
            (4, "Convenient location and surprisingly calm rooms."),
            (4, "Staff helped coordinate transport and local visits."),
        ],
        [10, 11, 3, 4, 5],
    ),
    build_hotel(
        "Riverfront Haven",
        "Rishikesh",
        "Tapovan",
        6000,
        "Yoga-town hotel with airy rooms, wellness-friendly amenities, and a clean minimalist style near cafes and river activity zones.",
        30.1309,
        78.3297,
        ["WiFi", "Breakfast", "Spa", "Parking", "Restaurant"],
        [
            (5, "Clean design and a very relaxed overall feel."),
            (4, "Good access to cafes and nearby activities."),
        ],
        [8, 9, 1, 4, 10],
    ),
    build_hotel(
        "Golden Temple Courtyard",
        "Amritsar",
        "Hall Bazaar",
        5800,
        "Warm hospitality stay balancing tradition and comfort with efficient service close to the city's most visited landmarks.",
        31.6340,
        74.8723,
        ["WiFi", "Breakfast", "AC", "Parking", "Restaurant"],
        [
            (4, "Comfortable rooms and a very convenient location."),
            (5, "Staff handled every request quickly and politely."),
        ],
        [11, 10, 4, 3, 6],
    ),
    build_hotel(
        "Nashik Vineyard Stay",
        "Nashik",
        "Gangapur Road",
        6500,
        "Leisure-focused retreat with vineyard-inspired interiors, open terraces, and a calm pace ideal for weekend escapes.",
        20.0110,
        73.7439,
        ["WiFi", "Pool", "Breakfast", "Parking", "Pet Friendly"],
        [
            (5, "Relaxing atmosphere and a nice change from city hotels."),
            (4, "Good for couples and short weekend trips."),
        ],
        [9, 1, 8, 7, 4],
    ),
    build_hotel(
        "Pondicherry Indigo House",
        "Puducherry",
        "White Town",
        6900,
        "French quarter boutique stay with bright interiors, cafe proximity, and an upscale but laid-back coastal feel.",
        11.9369,
        79.8348,
        ["WiFi", "Breakfast", "AC", "Beach Access", "Restaurant"],
        [
            (5, "Stylish rooms and a strong location for walking."),
            (4, "The property feels intimate and well maintained."),
        ],
        [10, 8, 11, 4, 9],
    ),
    build_hotel(
        "Mysuru Palace Avenue",
        "Mysuru",
        "Nazarbad",
        5700,
        "Refined mid-scale hotel with family rooms, heritage city access, and easy planning for local sightseeing.",
        12.3052,
        76.6552,
        ["WiFi", "Breakfast", "Parking", "Restaurant", "AC"],
        [
            (4, "Clean and practical with a polished front desk experience."),
            (4, "Worked well for a short family stop."),
        ],
        [3, 4, 10, 11, 5],
    ),
]


with app.app_context():
    try:
        db.create_all()
    except RuntimeError as exc:
        if "cryptography" in str(exc) and "caching_sha2_password" in str(exc):
            raise SystemExit(
                "MySQL requires the 'cryptography' package for the configured auth plugin. "
                "Run: pip install -r requirements.txt"
            ) from exc
        raise

    demo_user = User.query.filter_by(email="demo@stayatlas.com").first()
    if not demo_user:
        demo_user = User(full_name="Demo User", email="demo@stayatlas.com")
        demo_user.set_password("demo123")
        db.session.add(demo_user)
        db.session.commit()

    amenity_cache = {}
    for hotel_data in HOTEL_DATA:
        if Hotel.query.filter_by(name=hotel_data["name"]).first():
            continue

        hotel = Hotel(
            name=hotel_data["name"],
            city=hotel_data["city"],
            location=hotel_data["location"],
            description=hotel_data["description"],
            price_per_night=hotel_data["price_per_night"],
            main_image_url=hotel_data["main_image_url"],
            latitude=hotel_data["latitude"],
            longitude=hotel_data["longitude"],
        )

        for amenity_name in hotel_data["amenities"]:
            amenity = amenity_cache.get(amenity_name) or Amenity.query.filter_by(name=amenity_name).first()
            if not amenity:
                amenity = Amenity(name=amenity_name)
                db.session.add(amenity)
                db.session.flush()
            amenity_cache[amenity_name] = amenity
            hotel.amenities.append(amenity)

        db.session.add(hotel)
        db.session.flush()

        for image_url in hotel_data["images"]:
            db.session.add(HotelImage(hotel_id=hotel.id, image_url=image_url))

        for review_data in hotel_data["reviews"]:
            db.session.add(
                Review(
                    user_id=demo_user.id,
                    hotel_id=hotel.id,
                    rating=review_data["rating"],
                    comment=review_data["comment"],
                )
            )

    db.session.commit()
    print("Database seeded. Demo login: demo@stayatlas.com / demo123")
