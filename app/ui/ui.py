"""The main Chat app."""

import reflex as rx
from ui.components import chat, navbar, spline
#from reflex_spline import spline
# from reflex_clerk import clerk_provider, sign_in_button, install_signin_page

def index() -> rx.Component:
    """The main app."""
    return rx.chakra.vstack(
        navbar(),
        #spline(scene="https://prod.spline.design/joLpOOYbGL-10EJ4/scene.splinecode"),
        chat.chat(),
        chat.action_bar(),
        background_color=rx.color("mauve", 1),
        color=rx.color("mauve", 12),
        min_height="100vh",
        align_items="stretch",
        spacing="0",
    )


# Add state and page to the app.
app = rx.App(theme=rx.theme(appearance="dark",accent_color="violet",),)
app.add_page(index)
