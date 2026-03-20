from manim import *
import manium as m
import numpy as np
from math import sin, ceil
from theming import LinearTransformationScene_, ThreeDScene_

class LinearTransformExample(LinearTransformationScene_):
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

class LTNonSquare(LinearTransformationScene_):
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
            [2, 1],
            [0, 0]
        ]
        matrix = np.array(matrix).T

        self.matrix_text = m.Matrix(matrix).scale(1).to_edge(m.UP, buff=1).to_edge(m.LEFT)
        self.play(m.Create(self.matrix_text), run_time=0.3)
        self.wait()

        self.add_vector(vec := m.Vector([2, 1.5]))
        self.apply_matrix(matrix)
        self.wait()

class LT2d23d(LinearTransformationScene_):
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
            [1.5, 1],
        ]
        vec_ = np.array([1, 2])

        self.matrix_text = m.Matrix(matrix).scale(1).to_edge(m.UP, buff=1).to_edge(m.LEFT)
        self.play(m.Create(self.matrix_text), run_time=0.3)
        self.wait()
        matrix = np.concat([matrix, np.array([[0, 0]])], axis=0)
        print(matrix)

        self.add_vector(vec := m.Vector(vec_))
        self.apply_matrix(matrix)
        self.wait()

        print(np.dot(matrix, vec_.T))
        vec = vec.become(m.Vector(np.dot(matrix, vec_.T)))
        label = vec.coordinate_label(integer_labels=False, n_dim=1).shift(m.UP * 0.5)
        self.play(m.Create(label), run_time=0.3)
        self.wait()

class LinearTransform(LinearTransformationScene_):
    def __init__(self, **kwargs):
        LinearTransformationScene_.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs
        )

    def apply_custom_matrix(self, matrix):
        matrix = np.array(matrix).T

        self.matrix_text = m.Matrix(matrix).scale(1).to_edge(m.UP, buff=1).to_edge(m.LEFT)
        self.play(m.Create(self.matrix_text), run_time=0.3)
        self.wait()

        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait()

        self.moving_mobjects = []
        self.apply_inverse(matrix)
        self.wait()

    def construct(self):
        matrix = [
            [1, 0],
            [0, 1]
        ]
        self.apply_custom_matrix(matrix)
        # self.play(m.Uncreate(self.matrix_text), run_time=0.3)

class MatrixVectorMul(LinearTransform):
    def __init__(self, **kwargs):
        LinearTransformationScene_.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            **kwargs
        )

    def apply_custom_matrix(self, matrix):
        matrix = np.array(matrix).T

        self.matrix_text = m.Matrix(matrix).scale(1).to_edge(m.UP, buff=1).to_edge(m.LEFT)
        self.play(m.Create(self.matrix_text), run_time=0.3)
        self.wait()

        vec = self.add_vector([2, 1.5])
        label = vec.coordinate_label(integer_labels=False)
        self.play(m.Create(label), run_time=0.3)
        self.wait()
        self.play(m.Uncreate(label), run_time=0.3)

        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait()

        self.wait(0.5)
        vec = vec.become(m.Vector([3.75, 3.15], color=m.YELLOW))
        label = vec.coordinate_label(integer_labels=False)
        self.play(m.Create(label), run_time=0.3)
        self.wait()
        self.play(m.Uncreate(label), run_time=0.3)

        self.play(m.Create(label), run_time=0.3)
        self.wait()
        self.play(m.Uncreate(label), run_time=0.3)

        self.moving_mobjects = []
        self.apply_inverse(matrix)
        self.play(m.Uncreate(self.matrix_text), run_time=0.3)
        self.wait()

    def construct(self):
        matrix = [
            [1.5, -0.3],
            [0.5, 2.5]
        ]

        self.apply_custom_matrix(matrix)

class LTExample(LinearTransform):
    def construct(self):
        matrix = [
            [1.5, -0.3],
            [0.5, 2.5]
        ]
        self.apply_custom_matrix(matrix)

class LTTranspose(LinearTransform):
    def construct(self):
        matrix = np.array([
            [1.5, -0.3],
            [0.5, 2.5]
        ])
        self.apply_custom_matrix(matrix)
        self.apply_custom_matrix(matrix.T)

class LTTranspose2(LinearTransform):
    def construct(self):
        matrix = np.array([
            [2, -1],
            [4, 3]
        ])
        self.apply_custom_matrix(matrix)
        self.apply_custom_matrix(matrix.T)

class LTShift(LinearTransform):
    def construct(self):
        matrix = np.array([
            [0, 1],
            [1, 0]
        ])
        self.apply_custom_matrix(matrix)
        self.apply_custom_matrix(matrix.T)

