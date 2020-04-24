from manimlib.imports import *

class EuclidIntro(Scene):
    def construct(self):

        euclid_greek = Text(
            "τὰ Στοιχεῖα Εὐκλείδου",
            font="Georgia",
            stroke_width=0,
            size=1
            )

        euclid_english = Text(
            "Euclid's Elements",
            font="Georgia",
            stroke_width=0,
            size=1
            )

        opening_questions_english = Text(
            "Opening Questions",
            font="Georgia",
            stroke_width=0,
            size=1
        )
        placeholder = Text(
            "placeholder",
            font="Georgia",
            stroke_width=0,
            size=1
        )

        self.play(Write(opening_questions_english))
        self.wait()
        self.play(ReplacementTransform(opening_questions_english, placeholder), run_time=2)
        self.wait()
        self.play(ReplacementTransform(placeholder, euclid_greek), run_time=2)
        self.wait()
        self.play(ReplacementTransform(euclid_greek, euclid_english), run_time=2)
        self.wait()

