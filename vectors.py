from manim import *
import numpy as np
from math import sin, ceil

class VectorsExample(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane))

        x = ValueTracker(1)
        y = ValueTracker(2)

        vector = Vector([1,2])
        vector.add_updater(lambda m: m.become(Vector([
            int(x.get_value() * 100) / 100, 
            int(y.get_value() * 100) / 100
            ])))
        self.play(Create(vector))

        label = vector.coordinate_label()
        label.add_updater(lambda m: m.become(vector.coordinate_label()))
        self.play(Write(label))

        self.play(x.animate.set_value(3), y.animate.set_value(-2))
        self.wait(0.5)

        self.play(x.animate.set_value(-4), y.animate.set_value(1))
        self.wait(0.5)

        label.become(vector.coordinate_label(integer_labels=False))
        label.add_updater(lambda m: m.become(vector.coordinate_label(integer_labels=False)))
        self.wait(0.5)

        self.play(x.animate.set_value(-2.73), y.animate.set_value(-0.376))
        # label.become(vector.coordinate_label(integer_labels=False))
        self.wait(0.5)

        self.play(x.animate.set_value(-3), y.animate.set_value(0))
        # label.become(vector.coordinate_label(integer_labels=False))
        self.wait(0.5)

        self.wait()

class VectorShift(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane), run_time=0.3)

        vector = Vector([1,2])
        label = vector.coordinate_label()

        group = VGroup(vector, label)

        self.play(Create(group))

        self.play(group.animate.move_to(LEFT))
        self.wait(0.5)

        self.play(group.animate.move_to(UP))
        self.wait(0.5)

        self.play(group.animate.move_to(RIGHT * 2))
        self.wait(0.5)

        self.wait()


class VectorsAsDots(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane), run_time=0.3)

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
            vector = Vector(vec)
            self.play(Create(vector), run_time=0.3)
            label = vector.coordinate_label()
            self.play(Create(label), run_time=0.1)
            vectors.append(vector)
            labels.append(label)
            
        self.wait()

        for i in range(len(vectors)):
            vectors[i].become(Dot(point=[vecs[i][0], vecs[i][1], 0]))
            
        self.wait()

        for label in labels:
            self.remove(label)
            
        self.wait(2)


class VectorsAsLine(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane), run_time=0.3)

        vectors = []

        vecs = list(zip(np.linspace(-7, 7, 30), np.linspace(-7, 7, 30) * 0.3 + 1))
        # print(vecs)

        for vec in vecs:
            vector = Vector(vec)
            self.play(Create(vector), run_time=0.1)
            vectors.append(vector)
            
        self.wait()
        dots = []

        for i in range(len(vectors)):
            dot = Dot(point=[vecs[i][0], vecs[i][1], 0])
            vectors[i].become(dot)
            dots.append(dot)
            
        self.wait()

        line = Line([-7, -7 * 0.3 + 1, 0], [7, 7 * 0.3 + 1, 0])
        self.play(Write(line))
            
        self.wait(2)

class VectorsNDim(ThreeDScene):
    def construct(self):
        plane = NumberLine()
        self.play(Create(plane), run_time=0.3)

        x = ValueTracker(3)
        y = ValueTracker(0)
        z = ValueTracker(0)

        vector = Vector([3,0])
        vector.add_updater(lambda m: m.become(Vector([
            x.get_value(),
            y.get_value(),
            z.get_value()
            ])))
        self.play(Create(vector))

        label = vector.coordinate_label(n_dim=1)
        label.add_updater(lambda m: m.become(vector.coordinate_label(n_dim=1)))
        self.play(Write(label))

        self.play(x.animate.set_value(-1), y.animate.set_value(0))
        self.wait(0.5)

        self.play(x.animate.set_value(-4), y.animate.set_value(0))
        self.wait(0.5)

        self.play(x.animate.set_value(2), y.animate.set_value(0))
        self.wait(0.5)

        label.become(vector.coordinate_label(n_dim=2))
        label.add_updater(lambda m: m.become(vector.coordinate_label(n_dim=2)))
        self.wait(0.5)

        plane.become(NumberPlane())
        self.wait(0.5)

        self.play(x.animate.set_value(2), y.animate.set_value(-3))
        self.wait(0.5)

        self.play(x.animate.set_value(-1), y.animate.set_value(1))
        self.wait(0.5)

        plane.become(ThreeDAxes())
        self.wait(0.5)

        label.become(vector.coordinate_label(n_dim=3))
        label.add_updater(lambda m: m.become(vector.coordinate_label(n_dim=3)))
        self.wait(0.5)

        self.move_camera(phi=60 * DEGREES, theta=-15 * DEGREES, zoom=1, run_time=1.5)
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

