from manim import *
from PIL import Image, ImageFilter


def GroupTextImage(path, text):
    image = SVGMobject(path)
    label = Text(text, color=WHITE, weight=BOLD).next_to(image, DOWN).scale(0.75)
    return VGroup(image, label)


class WV_Intro(Scene):
    def construct(self):
        img_path = "./assets/naruto-uzumaki-3840x2160-22818.jpg"
        raw_img = Image.open(img_path)
        blurred_img = raw_img.filter(ImageFilter.GaussianBlur(radius=10))
        bg = ImageMobject(blurred_img)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)

        python_group = GroupTextImage("./assets/python-svgrepo-com.svg", "Python")
        stack_group = VGroup(python_group).scale(0.6)

        title = Text("Wallpaper Viewer", weight=BOLD).scale(1.25)
        subtitle = Text("Beautiful Wallpapers at Your Fingertips", weight=LIGHT).scale(0.5)
        footnote = Text("Python Module", weight=LIGHT).scale(0.5)
        content = VGroup(title, subtitle, footnote).arrange(DOWN, buff=0.3).scale(0.8).shift(UP * 0.8)
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
        self.play(Write(footnote), run_time=1)
        self.play(Write(stack_group), run_time=2)
        self.wait(2.5)


def main() -> None:
    pass
