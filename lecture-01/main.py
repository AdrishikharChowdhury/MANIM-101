from manim import *

class Lecture01(Scene):
    def construct(self):
        title = Text("Lecture 01: Introduction to Manim").shift(UP)
        subtitle = Text("Creating Animations with Python").shift(DOWN).scale(0.7)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        
        self.wait(2)