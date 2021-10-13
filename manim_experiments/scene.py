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
        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        # Only instances of VMobject implement set_stroke() and set_fill().
        # Instances of Mobject implement set_color() instead. The vast majority of
        # pre-defined classes are derived from VMobject so it is usually safe to assume
        # that you have access to the set_stroke() and set_fill()

        self.add(circle, square, triangle)
        self.wait(1)


class MobjectZOrder(Scene):

    def construct(self):

        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.add(triangle, square, circle)
        self.wait(1)


class SomeAnimations(Scene):

    def construct(self):
        square = Square()
        self.add(square)

        # some animation display mobjects, ...
        self.play(FadeIn(square))

        # ... some move or rotate mobjects around...
        self.play(Rotate(square, PI/4))

        self.wait(1)


class AnimateExample(Scene):

    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        # animate the change of color
        self.play(square.animate.set_fill(WHITE))

        # animate the change of position and the rotation at the same time
        self.play(square.animate.shift(UP).rotate(PI / 3))
        self.wait(1)

        # animate() is a property of all mobjects that animates the methods that come afterward.
        # For example, square.set_fill(WHITE) sets the fill color of the square, while square.animate.set_fill(WHITE)
        # animates this action.


class RunTime(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.play(square.animate.shift(UP), run_time=3)
        self.wait(1)


'''

Creating a custom animation.

Even though Manim has many built-in animations, you will find times when you
need to smoothly animate from one state of a Mobject to another. If you find yourself
in that situation, then you can define your own custom animation. You can start by extending
the Animation class and overriding its interpolate_mobject(). The interpolate_mobject() method receives alpha
as a parameter that starts at 0 and changes throughout the animation. So, you just have to manipulate
self.mobject inside Animation according to the alpha value in its interpolate_mobject method.

Let's say you start with a number and want to create a Transform animation that transforms
it to a target number. You can do it using FadeTransform, which will fade out the starting
number and fade in the targe number. But when we think about transforming a number from 
one to another, an intuitive way of doing it is by incrementing or decremeenting it smoothly. 
Manim has a feature that allows you to customize this behavior by definding your own custom
animation.

You can start by creating your own count class that extends Animation. The class can have
a constructor with three arguments, a DecimalNumber Mobject, start, and end. The constructor
will pass the DecimalNumber Mobject to the super constructor (in this case, the Animation constructor)
and will set start and end.

The only thing that you need to do is to define how you want it to look at every step of the animation.
Manim provides you with the alpha value in the interpolate_mobject() method based on frame rate of video,
rate function, and run time of animation played. The alpha parameter holds a value between 0 and 1
representing the step of the currently playing animation. For example, 0 means the beginning
of the animation, 0.5 means halfway, and 1 means the end of the animation.

Suppose you are starting at 50 and incrementing until the DecimalNumber reaches 100 at the
end of the animation.
  
- If alpha is 0, you want the value to be 50. 
- If alpha is 0.5, you want the value to be 75.
- If alpha is 1, you want the value to be 100.



Generally, you start with the starting number and add only some of the part of the 
value to be increment according to the alpha value. So, the logc of calculating the number
to display at each step will be - 50 + alpha * (100 - 50) Once you set the calculated value for the 
DecimalNumber, you are done.

Once you have defined your Count animation, you can play it in your Scene for any duration
you want for any DecimalNumber for any rate function.

'''


class Count(Animation):

    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation.

        super().__init__(number, **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


class CountingScene(Scene):

    def construct(self):
        # Create Decimal Number and add it to scene
        number = DecimalNumber().set_color(WHITE).scale(5)

        # Add an updater to keep the DecimalNumber centered as its value changes
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)

        self.wait()

        # Play the Count Animation to count from 0 to 100 in 4 seconds
        self.play(Count(number, 0, 100), run_time=4, rate_func=linear)

        self.wait()


'''

Using coordinates of a mobject

Mobjects contain points that define their boundaries. These points can 
be used to add the other mobjects respectively to each other, e.g. by methods
like get_center(), get_top() and get_start().
Here is an example of some important coordinates

'''


class MobjectExample(Scene):

    def construct(self):

        p1 = [-1, -1, 0]
        p2 = [1, -1, 0]
        p3 = [1, 1, 0]
        p4 = [-1, 1, 0]

        a = Line(p1, p2).append_points(
            Line(p2, p3).points).append_points(Line(p3, p4).points)
        point_start = a.get_start()
        point_end = a.get_end()
        point_center = a.get_center()
        self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}", font_size=24).to_edge(
            UR).set_color(YELLOW))
        self.add(Text(f"a.get_end() = {np.round(point_end,2).tolist()}", font_size=24).next_to(
            self.mobjects[-1], DOWN).set_color(RED))
        self.add(Text(f"a.get_center() = {np.round(point_center,2).tolist()}", font_size=24).next_to(
            self.mobjects[-1], DOWN).set_color(BLUE))

        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.points])
        self.add(a)

# Transforming mobjects into other mobjects
# It is also possible to transform a mobject into another mobject like this:
