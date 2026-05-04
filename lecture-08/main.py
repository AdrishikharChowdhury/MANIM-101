from manim import *
from PIL import Image,ImageFilter

def FadeOutComponents(self,bg,components):
    self.play(FadeOut(bg),*[FadeOut(component) for component in components],run_time=1)

def WriteTextBox(self,components):
    for component in components:
        WriteScene(self,component)
    
def WriteScene(self,component):
    if isinstance(component,SurroundingRectangle):
        self.play(DrawBorderThenFill(component),run_time=2) 
    else:
        self.play(Write(component),run_time=2)

class BasicOutro(Scene):
    def construct(self):
        img_path="./assets/background.jpg"
        raw_img=Image.open(img_path)
        blurred_img=raw_img.filter(ImageFilter.GaussianBlur(radius=10))
        bg=ImageMobject(blurred_img)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)

        title=Text("Thank You For Watching!",weight=BOLD)
        box=SurroundingRectangle(title,buff=0.75,color=BLUE,fill_color=BLACK,fill_opacity=0.5)
        components=[box,title]

        self.play(FadeIn(bg),run_time=1)
        WriteTextBox(self,components)
        FadeOutComponents(self,bg,components)