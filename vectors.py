import manim as m
import numpy as np
from theming import LinearTransformationScene_, Scene_, ThreeDScene_, apply_colors
from manim_themes.manim_theme import apply_theme

class VectorsExample(Scene_):
    """
    Демонстрирует понятие вектора как направления. 
    Анимирует несколько векторов на плоскости.
    """
    def construct(self):
        plane = m.NumberPlane()
        self.play(m.Create(plane))

        x = m.ValueTracker(1)
        y = m.ValueTracker(2)

        vector = m.Vector([1,2])
        vector.add_updater(lambda vec: vec.become(m.Vector([
            int(x.get_value() * 100) / 100, 
            int(y.get_value() * 100) / 100
            ])))
        self.play(m.Create(vector))

        label = vector.coordinate_label()
        label.add_updater(lambda vec: vec.become(vector.coordinate_label()))
        self.play(m.Write(label))

        self.play(x.animate.set_value(3), y.animate.set_value(-2))
        self.wait(0.5)

        self.play(x.animate.set_value(-4), y.animate.set_value(1))
        self.wait(0.5)

        label.become(vector.coordinate_label(integer_labels=False))
        label.add_updater(
            lambda vec: vec.become(vector.coordinate_label(integer_labels=False))
            )
        self.wait(0.5)

        self.play(x.animate.set_value(-2.73), y.animate.set_value(-0.376))
        # label.become(vector.coordinate_label(integer_labels=False))
        self.wait(0.5)

        self.play(x.animate.set_value(-3), y.animate.set_value(0))
        # label.become(vector.coordinate_label(integer_labels=False))
        self.wait(0.5)

        self.wait()

class VectorShift(Scene_):
    """
    Демонстриурет параллельный перенос вектора и что это остается тем же самым вектором.
    """
    def construct(self):
        plane = m.NumberPlane()
        self.play(m.Create(plane), run_time=0.3)

        vector = m.Vector([1,2])
        label = vector.coordinate_label()

        group = m.VGroup(vector, label)

        self.play(m.Create(group))

        self.play(group.animate.move_to(m.LEFT))
        self.wait(0.5)

        self.play(group.animate.move_to(m.UP))
        self.wait(0.5)

        self.play(group.animate.move_to(m.RIGHT * 2))
        self.wait(0.5)

        self.wait()


class VectorsAsDots(Scene_):
    """
    Показывает два представления вектора - как стрелок и как точки.
    На координатной плоскости появляются несколько векторов, изображенных как стрелки,
    затем они преобразуются в точки, сохраняя подписи с координатами.
    """
    def construct(self):
        plane = m.NumberPlane()
        self.play(m.Create(plane), run_time=0.3)

        vecs = [
            [-1, 2],
            [3, 2],
            [2, 3],
            [1, 3],
            [4, 2],
            [-3, 1],
            [-5, 0],
            [-5, 3],
            [1, 1],
            [3, -1],
            [5, -2],
        ]
        vectors = []
        labels = []

        for vec in vecs:
            vector = m.Vector(vec)
            self.play(m.Create(vector), run_time=0.3)
            label = vector.coordinate_label()
            self.play(m.Create(label), run_time=0.1)
            vectors.append(vector)
            labels.append(label)
            
        self.wait()

        for i in range(len(vectors)):
            vectors[i].become(m.Dot(point=[vecs[i][0], vecs[i][1], 0]))
            
        self.wait()


class _VectorsAsLine(Scene_):
    def construct(self):
        plane = m.NumberPlane()
        self.play(m.Create(plane), run_time=0.3)

        vectors = []

        vecs = list(zip(np.linspace(-7, 7, 30), np.linspace(-7, 7, 30) * 0.3 + 1))
        # print(vecs)

        for vec in vecs:
            vector = m.Vector(vec)
            self.play(m.Create(vector), run_time=0.1)
            vectors.append(vector)
            
        self.wait()
        dots = []

        for i in range(len(vectors)):
            dot = m.Dot(point=[vecs[i][0], vecs[i][1], 0])
            vectors[i].become(dot)
            dots.append(dot)
            
        self.wait()

        line = m.Line([-7, -7 * 0.3 + 1, 0], [7, 7 * 0.3 + 1, 0])
        self.play(m.Write(line))
            
        self.wait(2)

