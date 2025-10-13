from nicegui import ui, app
from components.navbar import show_navbar
from components.footer import show_footer
import requests

PHARMACIES = [
    {"name": "MediCare", "link_name": "medicare"},
    {"name": "Wellness Rx", "link_name": "wellness_rx"},
    {"name": "Local Drug Mart", "link_name": "local_drug_mart"},
]


@ui.page("/pharmacy/{name}")
def show_pharmacy_page(name: str):

    pharmacy_info = next(
        (p for p in PHARMACIES if p["link_name"] == name),
        {"name": name.replace("_", " ").title()},
    )
    pharmacy_name = pharmacy_info["name"]

    ui.page_title(f"{pharmacy_name} - Shop Home")

    ui.add_head_html(
        """
    <style>
        body { margin: 0; font-family: 'Poppins', sans-serif; }
        .hero-bg { 
            background-color: #f0f7fa; /* Light blue/grey background */
            /* Add padding and positioning for the background elements */
            padding-bottom: 500px; /* Ensure space for the full hero section */
        }
        .search-container {
            width: 100%;
            max-width: 600px;
        }
    </style>
    """
    )

    with ui.column().classes("w-full items-center pt-20 relative hero-bg min-h-screen"):

        ui.label("What Are You Looking For?").classes(
            "text-5xl font-extrabold text-gray-800 mt-16"
        )
        ui.label("The pharmacy that really delivers").classes(
            "text-lg text-gray-600 mt-2 mb-10"
        )

        with ui.row().classes(
            "search-container shadow-lg rounded-full overflow-hidden bg-white"
        ):

            with ui.row().classes(
                "px-4 py-3 border-r border-gray-200 items-center hidden sm:flex"
            ):
                ui.select(
                    options=["All categories", "Prescription", "OTC", "Vitamins"],
                    value="All categories",
                ).classes("bg-white text-sm w-36 ").props("borderless dense")

            ui.input(placeholder="search product").classes(
                "flex-grow bg-white text-lg h-full"
            ).props("borderless dense")

            ui.button(icon="search").props("flat color=black text-primary").classes(
                "text-lg w-16 h-full"
            )

        ui.image("assets/product_tube.png").classes(
            "absolute w-[300px] right-[10%] bottom-[10%] transform -translate-y-1/2"
        ).style("z-index: 1;")

        ui.image("assets/blister_pack.png").classes(
            "absolute w-[200px] top-[10%] left-[5%] opacity-70 rotate-[-15deg]"
        )

        ui.button("Back to Directory", on_click=lambda: ui.open("/")).classes(
            "mt-12 mb-4 bg-primary-dark"
        ).props("flat").style("z-index: 10;")

    def product_card(
        image, title, categories, old_price, new_price=None, discount=None
    ):
        with ui.column().style(" background-color: #f0f7fa;"):
            with ui.card().classes(
                "w-80 rounded-2xl shadow-md hover:shadow-lg transition p-4 flex flex-col justify-between"
            ):
                # Product Image & Discount Badge
                with ui.row().classes("relative justify-center"):
                    ui.image(image).classes("h-48 w-auto rounded-xl object-contain")

                # Product Info
                with ui.column().classes("mt-3 text-center"):
                    ui.label(categories).classes("text-xs text-gray-400")
                    ui.label(title).classes("font-semibold text-gray-800 text-base")

                    # Rating stars (simple static stars)
                    with ui.row().classes("justify-center my-1"):
                        for i in range(4):
                            ui.icon("star").classes("text-yellow-400 text-sm")
                        ui.icon("star_half").classes("text-yellow-400 text-sm")

                    # Price section
                    with ui.row().classes("justify-center items-center gap-2"):
                        if new_price:
                            ui.label(f"${old_price}").classes(
                                "line-through text-gray-400 text-sm"
                            )
                            ui.label(f"${new_price}").classes(
                                "text-pink-600 font-bold text-lg"
                            )
                        else:
                            ui.label(f"${old_price}").classes(
                                "text-gray-800 font-semibold text-lg"
                            )

                # Add to cart button
                with ui.row().classes("justify-center mt-3"):
                    ui.button("ADD TO CART", icon="shopping_cart").classes(
                        " hover:bg-teal-700 text-white px-4 py-2 rounded-full shadow"
                    ).props("color=teal-600")

        with ui.column().style(" background-color: #f0f7fa;").classes("ml-60 bg-cover"):
            with ui.column():
                ui.label("Shop Products").classes(
                    "text-3xl font-bold text-center mt-6 mb-4"
                )

            # Products Grid
            with ui.row().classes("justify-center flex-wrap gap-6 mb-10"):
                product_card(
                    image="https://via.placeholder.com/150",
                    title="Online Only Triple Oxygen",
                    categories="Covid Essentials, Health Conditions, Treatments",
                    old_price="193.38",
                    new_price="115.00",
                    discount="41",
                )

                product_card(
                    image="https://via.placeholder.com/150",
                    title="Oral Irrigator Electric",
                    categories="Health Conditions, OTC Deals, Treatments",
                    old_price="173.68",
                )

                product_card(
                    image="https://via.placeholder.com/150",
                    title="Organika Salmon Collagen",
                    categories="Diabetes, Fitness, Health Conditions",
                    old_price="124.98",
                )
                product_card(
                    image="https://via.placeholder.com/150",
                    title="Organika Salmon Collagen",
                    categories="Diabetes, Fitness, Health Conditions",
                    old_price="124.98",
                )
                product_card(
                    image="https://via.placeholder.com/150",
                    title="Organika Salmon Collagen",
                    categories="Diabetes, Fitness, Health Conditions",
                    old_price="124.98",
                )
                product_card(
                    image="https://via.placeholder.com/150",
                    title="Organika Salmon Collagen",
                    categories="Diabetes, Fitness, Health Conditions",
                    old_price="124.98",
                )

    show_footer()