class SVD(LinearTransformationScene_):
    def __init__(self, **kwargs):
        LinearTransformationScene_.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            **kwargs
        )

    def construct(self):
        matrix = np.array([[0.8, 0], [0.5, 3]]).T

        s = 0.7

        self.play(m.Create(A := m.Matrix(matrix).scale(s).to_edge(m.DOWN, buff=1).to_edge(m.LEFT)), run_time=0.01)

        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait()

        i = m.Vector([matrix[0][0], matrix[1][0]], color=m.GREEN)
        j = m.Vector([matrix[0][1], matrix[1][1]], color=m.RED)
        self.play(m.Create(i), run_time=0.01)
        self.play(m.Create(j), run_time=0.01)

        self.moving_mobjects = []
        self.apply_inverse(matrix)
        self.wait()

        U, S, Vh = np.linalg.svd(matrix, full_matrices=True)
        print(Vh)
        print(np.diag(S))
        print(U)

        self.play(m.Create(t1 := m.Text("=").scale(s).next_to(A, m.RIGHT)), run_time=0.01)
        self.play(m.Create(U_label := m.Matrix(np.round(U,2), stroke_width=7).scale(s).next_to(t1, m.RIGHT)), run_time=0.01)
        self.play(m.Create(t2 := m.Tex(r"$\times$").scale(s).next_to(U_label, m.RIGHT)), run_time=0.01)
        self.play(m.Create(S_label := m.Matrix(np.round(np.diag(S),2), stroke_width=7).scale(s).next_to(t2, m.RIGHT)), run_time=0.01)
        self.play(m.Create(t3 := m.Tex(r"$\times$").scale(s).next_to(S_label, m.RIGHT)), run_time=0.01)
        self.play(m.Create(V_label := m.Matrix(np.round(Vh,2), stroke_width=7).scale(s).next_to(t3, m.RIGHT)), run_time=0.01)
        self.wait()

        self.play(V_label.animate.set_color(m.YELLOW), run_time=0.3)
        self.play(m.Create(t := m.Text("Поворот", color=m.YELLOW).scale(s).next_to(V_label, m.UP)), run_time=0.01)
        self.moving_mobjects = []
        self.apply_matrix(Vh)
        self.play(m.Uncreate(t))
        self.play(V_label.animate.set_color(m.WHITE), run_time=0.3)
        self.wait()

        self.play(S_label.animate.set_color(m.YELLOW), run_time=0.3)
        self.play(m.Create(t := m.Text("Масштабирование", color=m.YELLOW).scale(s).next_to(S_label, m.UP)), run_time=0.01)
        self.moving_mobjects = []
        self.apply_matrix(np.diag(S))
        self.play(m.Uncreate(t))
        self.play(S_label.animate.set_color(m.WHITE), run_time=0.3)
        self.wait()

        self.play(U_label.animate.set_color(m.YELLOW), run_time=0.3)
        self.play(m.Create(t := m.Text("Поворот", color=m.YELLOW).scale(s).next_to(U_label, m.UP)), run_time=0.01)
        self.moving_mobjects = []
        self.apply_matrix(U)
        self.play(m.Uncreate(t))
        self.play(U_label.animate.set_color(m.WHITE), run_time=0.3)
        self.wait()


class AddFunction(LinearTransformationScene_):
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
        self.play(m.Create(m.Tex(r"$f(\vec{v}) = \vec{v} + \begin{bmatrix} 1  \\ 2 \end{bmatrix}$").scale(s).to_edge(m.UP, buff=1).to_edge(m.LEFT)), run_time=0.5)
        self.moving_mobjects = []

        self.play(m.Create(m.Vector([3, -2])), run_time=0.3)

        self.apply_nonlinear_transformation(lambda vec: vec + np.array([1, 2, 0])) 
        self.wait()   

        self.play(m.Create(m.Vector([4, 0], color=m.YELLOW)), run_time=0.3)
        self.wait()   


class AddNotLinear(LinearTransformationScene_):
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


class NonLinearTransform(LinearTransformationScene_):
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


class Exp(NonLinearTransform):
    def construct(self):
        self.apply_complex_func(lambda z: np.exp(z))
        self.wait()   


class Square(NonLinearTransform):
    def construct(self):
        self.apply_complex_func(lambda z: 0.5*z**2)
        self.wait()   


class Crazy(NonLinearTransform):
    def construct(self):
        self.apply_complex_func(lambda z: np.sin(z)**2 + np.sinh(z))
        self.wait()   


