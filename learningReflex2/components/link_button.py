import reflex as rx
import learningReflex2.styles.styles as styles

def link_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="instagram",
                    width=styles.Size.LARGE.value,
                    height=styles.Size.LARGE.value,
                    margin=styles.Size.SMALL.value,
                    ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing="0",
                    align_items="left",
                    margin=styles.Size.ZERO.value,
                ),
            ),
            width="100%",
            justify="center",
            align="center",
        ),
        href=url,
        is_external=True,
        width="100%",
    )