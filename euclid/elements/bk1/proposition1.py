from manimlib.imports import *

class Diagram1(Scene, GetIntersections):
    def construct(self):
        self.defineDiagram()
        self.defineEquilateralTriangle()
        self.drawDiagram()

    def drawDiagram(self):

        self.play(ShowCreation(self.triangleABC, run_time=3))
        self.wait()
        self.play(Uncreate(self.triangleABC))

        self.markPoint(self.dotA, self.pointA_label)
        self.play(ShowCreation(self.circleAB))

        self.markPoint(self.dotB, self.pointB_label)
        self.play(ShowCreation(self.lineAB))

        self.play(ShowCreation(self.circleBC))
        self.wait()
        self.markPoint(self.dotC, self.pointC_label)

        self.play(ShowCreation(self.lineAC))
        self.play(ShowCreation(self.lineBC))

        self.wait()

    def defineEquilateralTriangle(self):
        self.triangleABC = VGroup(
            # self.pointA,
            self.dotA.copy(),
            self.pointA_label.copy(),
            # self.pointB,
            self.dotB.copy(),
            self.pointB_label.copy(),
            self.lineAB.copy(),
            # self.pointC,
            self.dotC.copy(),
            self.pointC_label.copy(),
            self.lineAC.copy(),
            self.lineBC.copy()
        )

    def defineDiagram(self):
        self.pointA = np.array([-1, 0, 0])
        self.dotA = self.createDotForPoint(self.pointA)
        self.pointA_label = TexMobject("A")
        self.pointA_label.next_to(self.pointA, LEFT)

        self.circleAB_radius = 2

        self.pointB = self.pointA.copy()
        self.pointB[0] += self.circleAB_radius # X coordinate offset
        self.dotB = self.createDotForPoint(self.pointB)
        self.pointB_label = TexMobject("B")
        self.pointB_label.next_to(self.pointB, RIGHT)

        self.circleAB = Circle(
            arc_center=self.pointA,
            radius=self.circleAB_radius
            )
        self.circleBC = Circle(
            arc_center=self.pointB,
            radius=self.circleAB_radius
            )
        self.circleBC.flip(UP) # Draws from right side, going up
        # self.circleBC.rotate(DEGREES*180) # Draws from left side, going down

        self.lineAB = Line(start=self.pointA, end=self.pointB)

        self.intersections = self.get_intersections_between_two_vmobs(
            self.circleAB,
            self.circleBC
            )

        self.pointC = None
        for point in self.intersections:
            # This will only work in this case, where there is only one valid intersection
            # print(point)
            if point[1] > 0: # checks y coordinate
                self.pointC = point
        self.dotC = self.createDotForPoint(self.pointC)
        self.pointC_label = TexMobject("C")
        self.pointC_label.next_to(self.pointC, UP)

        self.lineAC = Line(start=self.pointC, end=self.pointA)
        self.lineBC = Line(start=self.pointC, end=self.pointB)


    def createDotForPoint(self, point):
        return Dot(radius=0.05, color=YELLOW, point=point)

    def setDotAndLabelInForeground(self, dot, label):
        self.add_foreground_mobjects(dot)
        self.add_foreground_mobjects(label)

    def markPoint(self, dot, label):
        self.play(ShowCreation(dot), ShowCreation(label))
        self.setDotAndLabelInForeground(dot, label)
