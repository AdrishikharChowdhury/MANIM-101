from manim import *
import numpy as np

class Waves(Scene):
    def construct(self):
        axes=Axes(x_range=[-10,10],y_range=[-2,2])
        grid=NumberPlane(x_range=[-10,10],y_range=[-2,2],background_line_style={"stroke_color":GREY,"stroke_width":1})

        graph=axes.plot(lambda x:np.sin(x),color=BLUE)
        self.play(Create(graph),Create(axes),Create(grid))

        self.wait(2)