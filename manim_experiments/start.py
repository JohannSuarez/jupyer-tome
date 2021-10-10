from manimlib import *


class SquareToCircle(Scene):

    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)

        square = Square()
        self.play(ShowCreation(square))
        self.wait()  # A Pause. Default is 1s but you can pass a parameter.

        # Morph the square into a circle
        self.play(ReplacementTransform(square, circle))
        self.wait()  # A Pause. Default is 1s but you can pass a parameter.
