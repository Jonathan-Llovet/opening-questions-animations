from manimlib.imports import *

class BigOLogo(Scene):
    def construct(self):
        header = TextMobject("Opening Questions").move_to(DOWN*1.25)
        openingQuestions = TexMobject("O", "(", "Q", ")").scale_in_place(3)
        openingQuestions.set_color_by_tex("O", BLUE_B)
        openingQuestions.set_color_by_tex("Q", WHITE)
        openingQuestions.set_color_by_tex("(", RED_E)
        openingQuestions.set_color_by_tex(")", RED_E)
        logo = VGroup(header, openingQuestions).move_to(np.array([0, 0, 0])).scale_in_place(1.45)
        self.play(ShowCreation(logo))
        # self.play(ShowCreation(header))
        # self.play(ShowCreation(openingQuestions))
