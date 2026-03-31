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


if __name__ == '__main__':
    import os
    from pathlib import Path

    SCENES = [
        # "VectorsExample",
        # "VectorShift",
        # "VectorsAsDots",
        # "VectorsNDim",
        # "VectorScaling",
        # "VectorSumTriangle",
        # "VectorSumParallelogram",
        # "VectorSumScaling",
        # "VectorLinearCombine",
        # "VectorSumThree",
        # "VectorBasis",
        # "VectorLinearCombineCollinear",
        # "VectorLinearCombine23D",
        "AddFunction",
        "AddNotLinear",
        "Square",
        "LinearTransformExample",
    ]
    file_path = Path(__file__).resolve()

    for SCENE in SCENES:
        os.system(f"manim {Path(__file__).resolve()} {SCENE} -qh")
        os.system(f"manim {Path(__file__).resolve()} {SCENE} -s")
