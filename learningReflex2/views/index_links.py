import reflex as rx
from learningReflex2.components.link_button import link_button
from learningReflex2.components.title import title
from learningReflex2.routes import Route

def links() -> rx.Component:
    return rx.vstack(
        title("Links"),
        link_button(title="Home", body="Welcome to my website", url="https://www.google.com", src_icon="house"),
        link_button(title="About", body="About me", url="https://www.google.com", src_icon="instagram"),
        link_button(title="Contact", body="Contact me", url="https://www.google.com", src_icon="contact"),
        link_button(title="Blog", body="Read my blog", url="https://www.google.com", src_icon="clipboard-minus"),
        title("Links"),
        link_button(title="Courses", body="See my courses", url=Route.COURSES.value, src_icon="code", external_url=False),
        link_button(title="About", body="About me", url="https://www.google.com", src_icon="contact"),
        link_button(title="Contact", body="Contact me", url="https://www.google.com", src_icon="link"),
        link_button(title="Blog", body="Read my blog", url="https://www.google.com", src_icon="clipboard-minus"),
        width="100%",
        justify_content="center",
        align_items="center",
        spacing="4",
        padding="4"
    )