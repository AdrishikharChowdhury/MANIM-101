from manim import *
from PIL import Image,ImageFilter

def FadeOutComponents(self,bg,components):
    self.play(FadeOut(bg),*[FadeOut(component) for component in components],run_time=1)

def GroupTextImage(path,text):
    if text=="Next JS" :
        image=SVGMobject(path).set_color(WHITE)
    else:
        image=SVGMobject(path)
    text=Text(text,color=WHITE,weight=BOLD).next_to(image,DOWN).scale(0.75)
    return VGroup(image,text)

def WriteTextBox(self,components):
    for component in components:
        WriteScene(self,component)
    
def WriteScene(self,component):
    if isinstance(component,SurroundingRectangle):
        self.play(DrawBorderThenFill(component),run_time=2) 
    else:
        self.play(Write(component),run_time=2)

class BasicIntro(Scene):
    def construct(self):
        img_path="./assets/background.jpg"
        mongo_path="./assets/mongodb.svg"
        next_path="./assets/nextjs.svg"
        ts_path="./assets/typescript.svg"

        raw_img=Image.open(img_path)
        blurred_img=raw_img.filter(ImageFilter.GaussianBlur(radius=10))
        bg=ImageMobject(blurred_img)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)

        mongo_group=GroupTextImage(mongo_path,"MongoDB")
        next_group=GroupTextImage(next_path,"Next JS")
        ts_group=GroupTextImage(ts_path,"TypeScript")

        stack_group=VGroup(mongo_group,next_group,ts_group).arrange(RIGHT,buff=0.75).shift(DOWN*2).scale(0.6)

        title=Text("Enter Title of the Intro",weight=BOLD).shift(UP)
        subtitle=Text("Enter the Subtitle of the Intro",weight=LIGHT).scale(0.5)
        box=SurroundingRectangle(title,subtitle,buff=0.75,color=BLUE,fill_color=BLACK,fill_opacity=0.5)
        components=[box,title,subtitle,stack_group]

        self.play(FadeIn(bg),run_time=1)
        WriteTextBox(self,components)
        FadeOutComponents(self,bg,components)