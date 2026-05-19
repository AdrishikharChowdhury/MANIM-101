from manim import *
from PIL import Image,ImageFilter

def FadeOutComponents(self,bg,components):
    self.play(FadeOut(bg),*[FadeOut(component) for component in components],run_time=1)

def GroupTextImage(path,text):
    if text=="Groq":
        image=SVGMobject(path).set_color(WHITE)
    if text=="Supabase":
        image=SVGMobject(path)
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

class LearnHubIntro(Scene):
    def construct(self):
        img_path="./assets/background.png"
        supabase_path="./assets/supabase.svg"
        next_path="./assets/nextjs-light.svg"
        ts_path="./assets/typescript.svg"
        clerk_path="./assets/symbol-primary.svg"
        vapi_path="./assets/va-square-2.svg"
        groq_path="./assets/groq.svg"

        raw_img=Image.open(img_path)
        blurred_img=raw_img.filter(ImageFilter.GaussianBlur(radius=10))
        bg=ImageMobject(blurred_img)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)

        supabase_group=GroupTextImage(supabase_path,"Supabase")
        next_group=GroupTextImage(next_path,"Next JS")
        ts_group=GroupTextImage(ts_path,"TypeScript")
        clerk_group=GroupTextImage(clerk_path,"Clerk")
        vapi_group=GroupTextImage(vapi_path,"Vapi")
        groq_group=GroupTextImage(groq_path,"Groq")

        stack_group=VGroup(supabase_group,next_group,ts_group,clerk_group,vapi_group,groq_group).arrange(RIGHT,buff=0.75).shift(DOWN*2).scale(0.6)

        title=Text("Project LearnHub",weight=BOLD).shift(UP)
        subtitle=Text("A Learning Hub for everyone",weight=LIGHT).scale(0.5)
        box=SurroundingRectangle(title,subtitle,buff=0.75,color="#e9bab3",fill_color=BLACK,fill_opacity=0.5)
        components=[box,title,subtitle,stack_group]

        self.play(FadeIn(bg),run_time=1)
        WriteTextBox(self,components)
        self.wait(2.5)
        FadeOutComponents(self,bg,components)
        