class Vectorsd(ThreeDScene):
    def construct(self):
        plane = NumberLine()
        self.play(Create(plane), run_time=0.3)

        x = ValueTracker(3)
        y = ValueTracker(0)
        z = ValueTracker(0)

        vector = Vector([3,0])
        vector.add_updater(lambda m: m.become(Vector([
            x.get_value(),
            y.get_value(),
            z.get_value()
            ])))
        self.play(Create(vector))

        label = vector.coordinate_label(n_dim=1)
        label.add_updater(lambda m: m.become(vector.coordinate_label(n_dim=1)))
        self.play(Write(label))

        plane.become(ThreeDAxes())
        self.wait(0.5)

        label.become(vector.coordinate_label(n_dim=3))
        label.add_updater(lambda m: m.become(vector.coordinate_label(n_dim=3)))
        self.wait(0.5)

        self.move_camera(phi=60 * DEGREES, theta=-15 * DEGREES, zoom=1, run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(0.5)

        self.play(x.animate.set_value(3), y.animate.set_value(0), z.animate.set_value(3))
        self.wait(0.5)

        self.play(x.animate.set_value(-2), y.animate.set_value(-2), z.animate.set_value(3))
        self.wait(0.5)

        self.play(x.animate.set_value(1), y.animate.set_value(3), z.animate.set_value(-2))
        self.wait(0.5)

        self.wait(2)


class VectorScaling(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane))

        x = ValueTracker(2)
        y = ValueTracker(1)
        s = ValueTracker(2)

        vector = always_redraw(lambda: Vector([
            int(x.get_value() * 100) / 100, 
            int(y.get_value() * 100) / 100
            ]))
        self.play(Create(vector))

        label = always_redraw(lambda: vector.coordinate_label(integer_labels=False))
        self.play(Write(label))

        text = always_redraw(lambda: Text("Скаляр: {:.2f}".format(s.get_value())).shift(UP * 3.5))
        self.play(Write(text))

        scaled = always_redraw(lambda: Vector([
            int(x.get_value() * s.get_value() * 100) / 100, 
            int(y.get_value() * s.get_value() * 100) / 100
            ], color=YELLOW))
        self.play(Create(scaled))

        label = always_redraw(lambda: scaled.coordinate_label(integer_labels=False, color=YELLOW))
        self.play(Write(label))

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


class VectorSum(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane), run_time=0.2)

        v1 = Vector([2, 3])
        l1 = v1.coordinate_label(integer_labels=False)
        g1= VGroup(v1, l1)
        self.play(Create(g1))

        v2 = Vector([1, -1], color=YELLOW)
        l2 = v2.coordinate_label(integer_labels=False, color=YELLOW)
        g2= VGroup(v2, l2)
        self.play(Create(g2))

        self.play(v2.animate.shift(v1.get_end()))
        self.wait(0.5)

        self.remove(l2)
        self.wait(0.5)

        v3 = Vector([3, 2], color=PINK)
        l3 = v3.coordinate_label(integer_labels=False, color=PINK)
        g3= VGroup(v3, l3)
        self.play(Create(g3))

        self.wait(2)


