from manim import *

# Tip:
# Every animation must be contained within the construct()
# method of a class that derives from Scene.
# Other code, for example auxiliary or mathematical functions,
# may reside outside the class.


class CreateTable(Scene):

    def construct(self):

        name = Text("Pack")
        #name = "string"
        attribs = VGroup(
            *[Text(f'NFT{i+1}', font_size=15).shift(DOWN*0.5*i) for i in range(5)]
        )

        operations = Text('_populate_pack', font_size=15)

        table = MobjectTable([[name], [attribs], [operations]],
                             include_outer_lines=True)  # Create square

        # self.add(table)  # animate the creation of the square
        self.play(Create(table))
        self.wait(2)
        # interpolate the square into the circle
