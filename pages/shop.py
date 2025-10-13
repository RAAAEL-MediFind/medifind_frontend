from nicegui import ui


def product_card(image, title, categories, old_price, new_price=None, discount=None):
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


@ui.page("/shop")
def shop_page():
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
