from manimlib.imports import *

class Diagram1(Scene, GetIntersections):
    def construct(self):
        self.defineDiagram()
        self.drawDiagram()

    def drawDiagram(self):
        self.markPoint(self.pointA, self.pointA_label)
        self.play(ShowCreation(self.circleAB))

        self.markPoint(self.pointB, self.pointB_label)
        self.play(ShowCreation(self.lineAB))

        self.circleBC.flip(UP) # Draws from right side, going up
        # self.circleBC.rotate(DEGREES*180) # Draws from left side, going down
        self.play(ShowCreation(self.circleBC))
        self.wait()
        self.markPoint(self.pointC, self.pointC_label)

        self.play(ShowCreation(self.lineAC))
        self.play(ShowCreation(self.lineBC))

        self.wait()

    def defineDiagram(self):
        self.pointA = np.array([-1, 0, 0])
        self.pointA_label = TexMobject("A")
        self.pointA_label.next_to(self.pointA, LEFT)

        self.circleAB_radius = 2

        self.pointB = self.pointA.copy()
        self.pointB[0] += self.circleAB_radius # X coordinate offset
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

        self.pointC_label = TexMobject("C")
        self.pointC_label.next_to(self.pointC, UP)

        self.lineAC = Line(start=self.pointC, end=self.pointA)
        self.lineBC = Line(start=self.pointC, end=self.pointB)

    def markPoint(self, point, label):
        dot = Dot(radius=0.05, color=YELLOW, point=point)
        self.play(ShowCreation(dot), ShowCreation(label))
        self.add_foreground_mobjects(dot)
        self.add_foreground_mobjects(label)
