from manim import *
from PIL import Image,ImageFilter

class Logos(Scene):
    def construct(self):
        img_path="./assets/background.webp"
        mongo_path="./assets/mongodb.svg"
        next_path="./assets/nextjs.svg"
        ts_path="./assets/typescript.svg"
        raw_img=Image.open(img_path)
        blurred_image=raw_img.filter(ImageFilter.GaussianBlur(radius=10))
        bg=ImageMobject(blurred_image)

        mongo_image=SVGMobject(mongo_path).scale(0.8)
        mongo_text=Text("MongoDB",color=WHITE).next_to(mongo_image,DOWN).scale(0.5)

        next_image=SVGMobject(next_path).scale(0.8).set_color(WHITE)
        next_text=Text("Next JS",color=WHITE).next_to(next_image,DOWN).scale(0.5)

        ts_image=SVGMobject(ts_path).scale(0.8)
        ts_text=Text("Typescript",color=WHITE).next_to(ts_image,DOWN).scale(0.5)
        

        mongo_group=VGroup(mongo_image,mongo_text).shift(LEFT*2.5)
        next_group=VGroup(next_image,next_text)
        ts_group=VGroup(ts_image,ts_text).shift(RIGHT*2.5)

        
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)

        self.play(FadeIn(bg))
        self.play(Write(mongo_group),Write(next_group),Write(ts_group),run_time=2)
        self.play(FadeOut(mongo_group),FadeOut(next_group),FadeOut(ts_group),run_time=2)
        self.play(FadeOut(bg))