class VectorSumAround(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane), run_time=0.2)

        v1 = Vector([2, 3])
        l1 = v1.coordinate_label(integer_labels=False)
        g1= VGroup(v1, l1)
        self.play(Create(g1))

        v2 = Vector([1, -1], color=YELLOW)
        l2 = v2.coordinate_label(integer_labels=False, color=YELLOW)
        g2= VGroup(v2, l2)
        self.play(Create(g2))

        v21 = Vector([1, -1], color=YELLOW)
        self.play(v21.animate.shift(v1.get_end()))
        self.wait(0.5)

        v12 = Vector([2, 3])
        self.play(v12.animate.shift(v2.get_end()))
        self.wait(0.5)

        self.remove(l2)
        self.wait(0.5)

        v3 = Vector([3, 2], color=PINK)
        l3 = v3.coordinate_label(integer_labels=False, color=PINK)
        g3= VGroup(v3, l3)
        self.play(Create(g3))

        self.wait(2)


class VectorSumScaling(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane), run_time=0.3)

        s = ValueTracker(1)

        v1 = always_redraw(lambda: Vector([
            int(s.get_value() * 2 * 100) / 100, 
            int(s.get_value() * 3 * 100) / 100
            ]))
        self.play(Create(v1))

        v2 = always_redraw(lambda: Vector([
            int(s.get_value() * 1 * 100) / 100, 
            int(s.get_value() * (-1) * 100) / 100
            ], color=YELLOW))
        self.play(Create(v2))

        text = always_redraw(lambda: Text("Скаляр: {:.2f}".format(s.get_value())).shift(UP * 3.5))
        self.play(Write(text))

        # v21 = Vector([1, -1], color=YELLOW)
        # self.play(v21.animate.shift(v1.get_end()), run_time=0.3)
        # self.wait(0.5)

        # v12 = Vector([2, 3])
        # self.play(v12.animate.shift(v2.get_end()), run_time=0.3)
        # self.wait(0.5)

        v3 = always_redraw(lambda: Vector([
            int(s.get_value() * 3 * 100) / 100, 
            int(s.get_value() * 2 * 100) / 100
            ], color=PINK))
        self.play(Create(v3))

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


class VectorLinearCombine(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane), run_time=0.3)

        a = ValueTracker(1)
        b = ValueTracker(1)

        x1, x2 = 0.8, 0.5
        y1, y2 = 1, 1.6

        v1 = always_redraw(lambda: Vector([
            int(a.get_value() * x1 * 100) / 100, 
            int(a.get_value() * x2 * 100) / 100
            ]))
        self.play(Create(v1), run_time=0.3)

        v2 = always_redraw(lambda: Vector([
            int(b.get_value() * y1 * 100) / 100, 
            int(b.get_value() * y2 * 100) / 100
            ], color=YELLOW))
        self.play(Create(v2), run_time=0.3)

        text = always_redraw(lambda: 
                Text("A = {:.2f}; B = {:.2f}".format(a.get_value(), b.get_value())).shift(UP * 3.5))
        self.play(Write(text), run_time=0.3)

        # v21 = Vector([1, -1], color=YELLOW)
        # self.play(v21.animate.shift(v1.get_end()), run_time=0.3)
        # self.wait(0.5)

        # v12 = Vector([2, 3])
        # self.play(v12.animate.shift(v2.get_end()), run_time=0.3)
        # self.wait(0.5)

        v3 = always_redraw(lambda: Vector([
            int((a.get_value() * x1 + b.get_value() * y1) * 100) / 100, 
            int((a.get_value() * x2 + b.get_value() * y2) * 100) / 100
            ], color=PINK))
        self.play(Create(v3), run_time=0.3)

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


class VectorLinearCombineCollinear(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane), run_time=0.3)

        a = ValueTracker(1)
        b = ValueTracker(1)

        x1, x2 = 0.8, 0.5
        y1, y2 = 1.6, 1

        v1 = always_redraw(lambda: Vector([
            int(a.get_value() * x1 * 100) / 100, 
            int(a.get_value() * x2 * 100) / 100
            ]))
        self.play(Create(v1), run_time=0.3)

        v2 = always_redraw(lambda: Vector([
            int(b.get_value() * y1 * 100) / 100, 
            int(b.get_value() * y2 * 100) / 100
            ], color=YELLOW))
        self.play(Create(v2), run_time=0.3)

        text = always_redraw(lambda: 
                Text("A = {:.2f}; B = {:.2f}".format(a.get_value(), b.get_value())).shift(UP * 3.5))
        self.play(Write(text), run_time=0.3)

        v3 = always_redraw(lambda: Vector([
            int((a.get_value() * x1 + b.get_value() * y1) * 100) / 100, 
            int((a.get_value() * x2 + b.get_value() * y2) * 100) / 100
            ], color=PINK))
        self.play(Create(v3), run_time=0.3)

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


