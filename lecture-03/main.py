from manim import *

class Shapes(Scene):
    def construct(self):
        circle=Circle(radius=2.5, stroke_color=GREEN, fill_color=BLUE,fill_opacity=0.75)
        square=Square(side_length=5,stroke_color=GREEN, fill_color=BLUE,fill_opacity=0.75)
        rectangle=Rectangle(width=3,height=5,stroke_color=GREEN, fill_color=BLUE,fill_opacity=0.75)
        shapeGroup=VGroup(circle,square,rectangle)
        shapeGroup.arrange(RIGHT,buff=0.5)
        shapeGroup.move_to(ORIGIN)
        self.play(Create(shapeGroup),run_time=5)
        self.wait(1.5)
