from manim import *

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

        outer_circle = Circle()
        outer_circle.set_stroke(color=nmc['light_blue'], width=7)

        outer_circle.set_fill(
            color=nmc['dark_blue'], opacity=1).set_sheen(-0.3, DR)

        inner_circle = Circle()

        inner_circle.set_stroke(color=nmc['light_blue'], width=3).scale(
            0.8)

        coin = VGroup(outer_circle, inner_circle)

        self.play(FadeIn(coin))

        '''
        self.play(outer_circle.animate.set_fill(
            color=nmc['dark_blue'], opacity=1).set_sheen(-0.3, DR), run_time=0.5)
        '''
        # You can animate methods of a VMObject using .animate
        # self.play(outer_circle.animate.set_sheen(-0.3, DR), run_time=0.2)
        self.wait(1)
