from manimlib.imports import *

class Shape(Scene):
    def construct(self):
        circle = Circle(arc_center=2)
        square = Square()
        triangle = Polygon(
            np.array([2, 2, 1]),
            # np.array([0, 0, 1]),
            np.array([1, 1, 0]),
            np.array([1, -1, 0])
            )
        
        self.play(DrawBorderThenFill(circle))
        self.play(DrawBorderThenFill(square))
        self.play(DrawBorderThenFill(triangle))