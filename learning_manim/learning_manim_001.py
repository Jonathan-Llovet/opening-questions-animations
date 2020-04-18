from manimlib.imports import *


class Grid(VMobject):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        VMobject.__init__(self, **kwargs)

    def generate_points(self):
        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows":8,
        "columns":14,
        "height": FRAME_Y_RADIUS*2,
        "width": 14,
        "grid_stroke":0.5,
        "grid_color":WHITE,
        "axis_color":RED,
        "axis_stroke":2,
        "show_points":False,
        "point_radius":0,
        "labels_scale":0.5,
        "labels_buff":0,
        "number_decimals":2
    }

    def __init__(self,**kwargs):
        VGroup.__init__(self,**kwargs)
        rows=self.rows
        columns=self.columns
        grilla=Grid(width=self.width,height=self.height,rows=rows,columns=columns).set_stroke(self.grid_color,self.grid_stroke)

        vector_ii=ORIGIN+np.array((-self.width/2,-self.height/2,0))
        vector_id=ORIGIN+np.array((self.width/2,-self.height/2,0))
        vector_si=ORIGIN+np.array((-self.width/2,self.height/2,0))
        vector_sd=ORIGIN+np.array((self.width/2,self.height/2,0))

        ejes_x=Line(LEFT*self.width/2,RIGHT*self.width/2)
        ejes_y=Line(DOWN*self.height/2,UP*self.height/2)

        ejes=VGroup(ejes_x,ejes_y).set_stroke(self.axis_color,self.axis_stroke)

        divisiones_x=self.width/columns
        divisiones_y=self.height/rows

        direcciones_buff_x=[UP,DOWN]
        direcciones_buff_y=[RIGHT,LEFT]
        dd_buff=[direcciones_buff_x,direcciones_buff_y]
        vectores_inicio_x=[vector_ii,vector_si]
        vectores_inicio_y=[vector_si,vector_sd]
        vectores_inicio=[vectores_inicio_x,vectores_inicio_y]
        tam_buff=[0,0]
        divisiones=[divisiones_x,divisiones_y]
        orientaciones=[RIGHT,DOWN]
        puntos=VGroup()
        leyendas=VGroup()


        for tipo,division,orientacion,coordenada,vi_c,d_buff in zip([columns,rows],divisiones,orientaciones,[0,1],vectores_inicio,dd_buff):
            for i in range(1,tipo):
                for v_i,direcciones_buff in zip(vi_c,d_buff):
                    ubicacion=v_i+orientacion*division*i
                    punto=Dot(ubicacion,radius=self.point_radius)
                    coord=round(punto.get_center()[coordenada],self.number_decimals)
                    leyenda=TextMobject("%s"%coord).scale(self.labels_scale)
                    leyenda.next_to(punto,direcciones_buff,buff=self.labels_buff)
                    puntos.add(punto)
                    leyendas.add(leyenda)

        self.add(grilla,ejes,leyendas)
        if self.show_points==True:
            self.add(puntos)

class GreekText(Scene):
    def construct(self):
        greek_text = """Τῶν ὄντων τὰ μέν ἐστιν ἐφ' ἡμῖν, τὰ δὲ οὐκ ἐφ' ἡμῖν."""
        greek = Text(greek_text, font="Geneva",stroke_width=0, size=0.5)
        self.play(Write(greek, run_time=5))
        self.wait()

class GreekTexMobject(Scene):
    # Does not render properly
    def construct(self):
        greek_text = """Τῶν ὄντων τὰ μέν ἐστιν ἐφ' ἡμῖν, τὰ δὲ οὐκ ἐφ' ἡμῖν."""
        greek = TexMobject(greek_text)
        self.play(Write(greek, run_time=5))
        self.wait()
class Shape(Scene):

    def construct(self):
        grid = ScreenGrid()
        circle = Circle()
        circle_up = Circle(arc_center=UP)
        circle_down = Circle(arc_center=DOWN)
        circle_left = Circle(arc_center=LEFT)
        circle_right = Circle(arc_center=RIGHT)
        square = Square()
        bigsquare = Polygon(
            np.array([-2, 2, 0]),
            np.array([2, 2, 0]),
            np.array([2, -2, 0]),
            np.array([-2, -2, 0])
            )
        square_UR = np.array([1, 1, 0])
        square_DR = np.array([1, -1, 0])
        square_UL = np.array([-1, 1, 0])
        square_DL = np.array([-1, -1, 0])
        bigsquare_UR = np.array([2, 2, 0])
        bigsquare_DR = np.array([2, -2, 0])
        bigsquare_UL = np.array([-2, 2, 0])
        bigsquare_DL = np.array([-2, -2, 0])

        triangle_right_to_up_right = Polygon(
            bigsquare_UR,
            square_UR,
            square_DR
            )
        triangle_right_to_down_right = Polygon(
            bigsquare_DR,
            square_UR,
            square_DR
            )

        triangle_left_to_up_left = Polygon(
            bigsquare_UL,
            square_UL,
            square_DL
            )
        triangle_left_to_down_left = Polygon(
            bigsquare_DL,
            square_UL,
            square_DL
            )



        self.add(grid)
        self.play(ShowCreation(circle))
        # self.play(ShowCreation(circle_up))
        # self.play(ShowCreation(circle_down))
        # self.play(ShowCreation(circle_left))
        # self.play(ShowCreation(circle_right))
        self.play(ShowCreation(square))
        self.play(ShowCreation(bigsquare))
        circle.target = Circle(arc_center=bigsquare_UR)
        self.play(MoveToTarget(circle, run_time=2.2))
        circle.target = Circle(arc_center=bigsquare_UL)
        self.play(MoveToTarget(circle, run_time=2.2))
        circle.target = Circle(arc_center=bigsquare_DL)
        self.play(MoveToTarget(circle, run_time=2.2))
        circle.target = Circle(arc_center=bigsquare_DR)
        self.play(MoveToTarget(circle, run_time=2.2))
        circle.target = Circle(arc_center=bigsquare_UR)
        self.play(MoveToTarget(circle, run_time=2.2))
        circle.target = Circle()
        self.play(MoveToTarget(circle, run_time=2.2))
        # self.play(ShowCreation(triangle_right_to_up_right))
        # self.play(ShowCreation(triangle_right_to_down_right))
        # self.play(ShowCreation(triangle_left_to_up_left))
        # self.play(ShowCreation(triangle_left_to_down_left))
        self.wait()
        