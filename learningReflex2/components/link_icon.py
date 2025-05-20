import reflex as rx
import learningReflex2.styles.styles as styles


def link_icon(name: str, url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag=name,
        ),
        href=url,
        is_external=True,
    )
