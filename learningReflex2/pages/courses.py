import learningReflex2.styles.styles as styles
from learningReflex2.components.navbar import navbar
from learningReflex2.views.header import header
from learningReflex2.views.courses_links import links 
from learningReflex2.components.footer import footer
from learningReflex2.routes import Route
import reflex as rx
import learningReflex2.utils as utils

@rx.page(
    route= Route.COURSES.value,
    title = utils.courses_title,
    description = utils.courses_description,
    image=utils.preview,
    meta = utils.course_meta,
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
            header(details=False),
            links(),
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin=styles.Size.LARGE.value,
            padding=styles.Size.DEFAULT.value,
            ),
        ),
        footer(),
    )
