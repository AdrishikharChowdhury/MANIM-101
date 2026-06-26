from manim import *
from PIL import Image, ImageFilter


def GroupTextImage(path, text):
    image = SVGMobject(path)
    label = Text(text, color=WHITE, weight=BOLD).next_to(image, DOWN).scale(0.75)
    return VGroup(image, label)


class Chips_Backend_Intro(Scene):
    def construct(self):
        img_path = "./assets/background.jpg"
        raw_img = Image.open(img_path)
        blurred_img = raw_img.filter(ImageFilter.GaussianBlur(radius=10))
        bg = ImageMobject(blurred_img)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)

        auth_group = GroupTextImage("./assets/authjs.svg", "Auth.js")
        neon_group = GroupTextImage("./assets/neon.svg", "Neon")
        redis_group = GroupTextImage("./assets/redis.svg", "Redis")
        workflow_group = GroupTextImage("./assets/workflow.svg", "Workflow")
        imagekit_group = GroupTextImage("./assets/imagekit.svg", "ImageKit")
        imagekit_group.scale(0.6)
        nodemailer_group = GroupTextImage("./assets/nodemailer.svg", "Nodemailer")
        stack_group = (
            VGroup(
                auth_group,
                neon_group,
                redis_group,
                workflow_group,
                imagekit_group,
                nodemailer_group,
            )
            .arrange(RIGHT, buff=0.75)
            .scale(0.6)
        )

        title = Text("C.H.I.P.S.", weight=BOLD).scale(1.25)
        subtitle = Text(
            "Centralized Hardware Inventory for Prototype Systems", weight=LIGHT
        ).scale(0.5)
        footnote1 = Text("Backend Infrastructure", weight=LIGHT).scale(0.5)
        footnote2 = (
            Text("Stage: Backend Setup", weight=LIGHT)
            .scale(0.5)
            .next_to(footnote1, DOWN, buff=0.1)
        )
        footnotes = VGroup(footnote1, footnote2)
        content = (
            VGroup(title, subtitle, footnotes)
            .arrange(DOWN, buff=0.3)
            .scale(0.8)
            .shift(UP * 0.8)
        )
        box = SurroundingRectangle(
            content,
            buff=0.5,
            color="#e9bab3",
            fill_color=BLACK,
            fill_opacity=0.5,
        )
        stack_group.next_to(box, DOWN, buff=0.5)

        self.play(FadeIn(bg), run_time=1)
        self.play(DrawBorderThenFill(box), run_time=2)
        self.play(Write(title), run_time=2)
        self.play(Write(subtitle), run_time=2)
        self.play(Write(footnotes), run_time=1)
        self.play(Write(stack_group), run_time=2)
        self.wait(2.5)
