const searchInput = document.getElementById("hotel-search");
const suggestionBox = document.getElementById("search-suggestions");
const siteHeader = document.querySelector(".site-header");

if (siteHeader) {
    const updateHeaderState = () => {
        siteHeader.classList.toggle("site-header-scrolled", window.scrollY > 16);
    };

    updateHeaderState();
    window.addEventListener("scroll", updateHeaderState, { passive: true });
}

if (searchInput && suggestionBox) {
    let currentRequest = null;

    searchInput.addEventListener("input", async (event) => {
        const query = event.target.value.trim();
        suggestionBox.innerHTML = "";
        suggestionBox.classList.remove("visible");

        if (query.length < 2) {
            return;
        }

        if (currentRequest) {
            currentRequest.abort();
        }

        currentRequest = new AbortController();

        try {
            const response = await fetch(`/api/hotel-suggestions?q=${encodeURIComponent(query)}`, {
                signal: currentRequest.signal,
            });
            const suggestions = await response.json();

            if (!suggestions.length) {
                return;
            }

            suggestions.forEach((suggestion) => {
                const button = document.createElement("button");
                button.type = "button";
                button.textContent = `${suggestion.label} (${suggestion.type})`;
                button.addEventListener("click", () => {
                    searchInput.value = suggestion.label;
                    suggestionBox.classList.remove("visible");
                });
                suggestionBox.appendChild(button);
            });
            suggestionBox.classList.add("visible");
        } catch (error) {
            if (error.name !== "AbortError") {
                console.error("Suggestion lookup failed", error);
            }
        }
    });

    document.addEventListener("click", (event) => {
        if (!suggestionBox.contains(event.target) && event.target !== searchInput) {
            suggestionBox.classList.remove("visible");
        }
    });
}

const bookingForm = document.getElementById("booking-form");

if (bookingForm) {
    const totalElement = document.getElementById("booking-total");
    const checkInInput = bookingForm.querySelector("input[name='check_in']");
    const checkOutInput = bookingForm.querySelector("input[name='check_out']");
    const nightlyPrice = Number(bookingForm.dataset.price || 0);

    const updateTotal = () => {
        const checkIn = new Date(checkInInput.value);
        const checkOut = new Date(checkOutInput.value);

        if (Number.isNaN(checkIn.getTime()) || Number.isNaN(checkOut.getTime())) {
            totalElement.innerHTML = "&#8377;0";
            return;
        }

        const nights = Math.ceil((checkOut - checkIn) / (1000 * 60 * 60 * 24));
        const total = nights > 0 ? nights * nightlyPrice : 0;
        totalElement.innerHTML = `&#8377;${total.toLocaleString("en-IN")}`;
    };

    checkInInput.addEventListener("change", updateTotal);
    checkOutInput.addEventListener("change", updateTotal);
}

const revealItems = document.querySelectorAll(".reveal");

if (revealItems.length) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) {
                return;
            }

            entry.target.classList.add("revealed");
            observer.unobserve(entry.target);
        });
    }, {
        threshold: 0.15,
        rootMargin: "0px 0px -40px 0px",
    });

    revealItems.forEach((item) => revealObserver.observe(item));
}