class VectorsNDim(ThreeDScene_):
    """
    Демонстрирует вектора в пространствах разной размерности.
    Показывает вектор на координатной прямой, затем он преобразуется в двумерный и затем - 
    в трехмерный вектор.
    """
    def construct(self):
        plane = m.NumberLine()
        self.play(m.Create(plane), run_time=0.3)

        x = m.ValueTracker(3)
        y = m.ValueTracker(0)
        z = m.ValueTracker(0)

        vector = m.Vector([3,0])
        vector.add_updater(lambda vec: vec.become(m.Vector([
            x.get_value(),
            y.get_value(),
            z.get_value()
            ])))
        self.play(m.Create(vector))

        label = vector.coordinate_label(n_dim=1)
        label.add_updater(lambda vec: vec.become(vector.coordinate_label(n_dim=1)))
        self.play(m.Write(label))

        self.play(x.animate.set_value(-1), y.animate.set_value(0))
        self.wait(0.5)

        self.play(x.animate.set_value(-4), y.animate.set_value(0))
        self.wait(0.5)

        self.play(x.animate.set_value(2), y.animate.set_value(0))
        self.wait(0.5)

        label.become(vector.coordinate_label(n_dim=2))
        label.add_updater(lambda vec: vec.become(vector.coordinate_label(n_dim=2)))
        self.wait(0.5)

        plane.become(m.NumberPlane())
        self.wait(0.5)

        self.play(x.animate.set_value(2), y.animate.set_value(-3))
        self.wait(0.5)

        self.play(x.animate.set_value(-1), y.animate.set_value(1))
        self.wait(0.5)

        plane.become(m.ThreeDAxes())
        self.wait(0.5)

        label.become(vector.coordinate_label(n_dim=3))
        label.add_updater(lambda vec: vec.become(vector.coordinate_label(n_dim=3)))
        self.wait(0.5)

        self.move_camera(phi=60 * m.DEGREES, theta=-15 * m.DEGREES, zoom=1, run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(0.5)

        self.play(x.animate.set_value(3), y.animate.set_value(0), z.animate.set_value(3))
        self.wait(0.5)

        self.play(x.animate.set_value(-2), y.animate.set_value(-2), z.animate.set_value(3))
        self.wait(0.5)

        self.play(x.animate.set_value(1), y.animate.set_value(3), z.animate.set_value(-2))
        self.wait(0.5)

        self.play(x.animate.set_value(1), y.animate.set_value(-1), z.animate.set_value(-1))
        self.wait(0.5)

        self.wait(2)

class _Vectorsd(ThreeDScene_):
    def construct(self):
        plane = m.NumberLine()
        self.play(m.Create(plane), run_time=0.3)

        x = m.ValueTracker(3)
        y = m.ValueTracker(0)
        z = m.ValueTracker(0)

        vector = m.Vector([3,0])
        vector.add_updater(lambda vec: vec.become(m.Vector([
            x.get_value(),
            y.get_value(),
            z.get_value()
            ])))
        self.play(m.Create(vector))

        label = vector.coordinate_label(n_dim=1)
        label.add_updater(lambda vec: vec.become(vector.coordinate_label(n_dim=1)))
        self.play(m.Write(label))

        plane.become(m.ThreeDAxes())
        self.wait(0.5)

        label.become(vector.coordinate_label(n_dim=3))
        label.add_updater(lambda vec: vec.become(vector.coordinate_label(n_dim=3)))
        self.wait(0.5)

        self.move_camera(phi=60 * m.DEGREES, theta=-15 * m.DEGREES, zoom=1, run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(0.5)

        self.play(x.animate.set_value(3), y.animate.set_value(0), z.animate.set_value(3))
        self.wait(0.5)

        self.play(x.animate.set_value(-2), y.animate.set_value(-2), z.animate.set_value(3))
        self.wait(0.5)

        self.play(x.animate.set_value(1), y.animate.set_value(3), z.animate.set_value(-2))
        self.wait(0.5)

        self.wait(2)


class VectorScaling(Scene_):
    """
    Иллюстрирует операцию умножения вектора на скаляр.
    Показывает вектор, выводит значение скаляра и демонстриурет анимацию изменения вектора
    при изменении скаляра, на который он умножается.
    """
    def construct(self):
        plane = m.NumberPlane()
        self.play(m.Create(plane))

        x = m.ValueTracker(2)
        y = m.ValueTracker(1)
        s = m.ValueTracker(2)

        vector = m.always_redraw(lambda: m.Vector([
            int(x.get_value() * 100) / 100, 
            int(y.get_value() * 100) / 100
            ]))
        self.play(m.Create(vector))

        label = m.always_redraw(lambda: vector.coordinate_label(integer_labels=False))
        self.play(m.Write(label))

        text = m.always_redraw(lambda: m.Text(
            "Скаляр: {:.2f}".format(s.get_value())
            ).shift(m.UP * 3.5))
        self.play(m.Write(text))

        scaled = m.always_redraw(lambda: m.Vector([
            int(x.get_value() * s.get_value() * 100) / 100, 
            int(y.get_value() * s.get_value() * 100) / 100
            ], color=m.YELLOW))
        self.play(m.Create(scaled))

        label = m.always_redraw(
            lambda: scaled.coordinate_label(integer_labels=False, color=m.YELLOW)
            )
        self.play(m.Write(label))

        self.wait()

        self.play(s.animate.set_value(1.5))
        self.wait(0.5)

        self.play(s.animate.set_value(0.7))
        self.wait(0.5)

        self.play(s.animate.set_value(0.1))
        self.wait(0.5)

        self.play(s.animate.set_value(-1))
        self.wait(0.5)

        self.play(s.animate.set_value(-2))
        self.wait(0.5)

        self.play(x.animate.set_value(1), x.animate.set_value(-1))
        self.wait(0.5)

        self.wait(2)


class VectorSumTriangle(Scene_):
    """
    Иллюстрирует операцию сложения векторов.
    Показывает два произвольных вектора и строит их сумму по правилу треугольника.
    """
    def construct(self):
        plane = m.NumberPlane()
        self.play(m.Create(plane), run_time=0.2)

        v1 = m.Vector([2, 3])
        l1 = v1.coordinate_label(integer_labels=False)
        g1= m.VGroup(v1, l1)
        self.play(m.Create(g1))

        v2 = m.Vector([1, -1], color=m.YELLOW)
        l2 = v2.coordinate_label(integer_labels=False, color=m.YELLOW)
        g2= m.VGroup(v2, l2)
        self.play(m.Create(g2))

        self.play(v2.animate.shift(v1.get_end()))
        self.wait(0.5)

        self.remove(l2)
        self.wait(0.5)

        v3 = m.Vector([3, 2], color=m.PINK)
        l3 = v3.coordinate_label(integer_labels=False, color=m.PINK)
        g3= m.VGroup(v3, l3)
        self.play(m.Create(g3))

        self.wait(2)


class VectorSumParallelogram(Scene_):
    """
    Иллюстрирует операцию сложения векторов.
    Строит два вектора на координатной плоскости и строит их сумму по правилу 
    параллелограмма.
    """
    def construct(self):
        plane = m.NumberPlane()
        self.play(m.Create(plane), run_time=0.2)

        v1 = m.Vector([2, 3])
        l1 = v1.coordinate_label(integer_labels=False)
        g1= m.VGroup(v1, l1)
        self.play(m.Create(g1))

        v2 = m.Vector([1, -1], color=m.YELLOW)
        l2 = v2.coordinate_label(integer_labels=False, color=m.YELLOW)
        g2= m.VGroup(v2, l2)
        self.play(m.Create(g2))

        v21 = m.Vector([1, -1], color=m.YELLOW)
        self.play(v21.animate.shift(v1.get_end()))
        self.wait(0.5)

        v12 = m.Vector([2, 3])
        self.play(v12.animate.shift(v2.get_end()))
        self.wait(0.5)

        self.remove(l2)
        self.wait(0.5)

        v3 = m.Vector([3, 2], color=m.PINK)
        l3 = v3.coordinate_label(integer_labels=False, color=m.PINK)
        g3= m.VGroup(v3, l3)
        self.play(m.Create(g3))

        self.wait(2)


class VectorSumScaling(Scene_):
    """
    Иллюстрирует дистрибутивное свойство операции сложения векторов.
    Строит сумму двух векторов и умножает ее на скаляр. Видно, что масштабируются 
    и слагаемые и сумма.
    """
    def construct(self):
        plane = m.NumberPlane()
        self.play(m.Create(plane), run_time=0.3)

        s = m.ValueTracker(1)

        v1 = m.always_redraw(lambda: m.Vector([
            int(s.get_value() * 2 * 100) / 100, 
            int(s.get_value() * 3 * 100) / 100
            ]))
        self.play(m.Create(v1))

        v2 = m.always_redraw(lambda: m.Vector([
            int(s.get_value() * 1 * 100) / 100, 
            int(s.get_value() * (-1) * 100) / 100
            ], color=m.YELLOW))
        self.play(m.Create(v2))

        text = m.always_redraw(lambda: m.Text("Скаляр: {:.2f}".format(s.get_value())).shift(m.UP * 3.5))
        self.play(m.Write(text))

        # v21 = m.Vector([1, -1], color=m.YELLOW)
        # self.play(v21.animate.shift(v1.get_end()), run_time=0.3)
        # self.wait(0.5)

        # v12 = m.Vector([2, 3])
        # self.play(v12.animate.shift(v2.get_end()), run_time=0.3)
        # self.wait(0.5)

        v3 = m.always_redraw(lambda: m.Vector([
            int(s.get_value() * 3 * 100) / 100, 
            int(s.get_value() * 2 * 100) / 100
            ], color=m.PINK))
        self.play(m.Create(v3))

        self.wait()

        self.play(s.animate.set_value(1.5))
        self.wait(0.5)

        self.play(s.animate.set_value(0.7))
        self.wait(0.5)

        self.play(s.animate.set_value(0.1))
        self.wait(0.5)

        self.play(s.animate.set_value(-1))
        self.wait(0.5)

        self.play(s.animate.set_value(-2))
        self.wait(0.5)

        self.play(s.animate.set_value(-0.75))
        self.wait(0.5)

        self.wait(2)


class VectorLinearCombine(Scene_):
    def construct(self):
        plane = m.NumberPlane()
        self.play(m.Create(plane), run_time=0.3)

        a = m.ValueTracker(1)
        b = m.ValueTracker(1)

        x1, x2 = 0.8, 0.5
        y1, y2 = 1, 1.6

        v1 = m.always_redraw(lambda: m.Vector([
            int(a.get_value() * x1 * 100) / 100, 
            int(a.get_value() * x2 * 100) / 100
            ]))
        self.play(m.Create(v1), run_time=0.3)

        v2 = m.always_redraw(lambda: m.Vector([
            int(b.get_value() * y1 * 100) / 100, 
            int(b.get_value() * y2 * 100) / 100
            ], color=m.YELLOW))
        self.play(m.Create(v2), run_time=0.3)

        text = m.always_redraw(lambda: 
                m.Text("A = {:.2f}; B = {:.2f}".format(a.get_value(), b.get_value())).shift(m.UP * 3.5))
        self.play(m.Write(text), run_time=0.3)

        # v21 = m.Vector([1, -1], color=m.YELLOW)
        # self.play(v21.animate.shift(v1.get_end()), run_time=0.3)
        # self.wait(0.5)

        # v12 = m.Vector([2, 3])
        # self.play(v12.animate.shift(v2.get_end()), run_time=0.3)
        # self.wait(0.5)

        v3 = m.always_redraw(lambda: m.Vector([
            int((a.get_value() * x1 + b.get_value() * y1) * 100) / 100, 
            int((a.get_value() * x2 + b.get_value() * y2) * 100) / 100
            ], color=m.PINK))
        self.play(m.Create(v3), run_time=0.3)

        self.wait()

        self.play(b.animate.set_value(1.5))
        self.wait(0.5)

        self.play(b.animate.set_value(-0.7))
        self.wait(0.5)

        self.play(b.animate.set_value(-3))
        self.wait(0.5)

        self.play(b.animate.set_value(0))
        self.wait(0.5)

        self.play(a.animate.set_value(-1.5), b.animate.set_value(-1.5))
        self.wait(0.5)

        self.play(a.animate.set_value(-3), b.animate.set_value(2))
        self.wait(0.5)

        self.play(a.animate.set_value(-6), b.animate.set_value(3))
        self.wait(0.5)

        self.play(a.animate.set_value(10), b.animate.set_value(-4))
        self.wait(0.5)

        self.play(a.animate.set_value(-4), b.animate.set_value(2))
        self.wait(0.5)

        self.wait(2)


class VectorSumThree(Scene_):
    """
    Демонстрирует понятие линейной зависимости трех векторов на плоскости.
    Строит три вектора на плоскости и показывает, как каждый может быть получен
    линейной комбинацией двух других.
    """
    def construct(self):
        plane = m.NumberPlane()
        self.play(m.Create(plane), run_time=0.2)

        v1 = m.Vector([2, 3])
        l1 = v1.coordinate_label(integer_labels=False)
        g1= m.VGroup(v1, l1)
        self.play(m.Create(g1))

        v2 = m.Vector([1, -1], color=m.YELLOW)
        l2 = v2.coordinate_label(integer_labels=False, color=m.YELLOW)
        g2= m.VGroup(v2, l2)
        self.play(m.Create(g2))

        v3 = m.Vector([3, 2], color=m.PINK)
        l3 = v3.coordinate_label(integer_labels=False, color=m.PINK)
        g3= m.VGroup(v3, l3)
        self.play(m.Create(g3))

        self.wait(1)

        self.remove(l2, l1, l3)
        self.wait(0.5)

        self.play(v2.animate.shift(v1.get_end()))
        text = m.Tex(r"$\vec{v_3} = \vec{v_1} + \vec{v_2}$").shift(m.UP * 3.5)
        self.play(m.Write(text), run_time=0.3)
        self.wait(1)
        self.play(m.Unwrite(text), run_time=0.3)

        self.play(v2.animate.become(m.Vector([1, -1], color=m.YELLOW)))
        self.wait(0.5)

        self.play(v2.animate.become(m.Vector([-1, 1], color=m.YELLOW)))
        self.wait(0.5)

        self.play(v2.animate.shift(v3.get_end()))
        text = m.Tex(r"$\vec{v_2} = \vec{v_3} + (-1) \vec{v_2}$").shift(m.UP * 3.5)
        self.play(m.Write(text), run_time=0.3)
        self.wait(1)
        self.play(m.Unwrite(text), run_time=0.3)

        self.play(v2.animate.become(m.Vector([1, -1], color=m.YELLOW)))
        self.wait(0.5)

        self.play(v1.animate.become(m.Vector([-2, -3])))
        self.wait(0.5)

        self.play(v1.animate.shift(v3.get_end()))
        text = m.Tex(r"$\vec{v_2} = \vec{v_3} + (-1) \vec{v_1}$").shift(m.UP * 3.5)
        self.play(m.Write(text), run_time=0.3)
        self.wait(1)
        self.play(m.Unwrite(text), run_time=0.3)

        self.play(v1.animate.become(m.Vector([2, 3])))
        self.wait(0.5)

        self.wait(2)


class VectorBasis(Scene_):
    """
    Иллюстрирует понятие базиса векторного пространства.
    Строит вектор и показывает, как он независимо от всего положения может быть 
    разложен на компоненты базиса.
    """
    def construct(self):
        plane = m.NumberPlane()
        self.play(m.Create(plane), run_time=0.3)

        a = m.ValueTracker(1)
        b = m.ValueTracker(1)

        x1, x2 = 1, 0
        y1, y2 = 0, 1

        v1 = m.always_redraw(lambda: m.Vector([
            int(a.get_value() * x1 * 100) / 100, 
            int(a.get_value() * x2 * 100) / 100
            ]))
        self.play(m.Create(v1), run_time=0.3)

        v2 = m.always_redraw(lambda: m.Vector([
            int(b.get_value() * y1 * 100) / 100, 
            int(b.get_value() * y2 * 100) / 100
            ], color=m.YELLOW))
        self.play(m.Create(v2), run_time=0.3)

        text = m.always_redraw(lambda: 
                m.Text("A = {:.2f}; B = {:.2f}".format(a.get_value(), b.get_value())).shift(m.UP * 3.5))
        self.play(m.Write(text), run_time=0.3)

        v3 = m.always_redraw(lambda: m.Vector([
            int((a.get_value() * x1 + b.get_value() * y1) * 100) / 100, 
            int((a.get_value() * x2 + b.get_value() * y2) * 100) / 100
            ], color=m.PINK))
        self.play(m.Create(v3), run_time=0.3)

        self.wait()

        self.play(b.animate.set_value(1.5))
        self.wait(0.5)

        self.play(b.animate.set_value(-0.7))
        self.wait(0.5)

        self.play(b.animate.set_value(-3))
        self.wait(0.5)

        self.play(b.animate.set_value(0))
        self.wait(0.5)

        self.play(a.animate.set_value(-1.5), b.animate.set_value(-1.5))
        self.wait(0.5)

        self.play(a.animate.set_value(-3), b.animate.set_value(2))
        self.wait(0.5)

        self.play(a.animate.set_value(-5), b.animate.set_value(3))
        self.wait(0.5)

        self.play(a.animate.set_value(5), b.animate.set_value(-3))
        self.wait(0.5)

        self.play(a.animate.set_value(-4), b.animate.set_value(2))
        self.wait(0.5)

        self.wait(2)


class VectorLinearCombineCollinear(Scene_):
    """
    Демонстрирует концепцию линейной оболочки системы векторов.
    Строит два коллинейарных вектора и их линейную комбинацию. Варьирует коэффициенты
    и показывает, какие вектора могут получиться.
    """
    def construct(self):
        plane = m.NumberPlane()
        self.play(m.Create(plane), run_time=0.3)

        a = m.ValueTracker(1)
        b = m.ValueTracker(1)

        x1, x2 = 0.8, 0.5
        y1, y2 = 1.6, 1

        v1 = m.always_redraw(lambda: m.Vector([
            int(a.get_value() * x1 * 100) / 100, 
            int(a.get_value() * x2 * 100) / 100
            ]))
        self.play(m.Create(v1), run_time=0.3)

        v2 = m.always_redraw(lambda: m.Vector([
            int(b.get_value() * y1 * 100) / 100, 
            int(b.get_value() * y2 * 100) / 100
            ], color=m.YELLOW))
        self.play(m.Create(v2), run_time=0.3)

        text = m.always_redraw(lambda: 
                m.Text("A = {:.2f}; B = {:.2f}".format(a.get_value(), b.get_value())).shift(m.UP * 3.5))
        self.play(m.Write(text), run_time=0.3)

        v3 = m.always_redraw(lambda: m.Vector([
            int((a.get_value() * x1 + b.get_value() * y1) * 100) / 100, 
            int((a.get_value() * x2 + b.get_value() * y2) * 100) / 100
            ], color=m.PINK))
        self.play(m.Create(v3), run_time=0.3)

        self.wait()

        self.play(b.animate.set_value(1.5))
        self.wait(0.5)

        self.play(b.animate.set_value(-0.7))
        self.wait(0.5)

        self.play(b.animate.set_value(-3))
        self.wait(0.5)

        self.play(b.animate.set_value(0))
        self.wait(0.5)

        self.play(a.animate.set_value(-1.5), b.animate.set_value(-1.5))
        self.wait(0.5)

        self.play(a.animate.set_value(-3), b.animate.set_value(2))
        self.wait(0.5)

        self.play(a.animate.set_value(10), b.animate.set_value(-4))
        self.wait(0.5)

        self.play(a.animate.set_value(-1), b.animate.set_value(2))
        self.wait(0.5)

        self.wait(2)


class _VectorLinearCombineNull(Scene_):
    def construct(self):
        plane = m.NumberPlane()
        self.play(m.Create(plane), run_time=0.3)

        a = m.ValueTracker(1)
        b = m.ValueTracker(1)

        x1, x2 = 0, 0
        y1, y2 = 0, 0

        v1 = m.Dot()
        self.play(m.Create(v1), run_time=0.3)

        v2 = m.always_redraw(lambda: m.Vector([
            int(b.get_value() * y1 * 100) / 100, 
            int(b.get_value() * y2 * 100) / 100
            ], color=m.YELLOW))
        self.play(m.Create(v2), run_time=0.3)

        text = m.always_redraw(lambda: 
                m.Text("A = {:.2f}; B = {:.2f}".format(a.get_value(), b.get_value())).shift(m.UP * 3.5))
        self.play(m.Write(text), run_time=0.3)

        v3 = m.always_redraw(lambda: m.Vector([
            int((a.get_value() * x1 + b.get_value() * y1) * 100) / 100, 
            int((a.get_value() * x2 + b.get_value() * y2) * 100) / 100
            ], color=m.PINK))
        self.play(m.Create(v3), run_time=0.3)

        self.wait()

        self.play(b.animate.set_value(1.5))
        self.wait(0.5)

        self.play(b.animate.set_value(-0.7))
        self.wait(0.5)

        self.play(b.animate.set_value(-3))
        self.wait(0.5)

        self.play(b.animate.set_value(0))
        self.wait(0.5)

        self.play(a.animate.set_value(-1.5), b.animate.set_value(-1.5))
        self.wait(0.5)

        self.play(a.animate.set_value(-3), b.animate.set_value(2))
        self.wait(0.5)

        self.play(a.animate.set_value(10), b.animate.set_value(-4))
        self.wait(0.5)

        self.play(a.animate.set_value(-1), b.animate.set_value(2))
        self.wait(0.5)

        self.wait(2)


class _VectorLinearCombineOneNull(Scene_):
    def construct(self):
        plane = m.NumberPlane()
        self.play(m.Create(plane), run_time=0.3)

        a = m.ValueTracker(1)
        b = m.ValueTracker(1)

        x1, x2 = 0, 0
        y1, y2 = 1.5, 1

        v1 = m.Dot()
        self.play(m.Create(v1), run_time=0.3)

        v2 = m.always_redraw(lambda: m.Vector([
            int(b.get_value() * y1 * 100) / 100, 
            int(b.get_value() * y2 * 100) / 100
            ], color=m.YELLOW))
        self.play(m.Create(v2), run_time=0.3)

        text = m.always_redraw(lambda: 
                m.Text("A = {:.2f}; B = {:.2f}".format(a.get_value(), b.get_value())).shift(m.UP * 3.5))
        self.play(m.Write(text), run_time=0.3)

        v3 = m.always_redraw(lambda: m.Vector([
            int((a.get_value() * x1 + b.get_value() * y1) * 100) / 100, 
            int((a.get_value() * x2 + b.get_value() * y2) * 100) / 100
            ], color=m.PINK))
        self.play(m.Create(v3), run_time=0.3)

        self.wait()

        self.play(b.animate.set_value(1.5))
        self.wait(0.5)

        self.play(b.animate.set_value(-0.7))
        self.wait(0.5)

        self.play(b.animate.set_value(-3))
        self.wait(0.5)

        self.play(b.animate.set_value(0))
        self.wait(0.5)

        self.play(a.animate.set_value(-1.5), b.animate.set_value(-1.5))
        self.wait(0.5)

        self.play(a.animate.set_value(-3), b.animate.set_value(2))
        self.wait(0.5)

        self.play(a.animate.set_value(10), b.animate.set_value(-4))
        self.wait(0.5)

        self.play(a.animate.set_value(-1), b.animate.set_value(2))
        self.wait(0.5)

        self.wait(2)


class VectorLinearCombine23D(ThreeDScene_):
    """
    Демонстрирует понятие линейной оболочки в трехмерном пространстве.
    Строит два трехмерных вектора и демонстрирует их всевозможные линейные комбинации.
    """
    def construct(self):
        plane = m.ThreeDAxes()
        self.play(m.Create(plane), run_time=0.3)

        self.move_camera(phi=75 * m.DEGREES, theta=-15 * m.DEGREES, zoom=1, run_time=1.5)
        self.begin_3dillusion_camera_rotation(rate=1.5)
        self.wait(0.5)

        a = m.ValueTracker(1)
        b = m.ValueTracker(1)

        x1, x2, x3 = 2, 1.5, 0.5
        y1, y2, y3 = -1.5, 1, 0.5

        v1 = m.always_redraw(lambda: m.Vector([
            int(a.get_value() * x1 * 100) / 100, 
            int(a.get_value() * x2 * 100) / 100, 
            int(a.get_value() * x3 * 100) / 100
            ]))
        self.play(m.Create(v1), run_time=0.3)

        v2 = m.always_redraw(lambda: m.Vector([
            int(b.get_value() * y1 * 100) / 100, 
            int(b.get_value() * y2 * 100) / 100, 
            int(b.get_value() * y3 * 100) / 100
            ], color=m.YELLOW))
        self.play(m.Create(v2), run_time=0.3)

        v3 = m.always_redraw(lambda: m.Vector([
            int((a.get_value() * x1 + b.get_value() * y1) * 100) / 100, 
            int((a.get_value() * x2 + b.get_value() * y2) * 100) / 100, 
            int((a.get_value() * x3 + b.get_value() * y3) * 100) / 100
            ], color=m.PINK))
        self.play(m.Create(v3), run_time=0.3)

        self.wait()

        self.play(a.animate.set_value(1.5), b.animate.set_value(1.5))
        self.wait(0.5)

        self.play(a.animate.set_value(3), b.animate.set_value(2))
        self.wait(0.5)

        self.play(a.animate.set_value(1), b.animate.set_value(-2))
        self.wait(0.5)

        self.play(a.animate.set_value(1), b.animate.set_value(2))
        self.wait(0.5)

        self.play(a.animate.set_value(0.5), b.animate.set_value(1.5))
        self.wait(0.5)

        self.wait(2)


class AddFunction(LinearTransformationScene_):
    """
    Показывает пример параллельного переноса как нелинейного преобразования 
    векторного пространства.
    """
    def __init__(self, **kwargs):
        LinearTransformationScene_.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False,
            leave_ghost_vectors=False,
            **kwargs
        )

    def construct(self):
        s = 1
        self.play(m.Create(m.Tex(
            r"$f(\vec{v}) = \vec{v} + \begin{bmatrix} 1  \\ 2 \end{bmatrix}$"
            ).scale(s).to_edge(m.UP, buff=1).to_edge(m.LEFT)), run_time=0.5)
        self.moving_mobjects = []

        self.play(m.Create(m.Vector([3, -2])), run_time=0.3)

        self.apply_nonlinear_transformation(lambda vec: vec + np.array([1, 2, 0])) 
        self.wait()   

        self.play(m.Create(m.Vector([4, 0], color=m.YELLOW)), run_time=0.3)
        self.wait()  


class AddNotLinear(LinearTransformationScene_):
    """
    Объясняет, почему параллельный перенос - не является линейным преобразованием.
    """
    def __init__(self, **kwargs):
        LinearTransformationScene_.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=True,
            leave_ghost_vectors=False,
            **kwargs
        )

    def construct(self):
        s = 1
        self.play(m.Create(m.Tex(r"$f(\vec{v}) = \vec{v} + \begin{bmatrix} 1  \\ 2 \end{bmatrix}$").scale(s).to_edge(m.UP, buff=1).to_edge(m.LEFT)), run_time=0.5)
        self.moving_mobjects = []

        self.play(m.Create(m.Vector([1, 1])), run_time=0.3)

        self.apply_nonlinear_transformation(lambda vec: vec + np.array([1, 2, 0])) 
        self.wait()   

        self.play(m.Create(m.Vector([2, 3], color=m.YELLOW)), run_time=0.3)
        self.wait()   


