from manimlib.imports import *

class EuclidIntro(Scene):

    def openingQuestionsLogo(self):
        opening_questions = TextMobject("Opening Questions").move_to(DOWN*1.25)
        bigO = TexMobject("O", "(", "Q", ")").scale_in_place(3)
        bigO.set_color_by_tex("O", BLUE_B)
        bigO.set_color_by_tex("Q", WHITE)
        bigO.set_color_by_tex("(", RED_E)
        bigO.set_color_by_tex(")", RED_E)
        logo = VGroup(bigO, opening_questions).move_to(np.array([0, 0, 0])).scale_in_place(1.45)
        self.opening_questions = opening_questions
        self.bigO = bigO
        self.logo = logo
        self.play(ShowCreation(bigO), run_time=2)
        self.play(ShowCreation(opening_questions), run_time=2)
        self.wait()


    def construct(self):
        elements_grc = Text(
            "Στοιχεῖα Εὐκλείδου",
            font="Georgia",
            stroke_width=0,
            size=1
            )
        
        elements_eng = Text(
            "Euclid's Elements",
            font="Georgia",
            stroke_width=0,
            size=1
            )

        self.openingQuestionsLogo()
        self.play(ReplacementTransform(self.logo, elements_grc), run_time=2)
        self.wait()
        self.play(ReplacementTransform(elements_grc, elements_eng), run_time=2)
        self.wait()
        self.play(FadeOut(elements_eng))