class LT3D(ThreeDScene_):
    def create_matrix(self, np_matrix):
        m = m.Matrix(np_matrix)

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(m.UP + m.LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = m.GREEN,
        self.basis_j_color = m.RED,
        self.basis_k_color = m.GOLD

        M = np.array([
            [2, 2, -1],
            [-2, 1, 2],
            [3, 1, -0]
        ])

        axes = m.ThreeDAxes()
        axes.set_color(m.GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * m.DEGREES, theta=-45 * m.DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = m.Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)

        basis_vector_helper.to_corner(m.UP + m.RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = m.Cube(side_length=1, fill_color=m.BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(m.BLUE_E)

        i_vec = m.Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = m.Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = m.Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = m.Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = m.Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = m.Vector(M @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            m.Create(cube),
            m.GrowArrow(i_vec),
            m.GrowArrow(j_vec),
            m.GrowArrow(k_vec),
            m.Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = m.ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            m.Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            m.Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            m.Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)


class LT3D_scale1(m.ThreeDScene):
    def create_matrix(self, np_matrix):
        m = m.Matrix(np_matrix)

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(m.UP + m.LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = m.GREEN,
        self.basis_j_color = m.RED,
        self.basis_k_color = m.GOLD

        M = np.array([
            [2, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])

        axes = m.ThreeDAxes()
        axes.set_color(m.GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * m.DEGREES, theta=-45 * m.DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = m.Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)

        basis_vector_helper.to_corner(m.UP + m.RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = m.Cube(side_length=1, fill_color=m.BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(m.BLUE_E)

        i_vec = m.Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = m.Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = m.Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = m.Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = m.Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = m.Vector(M @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            m.Create(cube),
            m.GrowArrow(i_vec),
            m.GrowArrow(j_vec),
            m.GrowArrow(k_vec),
            m.Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = m.ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            m.Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            m.Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            m.Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)


class LT3D_scale2(m.ThreeDScene):
    def create_matrix(self, np_matrix):
        m = m.Matrix(np_matrix)

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(m.UP + m.LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = m.GREEN,
        self.basis_j_color = m.RED,
        self.basis_k_color = m.GOLD

        M = np.array([
            [2, 0, 0],
            [0, 1, 0],
            [0, 0, 2.5]
        ])

        axes = m.ThreeDAxes()
        axes.set_color(m.GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * m.DEGREES, theta=-45 * m.DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = m.Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)

        basis_vector_helper.to_corner(m.UP + m.RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = m.Cube(side_length=1, fill_color=m.BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(m.BLUE_E)

        i_vec = m.Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = m.Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = m.Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = m.Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = m.Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = m.Vector(M @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            m.Create(cube),
            m.GrowArrow(i_vec),
            m.GrowArrow(j_vec),
            m.GrowArrow(k_vec),
            m.Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = m.ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            m.Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            m.Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            m.Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)


class LT3D_scale2_down(m.ThreeDScene):
    def create_matrix(self, np_matrix):
        m = m.Matrix(np_matrix)

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(m.UP + m.LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = m.GREEN,
        self.basis_j_color = m.RED,
        self.basis_k_color = m.GOLD

        M = np.array([
            [2, 0, 0],
            [0, 1, 0],
            [0, 0, 0.3]
        ])

        axes = m.ThreeDAxes()
        axes.set_color(m.GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * m.DEGREES, theta=-45 * m.DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = m.Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)

        basis_vector_helper.to_corner(m.UP + m.RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = m.Cube(side_length=1, fill_color=m.BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(m.BLUE_E)

        i_vec = m.Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = m.Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = m.Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = m.Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = m.Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = m.Vector(M @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            m.Create(cube),
            m.GrowArrow(i_vec),
            m.GrowArrow(j_vec),
            m.GrowArrow(k_vec),
            m.Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = m.ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            m.Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            m.Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            m.Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)


class LT3D_scale2_reversed(m.ThreeDScene):
    def create_matrix(self, np_matrix):
        m = m.Matrix(np_matrix)

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(m.UP + m.LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = m.GREEN,
        self.basis_j_color = m.RED,
        self.basis_k_color = m.GOLD

        M = np.array([
            [2, 0, 0],
            [0, 1, 0],
            [0, 0, -1.5]
        ])

        axes = m.ThreeDAxes()
        axes.set_color(m.GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * m.DEGREES, theta=-45 * m.DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = m.Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)

        basis_vector_helper.to_corner(m.UP + m.RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = m.Cube(side_length=1, fill_color=m.BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(m.BLUE_E)

        i_vec = m.Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = m.Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = m.Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = m.Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = m.Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = m.Vector(M @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            m.Create(cube),
            m.GrowArrow(i_vec),
            m.GrowArrow(j_vec),
            m.GrowArrow(k_vec),
            m.Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = m.ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            m.Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            m.Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            m.Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)


class LT3D_Shift(m.ThreeDScene):
    def create_matrix(self, np_matrix):
        m = m.Matrix(np_matrix)

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(m.UP + m.LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = m.GREEN,
        self.basis_j_color = m.RED,
        self.basis_k_color = m.GOLD

        M = np.array([
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0]
        ])

        axes = m.ThreeDAxes()
        axes.set_color(m.GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * m.DEGREES, theta=-45 * m.DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = m.Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)

        basis_vector_helper.to_corner(m.UP + m.RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = m.Cube(side_length=1, fill_color=m.BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(m.BLUE_E)

        i_vec = m.Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = m.Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = m.Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = m.Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = m.Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = m.Vector(M @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            m.Create(cube),
            m.GrowArrow(i_vec),
            m.GrowArrow(j_vec),
            m.GrowArrow(k_vec),
            m.Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = m.ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            m.Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            m.Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            m.Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)


class LT3D_Upper(m.ThreeDScene):
    def create_matrix(self, np_matrix):
        m = m.Matrix(np_matrix)

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(m.UP + m.LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = m.GREEN,
        self.basis_j_color = m.RED,
        self.basis_k_color = m.GOLD

        M = np.array([
            [1, -1, 1],
            [0, 1, 1],
            [0, 0, 1]
        ])

        axes = m.ThreeDAxes()
        axes.set_color(m.GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * m.DEGREES, theta=-45 * m.DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = m.Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)

        basis_vector_helper.to_corner(m.UP + m.RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = m.Cube(side_length=1, fill_color=m.BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(m.BLUE_E)

        i_vec = m.Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = m.Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = m.Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = m.Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = m.Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = m.Vector(M @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            m.Create(cube),
            m.GrowArrow(i_vec),
            m.GrowArrow(j_vec),
            m.GrowArrow(k_vec),
            m.Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = m.ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            m.Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            m.Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            m.Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)


class LT3d22d(m.ThreeDScene):
    def create_matrix(self, np_matrix):
        m = m.Matrix(np_matrix[:2,:])

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(m.UP + m.LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = m.GREEN,
        self.basis_j_color = m.RED,
        self.basis_k_color = m.GOLD

        M = np.array([
            [2, 2, -1],
            [-2, 1, 2],
            [0, 0, 0]
        ])

        axes = m.ThreeDAxes()
        axes.set_color(m.GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * m.DEGREES, theta=-45 * m.DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = m.Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)

        basis_vector_helper.to_corner(m.UP + m.RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)
        times = m.Tex(r"$\times$").scale(0.75).next_to(matrix, m.RIGHT)
        vector = m.Matrix(np.array([[1, 1, 1]]).T)
        vector.scale(0.75)
        vector.next_to(times, m.RIGHT)

        self.add_fixed_in_frame_mobjects(matrix)
        self.add_fixed_in_frame_mobjects(times)
        self.add_fixed_in_frame_mobjects(vector)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        i_vec = m.Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = m.Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = m.Vector(np.array([0, 0, 1]), color=self.basis_k_color)
        x_vec = m.Vector(np.array([1, 1, 1]), color=m.WHITE)

        i_vec_new = m.Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = m.Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = m.Vector(M @ np.array([0, 0, 1]), color=self.basis_k_color)
        x_vec_new = m.Vector(M @ np.array([1, 1, 1]), color=m.WHITE)

        self.play(
            m.GrowArrow(i_vec),
            m.GrowArrow(j_vec),
            m.GrowArrow(k_vec),
            m.GrowArrow(x_vec),
            m.Write(basis_vector_helper)
        )

        self.wait()

        self.play(
            m.Transform(i_vec, i_vec_new, run_time=1),
            m.Transform(j_vec, j_vec_new, run_time=1),
            m.Transform(k_vec, k_vec_new, run_time=1),
            m.Transform(x_vec, x_vec_new, run_time=1)
        )

        self.wait(2)

        # self.set_camera_orientation(phi=0 * m.DEGREES, theta=0 * m.DEGREES, zoom=1, run_time=2)
        self.move_camera(phi=0 * m.DEGREES, theta=-90 * m.DEGREES, run_time =2)
        self.stop_ambient_camera_rotation()

        eq = m.Tex(r"=").scale(0.75).next_to(vector, m.RIGHT)
        res = (M @ np.array([1, 1, 1]).reshape((-1, 1)))[:2,:]
        print(res)
        res = m.Matrix(res).scale(0.75).next_to(eq, m.RIGHT)
        
        i_label = i_vec_new.coordinate_label(n_dim=2, integer_labels=False, color=self.basis_i_color)
        j_label = j_vec_new.coordinate_label(n_dim=2, integer_labels=False, color=self.basis_j_color)
        k_label = k_vec_new.coordinate_label(n_dim=2, integer_labels=False, color=self.basis_k_color)
        res_label = x_vec_new.coordinate_label(n_dim=2, integer_labels=False)

        self.play(
            m.Create(eq),
            m.Create(res),
            m.Create(i_label),
            m.Create(j_label),
            m.Create(k_label),
            m.Create(res_label),
        )

        self.wait(1)


class LT2d23d(m.ThreeDScene):
    def create_matrix(self, np_matrix):
        m = m.Matrix(np_matrix[:,:2])

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(m.UP + m.LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = m.GREEN,
        self.basis_j_color = m.RED,
        self.basis_k_color = m.GOLD

        M = np.array([
            [2, 1, 0],
            [-2, 1, 0],
            [2, -1, 0]
        ])

        axes = m.ThreeDAxes()
        axes.set_color(m.GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=0 * m.DEGREES, theta=-90 * m.DEGREES)

        # matrix
        matrix = self.create_matrix(M)
        times = m.Tex(r"$\times$").scale(0.75).next_to(matrix, m.RIGHT)
        vector = m.Matrix(np.array([[1, 1]]).T)
        vector.scale(0.75)
        vector.next_to(times, m.RIGHT)

        self.add_fixed_in_frame_mobjects(matrix)
        self.add_fixed_in_frame_mobjects(times)
        self.add_fixed_in_frame_mobjects(vector)

        # axes & camera
        self.add(axes)

        i_vec = m.Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = m.Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        x_vec = m.Vector(np.array([1, 1, 0]), color=m.WHITE)

        i_vec_new = m.Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = m.Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        x_vec_new = m.Vector(M @ np.array([1, 1, 0]), color=m.WHITE)

        self.play(
            m.GrowArrow(i_vec),
            m.GrowArrow(j_vec),
            m.GrowArrow(x_vec),
        )

        self.wait()

        self.play(
            m.Transform(i_vec, i_vec_new, run_time=1),
            m.Transform(j_vec, j_vec_new, run_time=1),
            m.Transform(x_vec, x_vec_new, run_time=1)
        )

        eq = m.Tex(r"=").scale(0.75).next_to(vector, m.RIGHT)
        res = (M @ np.array([1, 1, 1]).reshape((-1, 1)))
        print(res)
        res = m.Matrix(res).scale(0.75).next_to(eq, m.RIGHT)
        
        i_label = i_vec_new.coordinate_label(n_dim=3, integer_labels=False, color=self.basis_i_color)
        j_label = j_vec_new.coordinate_label(n_dim=3, integer_labels=False, color=self.basis_j_color)
        res_label = x_vec_new.coordinate_label(n_dim=3, integer_labels=False)
        self.add_fixed_orientation_mobjects(i_label)
        self.add_fixed_orientation_mobjects(j_label)
        self.add_fixed_orientation_mobjects(res_label)

        self.move_camera(phi=75 * m.DEGREES, theta=-90 * m.DEGREES, run_time=2)
        self.begin_ambient_camera_rotation(rate=0.3)

        self.wait(10)

class LT2d21d(LinearTransformationScene_):
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
            [1.5, 1],
        ]
        vec_ = np.array([1, 2])

        self.matrix_text = m.Matrix(matrix).scale(1).to_edge(m.UP, buff=1).to_edge(m.LEFT)
        times = m.Tex(r"$\times$").scale(0.75).next_to(self.matrix_text, m.RIGHT)
        vector = m.Matrix(np.array([[1, 2]]).T)
        vector.scale(0.75)
        vector.next_to(times, m.RIGHT)
        self.play(m.Create(self.matrix_text), m.Create(times), m.Create(vector), run_time=0.3)
        self.wait()

        matrix = np.concat([matrix, np.array([[0, 0]])], axis=0)
        print(matrix)

        self.add_vector(vec := m.Vector(vec_))
        self.apply_matrix(matrix)
        self.wait()

        print(np.dot(matrix, vec_.T))
        vec = vec.become(m.Vector(np.dot(matrix, vec_.T)))
        label = vec.coordinate_label(integer_labels=False, n_dim=1).shift(m.UP * 0.5)
        self.play(m.Create(label), run_time=0.3)

        eq = m.Tex(r"=").scale(0.75).next_to(vector, m.RIGHT)
        res = np.dot(matrix, vec_.T).reshape((-1, 1))
        print(res)
        res = m.Matrix(res[:1,:]).scale(0.75).next_to(eq, m.RIGHT)
        self.play(m.Create(eq), m.Create(res), run_time=0.3)

        self.wait(2)

class LT2d21dreversed(LinearTransformationScene_):
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
            [1, 2],
        ]
        vec_ = np.array([1.5, 1])

        self.matrix_text = m.Matrix(matrix).scale(1).to_edge(m.UP, buff=1).to_edge(m.LEFT)
        times = m.Tex(r"$\times$").scale(0.75).next_to(self.matrix_text, m.RIGHT)
        vector = m.Matrix(np.array([[1.5, 2]]).T)
        vector.scale(0.75)
        vector.next_to(times, m.RIGHT)
        self.play(m.Create(self.matrix_text), m.Create(times), m.Create(vector), run_time=0.3)
        self.wait()

        matrix = np.concat([matrix, np.array([[0, 0]])], axis=0)
        print(matrix)

        self.add_vector(vec := m.Vector(vec_))
        self.apply_matrix(matrix)
        self.wait()

        print(np.dot(matrix, vec_.T))
        vec = vec.become(m.Vector(np.dot(matrix, vec_.T)))
        label = vec.coordinate_label(integer_labels=False, n_dim=1).shift(m.UP * 0.5)
        self.play(m.Create(label), run_time=0.3)

        eq = m.Tex(r"=").scale(0.75).next_to(vector, m.RIGHT)
        res = np.dot(matrix, vec_.T).reshape((-1, 1))
        print(res)
        res = m.Matrix(res[:1,:]).scale(0.75).next_to(eq, m.RIGHT)
        self.play(m.Create(eq), m.Create(res), run_time=0.3)

        self.wait(2)

class MatrixMatrixMul1(LinearTransformationScene_):
    def __init__(self, **kwargs):
        LinearTransformationScene_.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs
        )

    def apply_custom_matrix(self, matrix):
        matrix = np.array(matrix).T

        self.matrix_text = m.Matrix(matrix).scale(1).to_edge(m.UP, buff=1).to_edge(m.LEFT)
        self.play(m.Create(self.matrix_text), run_time=0.3)
        self.wait()

        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait()

        self.moving_mobjects = []
        self.apply_inverse(matrix)
        self.wait()

    def construct(self):
        matrix = [
            [1, -1],
            [2, 1]
        ]
        self.apply_custom_matrix(matrix)
        self.play(m.Uncreate(self.matrix_text), run_time=0.3)

        self.wait()
        matrix = [
            [-1, 1],
            [-2, -1]
        ]
        self.apply_custom_matrix(matrix)
        self.play(m.Uncreate(self.matrix_text), run_time=0.3)
        self.wait()

class MatrixMatrixMul2(LinearTransformationScene_):
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
            [1, -1],
            [2, 1]
        ]

        self.add_vector([1, 1])
        matrix = np.array(matrix).T

        matrix1_text = m.Matrix(matrix).scale(1).to_edge(m.UP, buff=1).to_edge(m.LEFT)
        self.play(m.Create(matrix1_text), run_time=0.3)
        self.wait()

        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait()

        self.play(m.Uncreate(matrix1_text), run_time=0.3)

        matrix = [
            [1, -1],
            [1, 0.5]
        ]
        matrix = np.array(matrix).T

        matrix2_text = m.Matrix(matrix).scale(1).to_edge(m.UP, buff=1).to_edge(m.LEFT)
        self.play(m.Create(matrix2_text), run_time=0.3)
        self.wait()

        self.apply_matrix(matrix)
        self.wait()

class MatrixMatrixMul(LinearTransformationScene_):
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
            [1, -1],
            [1, 0.5]
        ]

        self.add_vector([1, 1])
        matrix = np.array(matrix).T

        matrix1_text = m.Matrix(matrix).scale(1).to_edge(m.UP, buff=1).to_edge(m.LEFT)
        self.play(m.Create(matrix1_text), run_time=0.3)
        self.wait()

        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait()



        matrix = [
            [1, -1],
            [2, 1]
        ]

        self.play(m.Uncreate(matrix1_text), run_time=0.3)
        matrix = np.array(matrix).T

        matrix2_text = m.Matrix(matrix).scale(1).to_edge(m.UP, buff=1).to_edge(m.LEFT)
        self.play(m.Create(matrix2_text), run_time=0.3)
        self.wait()

        self.apply_matrix(matrix)
        self.wait()

class MatrixMatrixMulResult(LinearTransformationScene_):
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
            [1, -1],
            [1, 0.5]
        ]

        self.add_vector([1, 1])
        matrix = np.array(matrix).T

        matrix1_text = m.Matrix(matrix).to_edge(m.UP, buff=1).to_edge(m.LEFT).set_column_colors(m.GREEN, m.RED)
        self.play(m.Create(matrix1_text), run_time=0.3)
        self.wait()

        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait()

        i1 = m.Matrix([[1.0], [-1.0]]).set_column_colors(m.GREEN).move_to(1.5 * m.RIGHT + 2 * m.DOWN)
        j1 = m.Matrix([[1.0], [0.5]]).set_column_colors(m.RED).move_to(1.5 * m.RIGHT + 1 * m.UP)
        self.play(m.Create(i1), m.Create(j1), run_time=0.3)
        self.wait(3)
        self.play(m.Uncreate(i1), m.Uncreate(j1), run_time=0.3)

        matrix = [
            [1, -1],
            [2, 1]
        ]

        # self.play(m.Uncreate(matrix1_text), run_time=0.3)
        matrix = np.array(matrix).T

        matrix2_text = m.Matrix(matrix).to_edge(m.UP, buff=1).to_edge(m.LEFT)
        times = m.Tex(r"$\times$").next_to(matrix2_text, m.RIGHT)
        self.play(matrix1_text.animate.next_to(times, m.RIGHT))
        self.play(m.Create(matrix2_text), run_time=0.3)
        self.play(m.Create(times), run_time=0.3)
        self.wait(2)

        self.apply_matrix(matrix)

        i1 = m.Matrix([[-1.0], [-2.0]]).set_column_colors(m.GREEN).move_to(2 * m.LEFT + 2 * m.DOWN)
        j1 = m.Matrix([[2.0], [-0.5]]).set_column_colors(m.RED).move_to(3 * m.RIGHT + 0.5 * m.DOWN)
        self.play(m.Create(i1), m.Create(j1), run_time=0.3)

        eq = m.Text("=").next_to(matrix1_text, m.RIGHT)
        matrix3_text = m.Matrix([[-1.0, 2.0], [-2.0, -0.5]]).next_to(eq, m.RIGHT).set_column_colors(m.GREEN, m.RED)
        self.play(m.Create(eq), m.Create(matrix3_text), run_time=0.3)

        self.wait()

class MatrixMatrixMulNotSymmetrical(LinearTransformationScene_):
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
            [1, -1],
            [2, 1]
        ]

        self.add_vector([1, 1])
        matrix = np.array(matrix).T

        matrix1_text = m.Matrix(matrix).to_edge(m.UP, buff=1).to_edge(m.LEFT).set_column_colors(m.GREEN, m.RED)
        self.play(m.Create(matrix1_text), run_time=0.3)
        self.wait()

        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait()

        i1 = m.Matrix([[1], [-1]]).set_column_colors(m.GREEN).move_to(2 * m.RIGHT + 1 * m.DOWN)
        j1 = m.Matrix([[2], [1]]).set_column_colors(m.RED).move_to(3 * m.RIGHT + 1 * m.UP)
        self.play(m.Create(i1), m.Create(j1), run_time=0.3)
        self.wait(3)
        self.play(m.Uncreate(i1), m.Uncreate(j1), run_time=0.3)

        matrix = [
            [1, -1],
            [1, 0.5]
        ]

        matrix = np.array(matrix).T

        matrix2_text = m.Matrix(matrix).to_edge(m.UP, buff=1).to_edge(m.LEFT)
        times = m.Tex(r"$\times$").next_to(matrix2_text, m.RIGHT)
        self.play(matrix1_text.animate.next_to(times, m.RIGHT))
        self.play(m.Create(matrix2_text), run_time=0.3)
        self.play(m.Create(times), run_time=0.3)
        self.wait(2)

        self.apply_matrix(matrix)

        i1 = m.Matrix([[0.0], [-1.0]]).set_column_colors(m.GREEN).move_to(1 * m.LEFT + 1 * m.DOWN)
        j1 = m.Matrix([[3.0], [-1.0]]).set_column_colors(m.RED).move_to(4 * m.RIGHT + 1 * m.DOWN)
        self.play(m.Create(i1), m.Create(j1), run_time=0.3)

        eq = m.Text("=").next_to(matrix1_text, m.RIGHT)
        matrix3_text = m.Matrix([[0.0, 3.0], [-1.0, -1.0]]).next_to(eq, m.RIGHT).set_column_colors(m.GREEN, m.RED)
        self.play(m.Create(eq), m.Create(matrix3_text), run_time=0.3)

        self.wait()

class LUDdecomposition(m.Scene):
    def construct(self):
        # Заголовок
        title = m.Text("LU-разложение матрицы", font_size=48)
        self.play(m.Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(m.UP))
        self.wait(0.5)

        # Исходная матрица A
        A_matrix = [
            [4, 3, 2],
            [6, 5, 4],
            [8, 7, 9]
        ]
        A = m.Matrix(A_matrix, element_alignment_corner=m.DR, bracket_h_buff=0.2)
        A_label = m.MathTex("A = ").next_to(A, m.LEFT)
        A_group = m.VGroup(A_label, A).move_to(m.ORIGIN)
        self.play(m.Write(A_group))
        self.wait(2)

        # Пояснение: что такое LU-разложение
        explanation = m.Text(
            "LU-разложение: A = L * U\n"
            "L — нижняя треугольная матрица (единичная диагональ)\n"
            "U — верхняя треугольная матрица",
            font_size=30, line_spacing=1.5
        )
        explanation.next_to(A_group, m.DOWN, buff=1)
        self.play(m.Write(explanation))
        self.wait(3)
        self.play(m.FadeOut(explanation))

        # Начальные матрицы L (единичная) и U (копия A)
        n = len(A_matrix)
        L_matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        U_matrix = [row[:] for row in A_matrix]

        # Отображаем L и U
        L = m.Matrix(L_matrix, element_alignment_corner=m.DR, bracket_h_buff=0.2)
        U = m.Matrix(U_matrix, element_alignment_corner=m.DR, bracket_h_buff=0.2)
        L_label = m.MathTex("L = ").next_to(L, m.LEFT)
        U_label = m.MathTex("U = ").next_to(U, m.LEFT)
        L_group = m.VGroup(L_label, L)
        U_group = m.VGroup(U_label, U)
        L_group.move_to(m.LEFT * 3.5)
        U_group.move_to(m.RIGHT * 3.5)
        self.play(m.Write(L_group), m.Write(U_group))
        self.wait(2)

        # Пояснение: прямой ход метода Гаусса
        elimination_text = m.Text("Прямой ход метода Гаусса:\nобнуляем элементы ниже главной диагонали", font_size=28)
        elimination_text.next_to(A_group, m.DOWN, buff=1)
        self.play(m.Write(elimination_text))
        self.wait(2)

        # Процесс исключения: для каждого столбца
        for k in range(n - 1):  # текущий столбец
            # Обнуляем элементы в столбце k ниже диагонали
            for i in range(k + 1, n):
                multiplier = U_matrix[i][k] / U_matrix[k][k]
                # Запоминаем множитель в L
                L_matrix[i][k] = multiplier
                # Обновляем строку i матрицы U: U[i] = U[i] - multiplier * U[k]
                for j in range(k, n):
                    U_matrix[i][j] -= multiplier * U_matrix[k][j]

                # Анимация: выделяем строки и показываем множитель
                # Получаем координаты элементов матрицы U
                u_entries = U.get_entries()
                # Подсвечиваем строку k (опорную) и строку i
                self.play(
                    u_entries[k * n : (k+1) * n].animate.set_color(m.YELLOW),
                    u_entries[i * n : (i+1) * n].animate.set_color(m.RED),
                    run_time=0.5
                )
                mult_tex = m.MathTex(f"\\text{{Scalar: }} l_{{{i+1}{k+1}}} = {multiplier:.2f}").scale(0.8)
                mult_tex.next_to(U_group, m.DOWN, buff=0.5)
                self.play(m.Write(mult_tex))
                self.wait(1)
                self.play(m.FadeOut(mult_tex))

                # Обновляем матрицы на экране
                new_U = m.Matrix(U_matrix, element_alignment_corner=m.DR, bracket_h_buff=0.2)
                new_U.move_to(U_group, aligned_edge=m.LEFT)
                U_group.become(m.VGroup(U_label, new_U))
                self.play(m.Transform(U_group, U_group), run_time=0.5)

                new_L = m.Matrix(L_matrix, element_alignment_corner=m.DR, bracket_h_buff=0.2)
                new_L.move_to(L_group, aligned_edge=m.LEFT)
                L_group.become(m.VGroup(L_label, new_L))
                self.play(m.Transform(L_group, L_group), run_time=0.5)

                self.wait(1)

            # После обнуления столбца снимаем подсветку
            all_entries = U_group[1].get_entries()
            self.play(all_entries.animate.set_color(m.WHITE), run_time=0.5)

        self.wait(1)
        self.play(m.FadeOut(elimination_text))

        # Финальный результат: показываем, что A = L * U
        product_text = m.MathTex("A = L \\times U").scale(0.9)
        product_text.next_to(m.VGroup(L_group, U_group), m.DOWN, buff=1)
        self.play(m.Write(product_text))
        self.wait(2)

        # Проверка: вычисляем произведение L*U и сравниваем с A (чисто визуально)
        # Создаём матрицу произведения для демонстрации
        product_matrix = [[sum(L_matrix[i][k] * U_matrix[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        product = m.Matrix(product_matrix, element_alignment_corner=m.DR, bracket_h_buff=0.2)
        product_label = m.MathTex("L \\times U = ").next_to(product, m.LEFT)
        product_group = m.VGroup(product_label, product)
        product_group.next_to(product_text, m.DOWN, buff=0.8)
        self.play(m.Write(product_group))
        self.wait(2)

        # Сравниваем с исходной A (можно показать, что они равны)
        equal_text = m.MathTex("\\text{Equals to} A").scale(0.7)
        equal_text.next_to(product_group, m.DOWN, buff=0.5)
        self.play(m.Write(equal_text))
        self.wait(3)

        # Заключение
        conclusion = m.Text(
            "LU-разложение позволяет эффективно решать системы уравнений\n"
            "и вычислять определители",
            font_size=28, line_spacing=1.2
        )
        conclusion.next_to(equal_text, m.DOWN, buff=1)
        self.play(m.Write(conclusion))
        self.wait(3)

        # Финальная задержка
        self.wait(2)


if __name__ == '__main__':
    import os
    from pathlib import Path

    SCENES = [
        "LTExample",
        "LT3D",
        "LT2d23d",
        "LT3d22d",
        "LT2d21d",
        "LT2d21dreversed",
        "MatrixMatrixMul3",
        "MatrixMatrixMulResult",
        "MatrixMatrixMulNotSymmetrical",
        "LT3D_scale1",
        "LT3D_scale2",
        "LT3D_scale2_down",
        "LT3D_scale2_reversed",
    ]
    file_path = Path(__file__).resolve()

    for SCENE in SCENES:
        os.system(f"manim {Path(__file__).resolve()} {SCENE} -fqh")
        os.system(f"manim {Path(__file__).resolve()} {SCENE} -s")