class NonLinearTransform_(LinearTransformationScene_):
    def __init__(self, **kwargs):
        LinearTransformationScene_.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            **kwargs
        )

    def apply_complex_func(self, func):
        def complex_func(vec):
            z = vec[0] + 1j * vec[1]
            res = func(z)
            return [res.real, res.imag, 0]
        self.apply_nonlinear_transformation(complex_func)   


class _Exp(NonLinearTransform_):
    def construct(self):
        self.apply_complex_func(lambda z: np.exp(z))
        self.wait()   


class Square(NonLinearTransform_):
    """
    Показывает пример нелинейного преобразования - возведение в квадрат.
    """
    def construct(self):
        self.apply_complex_func(lambda z: 0.5*z**2)
        self.wait()  

class LinearTransformExample(LinearTransformationScene_):
    """
    Показывает пример преобразования линейного пространства, которое является линейным.
    """
    def __init__(self, **kwargs):
        LinearTransformationScene_.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            show_basis_vectors=True,
            **kwargs
        )
    def construct(self):
        matrix = [
            [1.5, -0.3],
            [0.5, 2.5]
        ]

        self.add_vector([1, 1])
        self.apply_matrix(matrix)
        self.wait()
        self.apply_inverse(matrix)
        self.wait()

class VectorInTwoBases(Scene_):
    """
    Иллюстрирует один и тот же вектор в двух разных базисах.
    Стандартный базис: d₁, d₂ (ортонормированный)
    Альтернативный базис: d'₁, d'₂ 
    Вектор A: [2, -2] в стандартном, [0, -2] в новом базисе
    """
    def construct(self):
        plane = m.NumberPlane()
        self.play(m.Create(plane), run_time=0.2)

        # СТАНДАРТНЫЙ БАЗИС (серый цвет)
        i_std = m.Vector([1, 0], color=m.GRAY)
        i_std_label = m.MathTex("\\vec{d}_1", color=m.GRAY).next_to(i_std.get_end(), m.RIGHT)  
        g_i_std = m.VGroup(i_std, i_std_label)
        self.play(m.Create(g_i_std))

        j_std = m.Vector([0, 1], color=m.GRAY)
        j_std_label = m.MathTex("\\vec{d}_2", color=m.GRAY).next_to(j_std.get_end(), m.UP)  
        g_j_std = m.VGroup(j_std, j_std_label)
        self.play(m.Create(g_j_std))


        self.wait(0.3)

        # ВЕКТОР A в стандартном базисе (фиолетовый)
        # Координаты: [2, -2]
        vec_A = m.Vector([2, -2], color=m.PURPLE)
        vec_A_label = m.MathTex("\\vec{A}", color=m.PURPLE).next_to(vec_A.get_end(), m.DR)
        g_vec_A = m.VGroup(vec_A, vec_A_label)
        self.play(m.Create(g_vec_A))

        self.wait(0.3)

        # Координаты в стандартном базисе - серые, длинные скобки 
        coords_std = m.Matrix([["2.0"], ["-2.0"]], left_bracket="[", right_bracket="]", color=m.GRAY)
        coords_std.scale(0.6).next_to(vec_A.get_end(), m.RIGHT, buff=0.7)
        self.play(m.Create(coords_std))

        self.wait(0.6)


        # АЛЬТЕРНАТИВНЫЙ БАЗИС (золотой цвет)
        # d₁ = [2, 2], d₂ = [-1, 1]
        # НЕ ортонормированный!
        d1 = m.Vector([2, 2], color=m.YELLOW)
        d1_label = m.MathTex("\\vec{d}'_1", color=m.YELLOW).next_to(d1.get_end(), m.UR)
        g_d1 = m.VGroup(d1, d1_label)
        self.play(m.Create(g_d1))

        d2 = m.Vector([-1, 1], color=m.YELLOW)
        d2_label = m.MathTex("\\vec{d}'_2", color=m.YELLOW).next_to(d2.get_end(), m.UL)
        g_d2 = m.VGroup(d2, d2_label)
        self.play(m.Create(g_d2))

        self.wait(0.5)


        # Координаты в новом базисе - золотые, длинные скобки
        coords_new = m.Matrix([["0"], ["-2.0"]], left_bracket="[", right_bracket="]").set_color(m.YELLOW)
        coords_new.scale(0.6).next_to(vec_A.get_end(), m.UP, buff=0.6)
        self.play(m.Create(coords_new))


        self.wait(2)




