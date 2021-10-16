from manim import *
import random

# Stands for "Night Mode Compatible" colors
nmc = {

    'light_blue': '#269FEB',
    'dark_blue': '#2680EB',
    'light_pink_purple': '#AD3DA4',
    'dark_purple': '#4B23B0',
    'orange': '#F28544',
    'dark_orange_yellow': '#D18022',
    'red': '#F05137',
    'green': '#43AD00',
    'pine_green': '#00A365',
    'gray': '#7C7C7C',
}


class DigitalCoin(Scene):

    def construct(self):

        # Generate a random 10-character string of binary digits.
        def rand_key(p: int) -> str:
            key1 = ""
            for i in range(p):
                temp = str(random.randint(0, 1))
                key1 += temp
            return(key1)

        r_binaries = [rand_key(5) + '\n' + rand_key(5) for i in range(6)]

        outer_circle = Circle()
        outer_circle.set_stroke(color=nmc['light_blue'], width=7)

        outer_circle.set_fill(
            color=nmc['dark_blue'], opacity=1).set_sheen(-0.3, DR)

        inner_circle = Circle()

        inner_circle.set_stroke(color=nmc['light_blue'], width=3).scale(
            0.8)

        with register_font("fonts/PTM55FT.ttf"):

            # Creating a set of Text mObjects, and cycling through them in the animation.
            binary_set = [Text(r_binaries[i], font="PT Mono").scale(
                0.6) for i in range(6)]

        coin = VGroup(outer_circle, inner_circle, binary_set[0])

        self.play(FadeIn(coin))

        for i in range(5):
            self.play(Transform(binary_set[0], binary_set[i]), run_time=0.1)
            self.wait(1)

        self.wait()


# Block comments to possibly reference in the future.
'''
# You can animate methods of a VMObject using .animate

self.play(outer_circle.animate.set_fill(
    color=nmc['dark_blue'], opacity=1).set_sheen(-0.3, DR), run_time=0.5)
'''

'''
text = Text("The quick brown fox jumps over the lazy dog",
            gradient=(BLUE, GREEN)).scale(0.5).shift(UP*1.5)

'''
