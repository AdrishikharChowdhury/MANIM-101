from manim import *
from PIL import Image, ImageFilter


def GroupTextImage(path, text):
    image = SVGMobject(path)
    label = Text(text, color=WHITE, weight=BOLD).next_to(image, DOWN).scale(0.75)
    return VGroup(image, label)


class Loony_Wolfie_Intro(Scene):
    def construct(self):
        img_path = "./assets/background.jpg"
        raw_img = Image.open(img_path)
        blurred_img = raw_img.filter(ImageFilter.GaussianBlur(radius=10))
        bg = ImageMobject(blurred_img)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)

        next_group = GroupTextImage("./assets/nextjs-light.svg", "Next JS")
        ts_group = GroupTextImage("./assets/typescript.svg", "TypeScript")
        stack_group = (
            VGroup(next_group, ts_group)
            .arrange(RIGHT, buff=0.75)
            .scale(0.6)
        )

        title = Text("Loony Wolfie", weight=BOLD)
        subtitle = Text("Build With A Plan", weight=LIGHT).scale(0.5)
        footnote1 = Text("Developers Journey", weight=LIGHT).scale(0.25)
        footnote2 = (
            Text("Stage: Landing Page and Basic Frontend", weight=LIGHT)
            .scale(0.25)
            .next_to(footnote1, DOWN, buff=0.1)
        )
        footnotes = VGroup(footnote1, footnote2)
        content = VGroup(title, subtitle, footnotes).arrange(DOWN, buff=0.3).scale(0.8)
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