class VectorLength(Scene_):
    """
    Иллюстрирует идею длины вектора через прямоугольный треугольник.
    Строит вектор на координатной плоскости и показывает его длину через 
    теорему Пифагора.
    """
    def construct(self):
        plane = m.NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": m.GRAY_E,
                "stroke_width": 1,
            }
        )
        self.play(m.Create(plane), run_time=0.2)

        # Вектор начинается в (-2, -2) и заканчивается в (1, 2)
        # Длина вектора: [3, 4] как и требуется
        start_point = np.array([-2, -2, 0])

        v = m.Vector([3, 4], color=m.PURPLE).shift(start_point)
        #v_label = m.MathTex("\\vec{v}", color=m.PURPLE).next_to(v.get_end(), m.UR, buff=0.2)
        g_v = m.VGroup(v)
        self.play(m.Create(g_v))

        self.wait(0.3)

        # Координаты вектора - серые длинные скобки
        coords_v = m.Matrix([["3.0"], ["4.0"]], left_bracket="[", right_bracket="]").set_color(m.GRAY)
        coords_v.scale(0.5).next_to(v.get_end(), m.RIGHT, buff=0.3)
        self.play(m.Create(coords_v))

        self.wait(0.3)

        # Катеты треугольника - тёмно-серый пунктир 
        leg_x = m.DashedLine(
            start=start_point, 
            end=start_point + np.array([3, 0, 0]), 
            color=m.DARK_GRAY, 
            stroke_width=4,
            dash_length=0.2
        )
        leg_x_label = m.MathTex("3", color=m.DARK_GRAY).next_to(leg_x, m.DOWN, buff=0.2)
        g_leg_x = m.VGroup(leg_x, leg_x_label)
        self.play(m.Create(g_leg_x))

        leg_y = m.DashedLine(
            start=start_point + np.array([3, 0, 0]), 
            end=start_point + np.array([3, 4, 0]), 
            color=m.DARK_GRAY, 
            stroke_width=4,
            dash_length=0.2
        )
        leg_y_label = m.MathTex("4", color=m.DARK_GRAY).next_to(leg_y, m.RIGHT, buff=0.2)
        g_leg_y = m.VGroup(leg_y, leg_y_label)
        self.play(m.Create(g_leg_y))

        self.wait(0.3)

        # Длина вектора 
        length_label = m.MathTex("|\\vec{v}| = 5", color=m.DARK_GRAY).next_to(v.get_midpoint(), m.LEFT, buff=0.5)
        self.play(m.Create(length_label))

        self.wait(0.3)

        # Формула длины вектора - компактная
        length_formula = m.MathTex(
            "|\\vec{v}| = \\sqrt{3^2 + 4^2} = \\sqrt{25} = 5",
            color=m.DARK_GRAY
        ).scale(0.7).to_edge(m.DOWN, buff=0.9)
        self.play(m.Create(length_formula))

        self.wait(2)

