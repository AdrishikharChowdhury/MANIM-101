from manim import *
from PIL import Image, ImageFilter


class Chips_Admin_Borrow_Outro(Scene):
    def construct(self):
        img_path = "./assets/background.jpg"
        raw_img = Image.open(img_path)
        blurred_img = raw_img.filter(ImageFilter.GaussianBlur(radius=10))
        bg = ImageMobject(blurred_img)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)

        title = Text("Thank You For Watching!", weight=BOLD)
        box = SurroundingRectangle(
            title, buff=0.75, color="#e9bab3",
            fill_color=BLACK, fill_opacity=0.5
        )

        self.play(FadeIn(bg), run_time=1)
        self.play(DrawBorderThenFill(box), run_time=2)
        self.play(Write(title), run_time=2)
        self.wait(2.5)
        self.play(FadeOut(bg), FadeOut(box), FadeOut(title), run_time=1)
