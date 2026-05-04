from manim import *

class Testing(Scene):
    def construct(self):
        name=Text("Adrishikhar Chowdhury").to_edge(UL,buff=1)
        square=Square(side_length=2.5,fill_color=RED,fill_opacity=0.75).shift(LEFT*3)
        triangle=Triangle().scale(1.2).to_edge(DR)

        self.play(Write(name))
        self.play(DrawBorderThenFill(square))
        self.play(Create(triangle))
        self.wait()

        self.play(name.animate.to_edge(UR,buff=1),run_time=2)
        self.play(square.animate.scale(2.5),triangle.animate.move_to(ORIGIN),run_time=4)
        self.wait()