class VectorDifference(Scene_):
    """
    Иллюстрирует операцию вычитания векторов.
    Строит два вектора на координатной плоскости и показывает их разность 
    как вектор, соединяющий их концы.
    """
    def construct(self):
        plane = m.NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": m.GRAY_E,
                "stroke_width": 1,
            }
        )
        self.play(m.Create(plane), run_time=0.2)

        # Начало векторов
        start_point = np.array([-1, -1, 0])

        # Первый вектор a = [3, 2] (серый)
        a = m.Vector([3, 2], color=m.GRAY).shift(start_point)
        a_label = m.MathTex("\\vec{a}", color=m.GRAY).next_to(a.get_end(), m.UR, buff=0.2)
        g_a = m.VGroup(a, a_label)
        self.play(m.Create(g_a))

        # Координаты вектора a
        coords_a = m.Matrix([["3.0"], ["2.0"]], left_bracket="[", right_bracket="]").set_color(m.GRAY)
        coords_a.scale(0.5).next_to(a.get_end(), m.RIGHT, buff=0.45)
        self.play(m.Create(coords_a))

        self.wait(0.3)

        # Второй вектор b = [1, 3] (серый)
        b = m.Vector([1, 3], color=m.GRAY).shift(start_point)
        b_label = m.MathTex("\\vec{b}", color=m.GRAY).next_to(b.get_end(), m.UL, buff=0.2)
        g_b = m.VGroup(b, b_label)
        self.play(m.Create(g_b))

        # Координаты вектора b
        coords_b = m.Matrix([["1.0"], ["3.0"]], left_bracket="[", right_bracket="]").set_color(m.GRAY)
        coords_b.scale(0.5).next_to(b.get_end(), m.LEFT, buff=0.45)
        self.play(m.Create(coords_b))

        self.wait(0.3)

        # Разность векторов a - b = [2, -1] (фиолетовый ВЕКТОР с направлением!)
        diff_vector = m.Vector([2, -1], color=m.PURPLE).shift(start_point + np.array([1, 3, 0]))
        self.play(m.Create(diff_vector))

        # Вычисляем середину вручную через numpy
        diff_midpoint = (start_point + np.array([1, 3, 0]) + start_point + np.array([3, 2, 0])) / 2
        diff_label = m.MathTex("\\vec{a} - \\vec{b}", color=m.PURPLE).move_to(diff_midpoint + np.array([0.0, -0.3, 0]))
        self.play(m.Create(diff_label))

        self.wait(0.3)

        # Координаты разности
        coords_diff = m.Matrix([["2.0"], ["-1.0"]], left_bracket="[", right_bracket="]").set_color(m.PURPLE)
        coords_diff.scale(0.5).move_to(diff_midpoint + np.array([0.8, 0.5, 0]))
        self.play(m.Create(coords_diff))

        self.wait(0.3)

        # Подпись "расстояние между векторами"
        distance_note = m.Text(
            "расстояние между векторами",
            color=m.DARK_GRAY,
            font_size=24
        ).to_edge(m.DOWN, buff=0.5)
        self.play(m.Create(distance_note))

        self.wait(2)

