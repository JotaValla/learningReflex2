import reflex as rx
from learningReflex2.components.link_button import link_button
from learningReflex2.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Links"),
        link_button(title="Home", body="Welcome to my website", url="https://www.google.com"),
        link_button(title="About", body="About me", url="https://www.google.com"),
        link_button(title="Contact", body="Contact me", url="https://www.google.com"),
        link_button(title="Blog", body="Read my blog", url="https://www.google.com"),
        title("Links"),
        link_button(title="Home", body="Welcome to my website", url="https://www.google.com"),
        link_button(title="About", body="About me", url="https://www.google.com"),
        link_button(title="Contact", body="Contact me", url="https://www.google.com"),
        link_button(title="Blog", body="Read my blog", url="https://www.google.com"),
        width="100%",
        justify_content="center",
        align_items="center",
        spacing="4",
        padding="4"
    )