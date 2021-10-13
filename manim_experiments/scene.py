from manim import *

# Tip:
# Every animation must be contained within the construct()
# method of a class that derives from Scene.
# Other code, for example auxiliary or mathematical functions,
# may reside outside the class.


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        # interpolate the square into the circle
        self.play(Transform(square, circle))
        self.play(FadeOut(square))  # fade out animation


class CreatingMobjects(Scene):
    def construct(self):

        circle = Circle()
        self.add(circle)

        # Any object that can be displayed on the screen is a mobject, even if it's
        # not necessarily mathematical in nature.
        # To display a mobject on the screen, call the add() method
        # of the containing Scene. This is the principal way of displaying a mobject on the
        # screen when it is not being animated. To remove a mobject from the screen, simply call
        # the remove() method from the containing Scene.

        self.wait(1)
        self.remove(circle)
        self.wait(1)


class Shapes(Scene):

    def construct(self):

        circle = Circle()
        square = Square()
        triangle = Triangle()

        # Unlike other graphics software, manim places the center of coordinates
        # at the center of the screen. The positive vertical direction is up,
        # and the positive horizontal direction is right. See also the constants, ORIGIN, UP, DOWN
        # LEFT, and RIGHT, and others defined in the 'constants' module.
        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)

        self.wait(1)

        # There are many other possible ways to place mobjects on the screen, for
        # example move_to(), next_to(), and align_to(). the next scene MobjectPlacement uses
        # all three.


class MobjectPlacement(Scene):

    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        # place the circle two units left from the origin
        # move_to() uses absolute units relative to origin.
        circle.move_to(LEFT * 2)

        # place the square to the left of the circle
        # next_to() uses relative units (relative to object passed as first argument)
        square.next_to(circle, LEFT)

        # align the left border of the triangle to the left border of the circle
        # align_to() uses LEFT not as measuring units but as a way to determine
        # the border to use for alignment. The coordinates of the borders of a
        # mobject are determined using an imaginary bounding box around it.
        triangle.align_to(circle, LEFT)

        # Note that these methods don't "attach" Mobjects to one another.

        self.add(circle, square, triangle)
        self.wait(1)


class MobjectStyling(Scene):

    def construct(self):

        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        # This scene uses two of the main functions that change the visual style
        # of a mobject: set_stroke() and set_fill()
        circle.set_stroke(color=GREEN), width = 20)
        square.set_fill(YELLOW, opacity = 1.0)
        triangle.set_fill(PINK, opacity = 0.5)

        # Only instances of VMobject implement set_stroke() and set_fill().
        # Instances of Mobject implement set_color() instead. The vast majority of
        # pre-defined classes are derived from VMobject so it is usually safe to assume
        # that you have access to the set_stroke() and set_fill()

        self.add(triangle, square, circle)
        self.wait(1)
