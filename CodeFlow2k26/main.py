import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

from manim import (
    Scene,
    FadeOut,
    FadeIn,
    SVGMobject,
    WHITE,
    BLACK,
    BOLD,
    LIGHT,
    Text,
    VGroup,
    DOWN,
    RIGHT,
    SurroundingRectangle,
    DrawBorderThenFill,
    Write,
    ImageMobject,
    config,
    UP,
    ORIGIN
)
from PIL import Image, ImageFilter
import numpy as np

def GroupTextImage(path, text):
    image = SVGMobject(path)
    # INCREASED: Scale individual SVGs up for a larger presence
    image.scale_to_fit_height(0.9)
    
    if text == "Groq":
        image.set_color(WHITE)
        
    # Scaled the text up slightly to match the larger logos
    text_mobject = Text(text, color=WHITE, weight=BOLD).scale(0.42)
    text_mobject.next_to(image, DOWN, buff=0.18)
    
    return VGroup(image, text_mobject)

def WriteTextBox(self, components):
    for component in components:
        if isinstance(component, SurroundingRectangle):
            self.play(DrawBorderThenFill(component), run_time=1.5) 
        else:
            self.play(Write(component), run_time=1)

class CodeFlowIntro(Scene):
    def construct(self):
        img_path = "./assets/background.png"
        
        # Tech Asset Paths
        next_path = "./assets/nextjs-light.svg"
        ts_path = "./assets/typescript.svg"
        clerk_path = "./assets/symbol-primary.svg"
        tailwind_path = "./assets/tailwind-svgrepo-com.svg"
        mui_path = "./assets/Material UI.svg"
        shadcn_path = "./assets/Shadcnui--Streamline-Simple-Icons.svg"
        supabase_path = "./assets/supabase.svg"
        groq_path = "./assets/groq.svg"
        fastapi_path = "./assets/FastAPI.svg"
        python_path = "./assets/Python.svg"
        pandas_path = "./assets/Pandas.svg"
        numpy_path = "./assets/NumPy.svg"
        sklearn_path = "./assets/scikit-learn.svg"
        matplotlib_path = "./assets/Matplotlib.svg"
        posthog_path = "./assets/Posthog--Streamline-Svg-Logos.svg"

        # Background Processing
        raw_img = Image.open(img_path)
        blurred_img = raw_img.filter(ImageFilter.GaussianBlur(radius=10))
        bg = ImageMobject(np.array(blurred_img))
        bg.scale_to_fit_width(config.frame_width)
        
        # --- Stage 1: Title Card ---
        title = Text("Financialo", weight=BOLD).scale(1.2).move_to(UP * 0.4)
        subtitle = Text("An AI Bank Statement Summarizer", weight=LIGHT).next_to(title, DOWN, buff=0.25).scale(0.55)
        box = SurroundingRectangle(
            VGroup(title, subtitle), buff=0.5, color="#e9bab3", fill_color=BLACK, fill_opacity=0.5
        )
        intro_components = [box, title, subtitle]

        # --- Stage 2: Large Uniform Grid Layout ---
        tech_items = [
            GroupTextImage(next_path, "Next JS"),
            GroupTextImage(ts_path, "TypeScript"),
            GroupTextImage(clerk_path, "Clerk"),
            GroupTextImage(tailwind_path, "Tailwind"),
            GroupTextImage(mui_path, "Material UI"),
            GroupTextImage(shadcn_path, "Shadcn UI"),
            GroupTextImage(supabase_path, "Supabase"),
            GroupTextImage(groq_path, "Groq"),
            GroupTextImage(fastapi_path, "FastAPI"),
            GroupTextImage(python_path, "Python"),
            GroupTextImage(pandas_path, "Pandas"),
            GroupTextImage(numpy_path, "NumPy"),
            GroupTextImage(sklearn_path, "Scikit-learn"),
            GroupTextImage(matplotlib_path, "Matplotlib"),
            GroupTextImage(posthog_path, "Posthog")
        ]
        
        # INCREASED: Adjusted row/column spacing and boosted grid scale factor from 0.55 to 0.85
        grid_layout = VGroup(*tech_items).arrange_in_grid(rows=3, cols=5, buff=(0.8, 0.6)).scale(0.85)
        grid_layout.move_to(ORIGIN) 
        
        # INCREASED: Expanded the outer bounding box padding (buff=0.7) to surround the huge layout smoothly
        big_box = SurroundingRectangle(
            grid_layout, buff=0.7, color="#e9bab3", fill_color=BLACK, fill_opacity=0.3
        )
        
        tech_components = [big_box, grid_layout]

        # --- PLAY TIMELINE ---
        
        # 1. Title Sequence Intro
        self.play(FadeIn(bg), run_time=1)
        WriteTextBox(self, intro_components)
        self.wait(2.0)
        
        # 2. Fade Title Out
        self.play(*[FadeOut(component) for component in intro_components], run_time=1)
        self.wait(0.3)
        
        # 3. Write Enlarged Row-by-Row Tech Grid
        WriteTextBox(self, tech_components)
        self.wait(3.5)
        
        # 4. Global Outro Cleanup
        self.play(FadeOut(bg), *[FadeOut(comp) for comp in tech_components], run_time=1)