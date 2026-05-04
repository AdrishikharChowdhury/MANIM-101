from manim import *
from PIL import Image,ImageFilter

class Background(Scene):
    def construct(self):
        img_path="background.jpg"
        raw_img=Image.open(img_path)
        blurred_img=raw_img.filter(ImageFilter.GaussianBlur(radius=10))

        bg=ImageMobject(blurred_img)

        bg.scale_to_fit_width(config.frame_width)

        self.add(bg)

        intro=Text("Welcome to the Video",color=WHITE).scale(1.5)
        box=SurroundingRectangle(intro,buff=0.5,color=WHITE,fill_color=BLACK,fill_opacity=0.5)
        self.play(FadeIn(bg),run_time=1)
        self.play(DrawBorderThenFill(box),run_time=1)
        self.play(Write(intro),run_time=2)
        self.play(FadeOut(intro),FadeOut(box),FadeOut(bg),run_time=1)
        self.wait()