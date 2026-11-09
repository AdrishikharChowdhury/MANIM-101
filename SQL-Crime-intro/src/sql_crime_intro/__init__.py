from manim import *
from PIL import Image, ImageFilter


def GroupImage(path, text):
    image = ImageMobject(path)
    image.height = 1.2
    label = Text(text, color=WHITE, weight=BOLD).next_to(image, DOWN).scale(0.6)
    return Group(image, label)


def GroupTextImage(path, text):
    image = SVGMobject(path)
    image.height = 1.2
    label = Text(text, color=WHITE, weight=BOLD).next_to(image, DOWN).scale(0.6)
    return Group(image, label)


class SQL_Crime_Intro(Scene):
    def construct(self):
        img_path = "./assets/background.jpg"
        raw_img = Image.open(img_path).convert("RGB")
        blurred_img = raw_img.filter(ImageFilter.GaussianBlur(radius=10))
        bg = ImageMobject(blurred_img)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)

        kaggle_group = GroupImage("./assets/kaggle.png", "Kaggle")
        tsql_group = GroupImage("./assets/tsql.png", "T-SQL")
        docker_group = GroupTextImage("./assets/docker.svg", "Docker")
        stack_group = Group(kaggle_group, tsql_group, docker_group).arrange(RIGHT, buff=1).scale(0.65)

        title = Text("Crime in India", weight=BOLD).scale(1.25)
        subtitle = Text("SQL Data Exploration & Analysis", weight=LIGHT).scale(0.5)
        footnote1 = Text("SQL Server 2022  •  Docker  •  T-SQL", weight=LIGHT).scale(0.45)
        footnote2 = Text("5 Phases  •  17 Analytical Questions", weight=LIGHT).scale(0.45).next_to(footnote1, DOWN, buff=0.1)
        footnotes = VGroup(footnote1, footnote2)
        content = VGroup(title, subtitle, footnotes).arrange(DOWN, buff=0.3).scale(0.8).shift(UP * 0.8)
        box = SurroundingRectangle(
            content,
            buff=0.5,
            color="#e9bab3",
            fill_color=BLACK,
            fill_opacity=0.5,
        )
        stack_group.next_to(box, DOWN, buff=0.5)

        self.play(FadeIn(bg), run_time=1)
        self.play(DrawBorderThenFill(box), run_time=2)
        self.play(Write(title), run_time=2)
        self.play(Write(subtitle), run_time=2)
        self.play(Write(footnotes), run_time=1)
        self.play(FadeIn(stack_group), run_time=2)
        self.wait(2.5)


def main() -> None:
    pass
