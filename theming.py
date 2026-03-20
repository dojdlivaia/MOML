import manim as m
from manim_themes.manim_theme import apply_theme

def apply_colors():
    m.Text.set_default(
        font="Courier New",
        color=m.BLACK
    )
    m.Tex.set_default(color=m.BLACK)
    m.MathTex.set_default(color=m.BLACK)

    # Mobjects
    m.Mobject.set_default(color=m.BLACK)
    m.VMobject.set_default(color=m.BLACK)
    m.Vector.set_default(color=m.BLACK)

class Scene_(m.Scene):
    def setup(self):
        theme = "Apple System Colors Light"
        apply_theme(manim_scene=self, theme_name=theme)
        apply_colors()

class ThreeDScene_(m.ThreeDScene):
    def setup(self):
        theme = "Apple System Colors Light"
        apply_theme(manim_scene=self, theme_name=theme)
        apply_colors()

class LinearTransformationScene_(m.LinearTransformationScene):
    def setup(self):
        theme = "Apple System Colors Light"
        apply_theme(manim_scene=self, theme_name=theme)
        apply_colors()