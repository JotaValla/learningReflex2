from enum import Enum
import reflex as rx
from learningReflex2.styles.colors import Colors, TextColors
from learningReflex2.styles.fonts import Fonts

MAX_WIDTH = "500px"

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "2em"


GLOBAL_STYLES = {
    "font_family": Fonts.DEFAULT.value,
    "background_color": Colors.BACKGROUND.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.DEFAULT.value,
        "border_radius": Size.DEFAULT.value,
        "text_color": TextColors.HEADER.value,
        "background_color": Colors.SECONDARY.value,
        "_hover": {
            "background_color": Colors.PRIMARY.value,
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    color=TextColors.HEADER.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    color=TextColors.BODY.value,
)

title_style = dict(
    padding_top=Size.SMALL.value,
    width="100%", 
    font_weight="bold",
)

navbar_style = dict(
    font_family=Fonts.NAVBAR.value,
    font_size=Size.LARGE.value,
)


