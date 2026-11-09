from manim import *
from PIL import Image, ImageFilter


def GroupTextImage(path, text):
    image = SVGMobject(path)
    image.height = 1.1
    label = Text(text, color=WHITE, weight=BOLD).next_to(image, DOWN, buff=0.15).scale(0.55)
    return VGroup(image, label)


class RRS_Intro(Scene):
    def construct(self):
        img_path = "./assets/background.jpg"
        raw_img = Image.open(img_path).convert("RGB")
        blurred_img = raw_img.filter(ImageFilter.GaussianBlur(radius=10))
        bg = ImageMobject(blurred_img)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)

        java_group = GroupTextImage("./assets/java.svg", "OpenJDK 27")
        stack_group = VGroup(java_group)

        title = Text("Round-Robin Scheduling", weight=BOLD).scale(0.95)
        subtitle = Text("CPU Scheduling Simulation", weight=LIGHT).scale(0.55)
        footnote = Text("Java  •  Time Quantum  •  FIFO Queue", weight=LIGHT).scale(0.42)
        content = VGroup(title, subtitle, footnote).arrange(DOWN, buff=0.3).shift(UP * 0.9)
        box = SurroundingRectangle(
            content,
            buff=0.55,
            color="#e9bab3",
            fill_color=BLACK,
            fill_opacity=0.5,
        )
        stack_group.next_to(box, DOWN, buff=0.5)

        self.play(FadeIn(bg), run_time=1)
        self.play(DrawBorderThenFill(box), run_time=2)
        self.play(Write(title), run_time=2)
        self.play(Write(subtitle), run_time=1.5)
        self.play(Write(footnote), run_time=1)
        self.play(FadeIn(stack_group, shift=UP * 0.3), run_time=1.5)
        self.wait(2.5)


def main() -> None:
    pass
