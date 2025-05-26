import learningReflex2.styles.styles as styles
from learningReflex2.components.navbar import navbar
from learningReflex2.views.header import header
from learningReflex2.views.index_links import links
from learningReflex2.components.footer import footer
from learningReflex2.routes import Route
import reflex as rx
import learningReflex2.utils as utils

class State (rx.State):
    """State for the index page."""
    # Add any state variables if needed
    pass

@rx.page(
    route= Route.INDEX.value,
    title = utils.index_title,
    description = utils.index_description,
    image=utils.preview,
    meta = utils.index_meta,
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
            header(details=True),
            links(),
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin=styles.Size.LARGE.value,
            padding=styles.Size.DEFAULT.value,
            ),
        ),
        footer(),
    )
