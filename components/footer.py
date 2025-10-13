from nicegui import ui,app

def show_footer():
    """MediFind Footer (unified blue gradient theme, scrolls with page)"""
    with ui.element("footer").classes(
        "bg-blue-400 text-gray-400 w-full mt-16 px-8 py-10"
    ):
        with ui.element("div").classes("max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8"):
            
            # About
            with ui.column().classes("space-y-3"):
                ui.label("About MediFind").classes("text-lg font-semibold text-white")
                ui.label(
                    "MediFind helps you locate medicines from verified pharmacies across Ghana — quickly, safely, and reliably."
                ).classes("text-sm leading-relaxed text-blue-100")

                # Social icons
                with ui.row().classes("gap-4 mt-3"):
                    for icon, link in [
                        ("facebook", "#"),
                        ("instagram", "#"),
                        ("twitter", "#"),
                        ("linkedin", "#"),
                    ]:
                        ui.link("", link, new_tab=True).classes(
                            "hover:opacity-80 transition"
                        ).props(f"icon={icon}")

            # Quick Links
            with ui.column().classes("space-y-3"):
                ui.label("Quick Links").classes("text-lg font-semibold text-white")
                for name, link in [
                    ("Home", "/"),
                    ("Find Medicine", "/find"),
                    ("Upload Prescription", "/upload"),
                    ("My Orders", "/orders"),
                    ("Contact Us", "/contact"),
                ]:
                    ui.link(name, link).classes(
                        "text-sm text-blue-100 hover:text-white transition"
                    )

            # Contact
            with ui.column().classes("space-y-3"):
                ui.label("Contact Us").classes("text-lg font-semibold text-white")
                ui.label("📍 Accra, Ghana").classes("text-sm text-blue-100")
                ui.label("📞 +233 20 123 4567").classes("text-sm text-blue-100")
                ui.label("✉️ support@medifind.com").classes("text-sm text-blue-100")

        # Footer bottom line
        with ui.row().classes("justify-center mt-8 border-t border-blue-300 pt-4"):
            ui.label("© 2025 MediFind. All rights reserved.").classes("text-xs text-blue-100")
