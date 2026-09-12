from manim import *
from PIL import Image, ImageFilter


class Chips_Org_Intro(Scene):
    def construct(self):
        img_path = "./assets/background.jpg"
        raw_img = Image.open(img_path)
        blurred_img = raw_img.filter(ImageFilter.GaussianBlur(radius=10))
        bg = ImageMobject(blurred_img)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)

        title = Text("C.H.I.P.S.", weight=BOLD).scale(1.25)
        subtitle = Text("Centralized Hardware Inventory for Prototype Systems", weight=LIGHT).scale(0.5)
        footnote1 = Text("Developer's Journey", weight=LIGHT).scale(0.5)
        footnote2 = Text("Stage: Organization Module", weight=LIGHT).scale(0.5).next_to(footnote1, DOWN, buff=0.1)
        footnotes = VGroup(footnote1, footnote2)
        content = VGroup(title, subtitle, footnotes).arrange(DOWN, buff=0.3).scale(0.8)
        box = SurroundingRectangle(
            content,
            buff=0.5,
            color="#e9bab3",
            fill_color=BLACK,
            fill_opacity=0.5,
        )

        self.play(FadeIn(bg), run_time=1)
        self.play(DrawBorderThenFill(box), run_time=2)
        self.play(Write(title), run_time=2)
        self.play(Write(subtitle), run_time=2)
        self.play(Write(footnotes), run_time=1)
        self.wait(2.5)
