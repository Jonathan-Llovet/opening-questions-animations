from manimlib.imports import *

class BigOLogo(Scene):
    def construct(self):
        opening_questions = TextMobject("Opening Questions").move_to(DOWN*1.25)
        bigO = TexMobject("O", "(", "Q", ")").scale_in_place(3)
        bigO.set_color_by_tex("O", BLUE_B)
        bigO.set_color_by_tex("Q", WHITE)
        bigO.set_color_by_tex("(", RED_E)
        bigO.set_color_by_tex(")", RED_E)
        logo = VGroup(bigO, opening_questions).move_to(np.array([0, 0, 0])).scale_in_place(1.45)
        self.play(ShowCreation(bigO), run_time=2)
        self.play(ShowCreation(opening_questions), run_time=2)
        self.wait()
        self.play(FadeOut(logo))
        self.wait()