class ScalarProduct(Scene_):
    """
    Иллюстрирует скалярное произведение векторов.
    Строит два вектора на координатной плоскости и показывает угол между ними.
    """
    def construct(self):
        plane = m.NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": m.GRAY_E,
                "stroke_width": 1,
            }
        )
        self.play(m.Create(plane), run_time=0.2)

        # Начало векторов
        start_point = np.array([-1, -1, 0])

        # Первый вектор a = [3, 1] (фиолетовый)
        a = m.Vector([3, 1], color=m.PURPLE).shift(start_point)
        a_label = m.MathTex("\\vec{a}", color=m.PURPLE).next_to(a.get_end(), m.UR, buff=0.2)
        g_a = m.VGroup(a, a_label)
        self.play(m.Create(g_a))

        # Координаты вектора a
        coords_a = m.Matrix([["3.0"], ["1.0"]], left_bracket="[", right_bracket="]").set_color(m.GRAY)
        coords_a.scale(0.5).next_to(a.get_end(), m.RIGHT, buff=0.45)
        self.play(m.Create(coords_a))

        self.wait(0.3)

        # Второй вектор b = [1, 2] (фиолетовый)
        b = m.Vector([1, 2], color=m.PURPLE).shift(start_point)
        b_label = m.MathTex("\\vec{b}", color=m.PURPLE).next_to(b.get_end(), m.UL, buff=0.2)
        g_b = m.VGroup(b, b_label)
        self.play(m.Create(g_b))

        # Координаты вектора b
        coords_b = m.Matrix([["1.0"], ["2.0"]], left_bracket="[", right_bracket="]").set_color(m.GRAY)
        coords_b.scale(0.5).next_to(b.get_end(), m.LEFT, buff=0.45)
        self.play(m.Create(coords_b))

        self.wait(0.3)

        # Угол между векторами φ (дуга)
        angle_arc = m.Arc(
            radius=0.8,
            start_angle=np.arctan2(1, 3),
            angle=np.arctan2(2, 1) - np.arctan2(1, 3),
            color=m.DARK_GRAY,
            stroke_width=3
        ).shift(start_point)
        self.play(m.Create(angle_arc))

        # Подпись угла φ
        phi_label = m.MathTex("\\varphi", color=m.DARK_GRAY).scale(0.7)
        phi_angle = (np.arctan2(1, 3) + np.arctan2(2, 1)) / 2
        phi_label.move_to(start_point + np.array([
            1.2 * np.cos(phi_angle),
            1.2 * np.sin(phi_angle),
            0
        ]))
        self.play(m.Create(phi_label))

        self.wait(0.3)

        # Формула скалярного произведения
        dot_product_formula = m.MathTex(
            "\\vec{a} \\cdot \\vec{b} = |\\vec{a}| \\cdot |\\vec{b}| \\cdot \\cos\\varphi",
            color=m.DARK_GRAY
        ).scale(0.7).to_edge(m.DOWN, buff=2.0)
        self.play(m.Create(dot_product_formula))

        self.wait(2)


