from nicegui import ui


def show_navbar():
    with ui.header().classes("bg-[#34989e] text-white p-0 h-8"):

        with ui.row().classes("w-full bg-[#34989e] items-center p-6"):

            with ui.row().classes("p-2 "):
                # Replace with an actual image link if you have one
                ui.label("MediFind").classes("text-4xl font-bold text-white-400")

                ui.link("Home", target="/home").classes(
                    "text-white font-semibold p-2 no-underline ml-20"
                )
                ui.link("Shop +", target="/shop").classes(
                    "text-white font-semibold p-2 no-underline ml-20"
                )

                ui.link("Contact", target="/contact").classes(
                    "text-white font-semibold p-2 no-underline ml-20"
                )

            with ui.row().classes("items-center text-white gap-4 ml-60"):
                ui.link("SIGN IN ", target="/signin").classes(
                    "text-white font-semibold no-underline"
                )
                ui.link("SIGN UP", target="/signup").classes(
                    "text-white font-semibold no-underline"
                )
                # Wishlist Icon
                ui.icon("favorite_border", size="md").classes(
                    "hover:text-red-400 cursor-pointer"
                )

                # Shopping Cart (with badge)
                with ui.row().classes("items-center"):
                    ui.icon("shopping_cart", size="md").classes("cursor-pointer")

            # --- 3. BOTTOM BAR (Navigation) ---
            # Using a simple row for the main navigation links

            # Dashboard Button
            ui.button(
                "Dashboard", on_click=lambda: ui.navigate("/userdashboard")
            ).classes(
                "bg-blue-800 text-white font-semibold text-sm px-4 py-1.5 rounded-full shadow-md "
                "hover:bg-blue-700 transition-colors duration-200"
            )

    # Setting the theme color for the rest of the application to match the header
    ui.add_head_html("<style>body { background-color: white; }</style>")

    # 3. Right: User Actions (Icons and Button)
