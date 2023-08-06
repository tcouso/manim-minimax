from manim import *

config.media_width = "75%"
config.verbosity = "WARNING"


class PseudoCode(Scene):
    def construct(self):
        # Add pseudocode images
        # https://docs.manim.community/en/stable/reference/manim.mobject.types.image_mobject.ImageMobject.html
#         max_code = ImageMobject("../img/max.png").scale(2)
#         min_code = ImageMobject("../img/min.png").scale(2)

        max_code = ImageMobject("img/max_eval.png").scale(2)
        min_code = ImageMobject("img/min_eval.png").scale(2)
        
        
        title = Text("Pseudocódigo búsqueda minimax").scale(0.6).shift(3.6 * UP)
        
        max_square_base = Rectangle(color=BLUE, width=5.5, height = 1.0)
        max_square_rec = Rectangle(color=BLUE, width=5.5, height = 3.5)
        
        min_square_base = Rectangle(color=RED, width=5.5, height = 1.0)
        min_square_rec = Rectangle(color=RED, width=5.5, height = 3.5)
        
        img_group = Group(max_code, min_code)
        img_group.arrange()
        self.add(img_group, title)
        
        # Animations
        max_square_base.shift(4 * LEFT + 2 * UP)
        max_square_rec.shift(4 * LEFT + 1.2 * DOWN)
        
        min_square_base.shift(3.5 * RIGHT + 2 * UP)
        min_square_rec.shift(3.5 * RIGHT + 1.2 * DOWN)
        
        self.wait()
        self.play(FadeIn(max_square_base))
        self.wait()
        self.play(FadeOut(max_square_base))
        
        self.play(FadeIn(min_square_base))
        self.wait()
        self.play(FadeOut(min_square_base))
        
        self.play(FadeIn(max_square_rec))
        self.wait()
        self.play(FadeOut(max_square_rec))
        
        self.play(FadeIn(min_square_rec))
        self.wait()
        self.play(FadeOut(min_square_rec))
        