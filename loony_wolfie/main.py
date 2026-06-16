from manim import *


class Loony_Wolfie_Intro(Scene):
    def construct(self):
        text = Text("Hello From Loony Wolfie")
        self.play(Write(text))
        self.wait()
