from manimlib.imports import *
# from communitylib.utils.imports import *


class Diagram1(Scene, GetIntersections):
    def construct(self):
        pointA = np.array([-.5, 0, 0])
        pointB = np.array([.5, 0, 0])
        circleAB = Circle(arc_center=pointA)
        circleBC = Circle(arc_center=pointB)

        lineAB = Line(start=pointA, end=pointB)
        intersections = self.get_intersections_between_two_vmobs(circleAB, circleBC)

        pointC = None
        for point in intersections:
            # This will only work in this case, where there is only one valid intersection
            print(point)
            if point[1] > 0:
                pointC = point

        lineAC = Line(start=pointC, end=pointA)
        lineBC = Line(start=pointC, end=pointB)

        self.markPoint(pointA)
        self.play(ShowCreation(circleAB))
        self.markPoint(pointB)
        self.play(ShowCreation(circleBC))
        self.play(ShowCreation(lineAB))
        self.markPoint(pointC)
        self.play(ShowCreation(lineAC))
        self.play(ShowCreation(lineBC))
        # self.play(ShowCreation(triangle))

        self.wait()

    def markPoint(self, point):
        dot = Dot(radius=0.05, color=YELLOW, point=point)
        self.play(ShowCreation(dot))
        self.add_foreground_mobjects(dot)