class OrthogonalVectors(Scene_):
    """
    Иллюстрирует ортогональные векторы.
    Строит два перпендикулярных вектора и показывает, что их скалярное 
    произведение равно нулю.
    """
    def construct(self):
        plane = m.NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": m.GRAY_E,
                "stroke_width": 1,
            }
        )
        self.play(m.Create(plane), run_time=0.2)

        # Начало векторов
        start_point = np.array([-1, -1, 0])

        # Первый вектор a = [3, 0] (фиолетовый, горизонтальный)
        a = m.Vector([3, 0], color=m.PURPLE).shift(start_point)
        a_label = m.MathTex("\\vec{a}", color=m.PURPLE).next_to(a.get_end(), m.RIGHT, buff=0.2)
        g_a = m.VGroup(a, a_label)
        self.play(m.Create(g_a))

        # Координаты вектора a
        coords_a = m.Matrix([["3.0"], ["0.0"]], left_bracket="[", right_bracket="]").set_color(m.GRAY)
        coords_a.scale(0.5).next_to(a.get_end(), m.RIGHT, buff=0.55)
        self.play(m.Create(coords_a))

        self.wait(0.3)

        # Второй вектор b = [0, 2] (фиолетовый, вертикальный)
        b = m.Vector([0, 2], color=m.PURPLE).shift(start_point)
        b_label = m.MathTex("\\vec{b}", color=m.PURPLE).next_to(b.get_end(), m.UP, buff=0.2)
        g_b = m.VGroup(b, b_label)
        self.play(m.Create(g_b))

        # Координаты вектора b
        coords_b = m.Matrix([["0.0"], ["2.0"]], left_bracket="[", right_bracket="]").set_color(m.GRAY)
        coords_b.scale(0.5).next_to(b.get_end(), m.RIGHT, buff=0.45)
        self.play(m.Create(coords_b))

        self.wait(0.3)

        # Прямой угол между векторами (квадратик в углу) - рисуем вручную
        right_angle_line1 = m.Line(
            start=start_point + np.array([0.4, 0, 0]),
            end=start_point + np.array([0.4, 0.4, 0]),
            color=m.DARK_GRAY,
            stroke_width=3
        )
        right_angle_line2 = m.Line(
            start=start_point + np.array([0, 0.4, 0]),
            end=start_point + np.array([0.4, 0.4, 0]),
            color=m.DARK_GRAY,
            stroke_width=3
        )
        right_angle = m.VGroup(right_angle_line1, right_angle_line2)
        self.play(m.Create(right_angle))

        self.wait(0.3)

        # Подпись "ортогональные: скалярное произведение = 0"
        orthogonal_note = m.Text(
            "ортогональные: скалярное произведение = 0",
            color=m.DARK_GRAY,
            font_size=24
        ).to_edge(m.UP, buff=0.8)
        self.play(m.Create(orthogonal_note))

        self.wait(0.3)

        # Формула скалярного произведения
        dot_product_formula = m.MathTex(
            "\\vec{a} \\cdot \\vec{b} = 3 \\cdot 0 + 0 \\cdot 2 = 0",
            color=m.DARK_GRAY
        ).scale(0.7).next_to(orthogonal_note, m.DOWN, buff=0.3)
        self.play(m.Create(dot_product_formula))

        self.wait(2)