class VectorLinearCombineNull(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane), run_time=0.3)

        a = ValueTracker(1)
        b = ValueTracker(1)

        x1, x2 = 0, 0
        y1, y2 = 0, 0

        v1 = Dot()
        self.play(Create(v1), run_time=0.3)

        v2 = always_redraw(lambda: Vector([
            int(b.get_value() * y1 * 100) / 100, 
            int(b.get_value() * y2 * 100) / 100
            ], color=YELLOW))
        self.play(Create(v2), run_time=0.3)

        text = always_redraw(lambda: 
                Text("A = {:.2f}; B = {:.2f}".format(a.get_value(), b.get_value())).shift(UP * 3.5))
        self.play(Write(text), run_time=0.3)

        v3 = always_redraw(lambda: Vector([
            int((a.get_value() * x1 + b.get_value() * y1) * 100) / 100, 
            int((a.get_value() * x2 + b.get_value() * y2) * 100) / 100
            ], color=PINK))
        self.play(Create(v3), run_time=0.3)

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


class VectorLinearCombineOneNull(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane), run_time=0.3)

        a = ValueTracker(1)
        b = ValueTracker(1)

        x1, x2 = 0, 0
        y1, y2 = 1.5, 1

        v1 = Dot()
        self.play(Create(v1), run_time=0.3)

        v2 = always_redraw(lambda: Vector([
            int(b.get_value() * y1 * 100) / 100, 
            int(b.get_value() * y2 * 100) / 100
            ], color=YELLOW))
        self.play(Create(v2), run_time=0.3)

        text = always_redraw(lambda: 
                Text("A = {:.2f}; B = {:.2f}".format(a.get_value(), b.get_value())).shift(UP * 3.5))
        self.play(Write(text), run_time=0.3)

        v3 = always_redraw(lambda: Vector([
            int((a.get_value() * x1 + b.get_value() * y1) * 100) / 100, 
            int((a.get_value() * x2 + b.get_value() * y2) * 100) / 100
            ], color=PINK))
        self.play(Create(v3), run_time=0.3)

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


class VectorLinearCombineOneNull(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane), run_time=0.3)

        a = ValueTracker(1)
        b = ValueTracker(1)

        x1, x2 = 0, 0
        y1, y2 = 1.5, 1

        v1 = Dot()
        self.play(Create(v1), run_time=0.3)

        v2 = always_redraw(lambda: Vector([
            int(b.get_value() * y1 * 100) / 100, 
            int(b.get_value() * y2 * 100) / 100
            ], color=YELLOW))
        self.play(Create(v2), run_time=0.3)

        text = always_redraw(lambda: 
                Text("A = {:.2f}; B = {:.2f}".format(a.get_value(), b.get_value())).shift(UP * 3.5))
        self.play(Write(text), run_time=0.3)

        v3 = always_redraw(lambda: Vector([
            int((a.get_value() * x1 + b.get_value() * y1) * 100) / 100, 
            int((a.get_value() * x2 + b.get_value() * y2) * 100) / 100
            ], color=PINK))
        self.play(Create(v3), run_time=0.3)

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


