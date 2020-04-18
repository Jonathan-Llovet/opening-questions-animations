from manimlib.imports import *

class AristotleSample(Scene):
    def construct(self):
        text_greek = Text(
            "Πᾶσα τέχνη καὶ πᾶσα μέθοδος,",
            font="Geneva",
            stroke_width=0,
            size=0.5
            ).move_to(UP*.5)

        text_english = Text(
            "Every art and every inquiry",
            font="Geneva",
            stroke_width=0,
            size=0.5
            ).move_to(DOWN*.5)
        self.play(Write(text_greek), run_time=1.5)
        self.play(ReplacementTransform(text_greek.copy(), text_english), run_time=1.5)
        self.wait()