class VectorProjection(Scene_):
    """
    Иллюстрирует проекцию вектора на другой вектор.
    Показывает связь скалярного произведения с длиной проекции.
    """
    def construct(self):
        plane = m.NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": m.GRAY_E,
                "stroke_width": 1,
            }
        )
        self.play(m.Create(plane), run_time=0.2)

        # Начало векторов
        start_point = np.array([-2, -1, 0])

        # Вектор b = [4, 0] (горизонтальный, СЕРЫЙ - это ось проекции)
        b = m.Vector([4, 0], color=m.GRAY).shift(start_point)
        b_label = m.MathTex("\\vec{b}", color=m.GRAY).next_to(b.get_end(), m.RIGHT, buff=0.2)
        g_b = m.VGroup(b, b_label)
        self.play(m.Create(g_b))

        # Координаты вектора b
        coords_b = m.Matrix([["4.0"], ["0.0"]], left_bracket="[", right_bracket="]").set_color(m.GRAY)
        coords_b.scale(0.5).next_to(b.get_end(), m.RIGHT, buff=0.45)
        self.play(m.Create(coords_b))

        self.wait(0.3)

        # Вектор a = [3, 2] (под углом, ФИОЛЕТОВЫЙ)
        a = m.Vector([3, 2], color=m.PURPLE).shift(start_point)
        a_label = m.MathTex("\\vec{a}", color=m.PURPLE).next_to(a.get_end(), m.UR, buff=0.2)
        g_a = m.VGroup(a, a_label)
        self.play(m.Create(g_a))

        # Координаты вектора a
        coords_a = m.Matrix([["3.0"], ["2.0"]], left_bracket="[", right_bracket="]").set_color(m.GRAY)
        coords_a.scale(0.5).next_to(a.get_end(), m.RIGHT, buff=0.45)
        self.play(m.Create(coords_a))

        self.wait(0.3)

        # Проекция вектора a на вектор b (СПЛОШНАЯ серо-фиолетовая линия)
        # Проекция = [3, 0] (только x-компонента)
        proj = m.Line(
            start=start_point,
            end=start_point + np.array([3, 0, 0]),
            color=m.PURPLE,
            stroke_width=5,
            stroke_opacity=0.6
        )
        self.play(m.Create(proj))

        # Перпендикуляр от конца a к проекции (ТОЛСТЫЙ фиолетовый пунктир)
        perp = m.DashedLine(
            start=start_point + np.array([3, 0, 0]),
            end=start_point + np.array([3, 2, 0]),
            color=m.PURPLE,
            stroke_width=5,
            dash_length=0.15
        )
        self.play(m.Create(perp))

        self.wait(0.3)

        # Подпись длины проекции (фиолетовая)
        proj_label = m.MathTex("|\\vec{a}_b| = 3", color=m.PURPLE).next_to(proj, m.DOWN, buff=0.3)
        self.play(m.Create(proj_label))

        self.wait(0.3)

        # Формула скалярного произведения через проекцию
        dot_product_formula = m.MathTex(
            "\\vec{a} \\cdot \\vec{b} = |\\vec{b}| \\cdot |\\vec{a}_b| = 4 \\cdot 3 = 12",
            color=m.DARK_GRAY
        ).scale(0.7).to_edge(m.DOWN, buff=0.5)
        self.play(m.Create(dot_product_formula))

        self.wait(0.3)

        # Альтернативная формула через cos
        cos_formula = m.MathTex(
            "\\vec{a} \\cdot \\vec{b} = |\\vec{a}| \\cdot |\\vec{b}| \\cdot \\cos\\varphi",
            color=m.DARK_GRAY
        ).scale(0.7).next_to(dot_product_formula, m.UP, buff=0.3)
        self.play(m.Create(cos_formula))

        self.wait(2)
        


if __name__ == '__main__':
    import subprocess
    from pathlib import Path

    SCENES = [
        # "VectorsExample",
        # "VectorShift",
        # "VectorsAsDots",
        # "VectorsNDim",
        # "VectorScaling",
        # "VectorSumTriangle",
        #"VectorSumParallelogram",
        # "VectorSumScaling",
        # "VectorLinearCombine",
        # "VectorSumThree",
        # "VectorBasis",
        # "VectorLinearCombineCollinear",
        # "VectorLinearCombine23D",
        #"AddFunction",
        #"AddNotLinear",
        #"Square",
        #"LinearTransformExample",
        #"VectorInTwoBases",
        #"VectorLength",
        #"VectorDifference",
        #"ScalarProduct",
        #"OrthogonalVectors",
        "VectorProjection",
  
    ]
    file_path = Path(__file__).resolve()

    for SCENE in SCENES:
        # Генерация видео
        subprocess.run(["manim", str(file_path), SCENE, "-qh"])
        # Генерация последнего кадра
        subprocess.run(["manim", str(file_path), SCENE, "-s"])