class VectorLinearCombine23D(ThreeDScene):
    def construct(self):
        plane = ThreeDAxes()
        self.play(Create(plane), run_time=0.3)

        self.move_camera(phi=75 * DEGREES, theta=-15 * DEGREES, zoom=1, run_time=1.5)
        self.begin_3dillusion_camera_rotation(rate=1.5)
        self.wait(0.5)

        a = ValueTracker(1)
        b = ValueTracker(1)

        x1, x2, x3 = 2, 1.5, 0.5
        y1, y2, y3 = -1.5, 1, 0.5

        v1 = always_redraw(lambda: Vector([
            int(a.get_value() * x1 * 100) / 100, 
            int(a.get_value() * x2 * 100) / 100, 
            int(a.get_value() * x3 * 100) / 100
            ]))
        self.play(Create(v1), run_time=0.3)

        v2 = always_redraw(lambda: Vector([
            int(b.get_value() * y1 * 100) / 100, 
            int(b.get_value() * y2 * 100) / 100, 
            int(b.get_value() * y3 * 100) / 100
            ], color=YELLOW))
        self.play(Create(v2), run_time=0.3)

        v3 = always_redraw(lambda: Vector([
            int((a.get_value() * x1 + b.get_value() * y1) * 100) / 100, 
            int((a.get_value() * x2 + b.get_value() * y2) * 100) / 100, 
            int((a.get_value() * x3 + b.get_value() * y3) * 100) / 100
            ], color=PINK))
        self.play(Create(v3), run_time=0.3)

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


class VectorSumThree(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane), run_time=0.2)

        v1 = Vector([2, 3])
        l1 = v1.coordinate_label(integer_labels=False)
        g1= VGroup(v1, l1)
        self.play(Create(g1))

        v2 = Vector([1, -1], color=YELLOW)
        l2 = v2.coordinate_label(integer_labels=False, color=YELLOW)
        g2= VGroup(v2, l2)
        self.play(Create(g2))

        v3 = Vector([3, 2], color=PINK)
        l3 = v3.coordinate_label(integer_labels=False, color=PINK)
        g3= VGroup(v3, l3)
        self.play(Create(g3))

        self.wait(1)

        self.remove(l2, l1, l3)
        self.wait(0.5)

        self.play(v2.animate.shift(v1.get_end()))
        text = Tex(r"$\vec{v_3} = \vec{v_1} + \vec{v_2}$").shift(UP * 3.5)
        self.play(Write(text), run_time=0.3)
        self.wait(1)
        self.play(Unwrite(text), run_time=0.3)

        self.play(v2.animate.become(Vector([1, -1], color=YELLOW)))
        self.wait(0.5)

        self.play(v2.animate.become(Vector([-1, 1], color=YELLOW)))
        self.wait(0.5)

        self.play(v2.animate.shift(v3.get_end()))
        text = Tex(r"$\vec{v_2} = \vec{v_3} + (-1) \vec{v_2}$").shift(UP * 3.5)
        self.play(Write(text), run_time=0.3)
        self.wait(1)
        self.play(Unwrite(text), run_time=0.3)

        self.play(v2.animate.become(Vector([1, -1], color=YELLOW)))
        self.wait(0.5)

        self.play(v1.animate.become(Vector([-2, -3])))
        self.wait(0.5)

        self.play(v1.animate.shift(v3.get_end()))
        text = Tex(r"$\vec{v_2} = \vec{v_3} + (-1) \vec{v_1}$").shift(UP * 3.5)
        self.play(Write(text), run_time=0.3)
        self.wait(1)
        self.play(Unwrite(text), run_time=0.3)

        self.play(v1.animate.become(Vector([2, 3])))
        self.wait(0.5)

        self.wait(2)


class VectorBasis(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane), run_time=0.3)

        a = ValueTracker(1)
        b = ValueTracker(1)

        x1, x2 = 1, 0
        y1, y2 = 0, 1

        v1 = always_redraw(lambda: Vector([
            int(a.get_value() * x1 * 100) / 100, 
            int(a.get_value() * x2 * 100) / 100
            ]))
        self.play(Create(v1), run_time=0.3)

        v2 = always_redraw(lambda: Vector([
            int(b.get_value() * y1 * 100) / 100, 
            int(b.get_value() * y2 * 100) / 100
            ], color=YELLOW))
        self.play(Create(v2), run_time=0.3)

        text = always_redraw(lambda: 
                Text("A = {:.2f}; B = {:.2f}".format(a.get_value(), b.get_value())).shift(UP * 3.5))
        self.play(Write(text), run_time=0.3)

        v3 = always_redraw(lambda: Vector([
            int((a.get_value() * x1 + b.get_value() * y1) * 100) / 100, 
            int((a.get_value() * x2 + b.get_value() * y2) * 100) / 100
            ], color=PINK))
        self.play(Create(v3), run_time=0.3)

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
