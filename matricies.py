import manim as m
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
        mat = m.Matrix(np_matrix)

        mat.scale(0.75)
        mat.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        mat.to_corner(m.UP + m.LEFT,buff=0.5)

        return mat

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


class LT3D_scale1(ThreeDScene_):
    def create_matrix(self, np_matrix):
        mat = m.Matrix(np_matrix)

        mat.scale(0.75)
        mat.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        mat.to_corner(m.UP + m.LEFT,buff=0.5)

        return mat

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


class LT3D_scale2(ThreeDScene_):
    def create_matrix(self, np_matrix):
        mat = m.Matrix(np_matrix)

        mat.scale(0.75)
        mat.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        mat.to_corner(m.UP + m.LEFT,buff=0.5)

        return mat

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


class LT3D_scale2_down(ThreeDScene_):
    def create_matrix(self, np_matrix):
        mat = m.Matrix(np_matrix)

        mat.scale(0.75)
        mat.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        mat.to_corner(m.UP + m.LEFT,buff=0.5)

        return mat

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


class LT3D_scale2_reversed(ThreeDScene_):
    def create_matrix(self, np_matrix):
        mat = m.Matrix(np_matrix)

        mat.scale(0.75)
        mat.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        mat.to_corner(m.UP + m.LEFT,buff=0.5)

        return mat

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = m.GREEN,
        self.basis_j_color = m.RED,
        self.basis_k_color = m.GOLD

        Mat = np.array([
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
        matrix = self.create_matrix(Mat)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = m.Cube(side_length=1, fill_color=m.BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(m.BLUE_E)

        i_vec = m.Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = m.Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = m.Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = m.Vector(Mat @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = m.Vector(Mat @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = m.Vector(Mat @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            m.Create(cube),
            m.GrowArrow(i_vec),
            m.GrowArrow(j_vec),
            m.GrowArrow(k_vec),
            m.Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = m.ApplyMatrix(Mat, cube)

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



class LT3D_Shift(ThreeDScene_):
    def create_matrix(self, np_matrix):
        mat = mat.Matrix(np_matrix)

        mat.scale(0.75)
        mat.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        mat.to_corner(m.UP + m.LEFT,buff=0.5)

        return mat

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = m.GREEN,
        self.basis_j_color = m.RED,
        self.basis_k_color = m.GOLD

        Mat = np.array([
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
        matrix = self.create_matrix(Mat)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = m.Cube(side_length=1, fill_color=m.BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(m.BLUE_E)

        i_vec = m.Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = m.Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = m.Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = m.Vector(Mat @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = m.Vector(Mat @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = m.Vector(Mat @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            m.Create(cube),
            m.GrowArrow(i_vec),
            m.GrowArrow(j_vec),
            m.GrowArrow(k_vec),
            m.Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = m.ApplyMatrix(Mat, cube)

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


class LT3D_Upper(ThreeDScene_):
    def create_matrix(self, np_matrix):
        mat = m.Matrix(np_matrix)

        mat.scale(0.75)
        mat.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        mat.to_corner(m.UP + m.LEFT,buff=0.5)

        return mat

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = m.GREEN,
        self.basis_j_color = m.RED,
        self.basis_k_color = m.GOLD

        Mat = np.array([
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
        matrix = self.create_matrix(Mat)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = m.Cube(side_length=1, fill_color=m.BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(m.BLUE_E)

        i_vec = m.Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = m.Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = m.Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = m.Vector(Mat @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = m.Vector(Mat @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = m.Vector(Mat @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            m.Create(cube),
            m.GrowArrow(i_vec),
            m.GrowArrow(j_vec),
            m.GrowArrow(k_vec),
            m.Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = m.ApplyMatrix(Mat, cube)

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


class LT3d22d(ThreeDScene_):
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

        Mat = np.array([
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
        matrix = self.create_matrix(Mat)
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

        i_vec_new = m.Vector(Mat @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = m.Vector(Mat @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = m.Vector(Mat @ np.array([0, 0, 1]), color=self.basis_k_color)
        x_vec_new = m.Vector(Mat @ np.array([1, 1, 1]), color=m.WHITE)

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
        res = (Mat @ np.array([1, 1, 1]).reshape((-1, 1)))[:2,:]
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


class LT2d23d(ThreeDScene_):
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

        Mat = np.array([
            [2, 1, 0],
            [-2, 1, 0],
            [2, -1, 0]
        ])

        axes = m.ThreeDAxes()
        axes.set_color(m.GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=0 * m.DEGREES, theta=-90 * m.DEGREES)

        # matrix
        matrix = self.create_matrix(Mat)
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

        i_vec_new = m.Vector(Mat @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = m.Vector(Mat @ np.array([0, 1, 0]), color=self.basis_j_color)
        x_vec_new = m.Vector(Mat @ np.array([1, 1, 0]), color=m.WHITE)

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
        res = (Mat @ np.array([1, 1, 1]).reshape((-1, 1)))
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

class MatrixDeterminantScene(LinearTransformationScene_):
    def __init__(self, **kwargs):
        LinearTransformationScene_.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            show_basis_vectors=True,
            **kwargs
        )

    def construct(self):
        self.remove(self.plane)
        self.plane = m.NumberPlane(
            x_range=[-4, 4, 1], y_range=[-4, 4, 1],
            background_line_style={"stroke_color": m.GRAY_E, "stroke_width": 1}
        )
        self.add(self.plane)
        self.add_transformable_mobject(self.plane)

        title = m.Text("Геометрический смысл определителя", font_size=32).to_edge(m.UP)
        self.add(title)

        A1 = np.array([[2, 1], [1, 2]])
        det1 = 3.0

        m1_tex = m.Matrix(A1).to_edge(m.UP, buff=1).to_edge(m.LEFT)
        self.play(m.Create(m1_tex), run_time=0.5)

        det1_eq = m.MathTex(r"\det(A_1) = 2 \cdot 2 - 1 \cdot 1 = 3").next_to(m1_tex, m.RIGHT, buff=0.5)
        det1_eq.set_color(m.DARK_GRAY)
        self.play(m.Write(det1_eq), run_time=0.5)
        self.wait(0.5)

        unit_sq1 = m.Polygon(
            [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
            fill_color=m.PURPLE, fill_opacity=0.4, stroke_color=m.PURPLE, stroke_width=2
        )
        self.add(unit_sq1)
        self.add_transformable_mobject(unit_sq1)
        self.wait(0.5)

        self.apply_matrix(A1)
        self.wait(0.5)

        area1 = m.Text(f"Площадь = {det1:.0f}", font_size=28).next_to(det1_eq, m.DOWN, buff=0.3)
        area1.set_color(m.PURPLE)
        self.play(m.Write(area1), run_time=0.5)
        self.wait(1.5)

        self.play(
            m.FadeOut(unit_sq1), m.FadeOut(area1),
            m.FadeOut(det1_eq), m.FadeOut(m1_tex),
            run_time=0.5
        )

        self.remove(self.plane)
        self.plane = m.NumberPlane(
            x_range=[-4, 4, 1], y_range=[-4, 4, 1],
            background_line_style={"stroke_color": m.GRAY_E, "stroke_width": 1}
        )
        self.add(self.plane)
        self.add_transformable_mobject(self.plane)
        self.wait(0.3)

        A2 = np.array([[0, 1], [1, 0]])
        det2 = -1.0

        m2_tex = m.Matrix(A2).to_edge(m.UP, buff=1).to_edge(m.LEFT)
        self.play(m.Create(m2_tex), run_time=0.5)

        det2_eq = m.MathTex(r"\det(A_2) = 0 \cdot 0 - 1 \cdot 1 = -1").next_to(m2_tex, m.RIGHT, buff=0.5)
        det2_eq.set_color(m.DARK_GRAY)
        self.play(m.Write(det2_eq), run_time=0.5)
        self.wait(0.5)

        unit_sq2 = m.Polygon(
            [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
            fill_color=m.PURPLE, fill_opacity=0.4, stroke_color=m.PURPLE, stroke_width=2
        )
        self.add(unit_sq2)
        self.add_transformable_mobject(unit_sq2)
        self.wait(0.5)

        self.apply_matrix(A2)
        self.wait(0.5)

        area2 = m.Text(f"Площадь = |{det2:.0f}| = 1  (смена ориентации)", font_size=24).next_to(det2_eq, m.DOWN, buff=0.3)
        area2.set_color(m.PURPLE)
        self.play(m.Write(area2), run_time=0.5)
        self.wait(1.5)

        conclusion = m.Text(
            "Определитель = коэффициент масштабирования площади\n(знак указывает на ориентацию базиса)",
            font_size=26, color=m.DARK_GRAY
        ).to_edge(m.DOWN)
        self.play(m.Write(conclusion), run_time=1)
        self.wait(2)

class DegenerateVolume3D(ThreeDScene_):
    '''Трёхмерное пространство. Три вектора-столбца матрицы A выходят из начала координат. Поскольку они
линейно зависимы, все три лежат в одной плоскости — параллелепипед вырожден, объём равен нулю. Плоскость, в
которой лежат все три вектора, подсвечена полупрозрачным цветом. '''
    def construct(self):
        # Настройка цветов по гайду
        self.basis_color = m.PURPLE
        self.axis_color = m.GRAY
        self.text_color = m.DARK_GRAY

        # Матрица с линейно зависимыми столбцами
        M = np.array([
            [2.0, 0.0, 2.0],
            [0.0, 2.0, 2.0],
            [1.0, 1.0, 2.0]
        ])

        # Оси координат и подписи
        axes = m.ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3], z_range=[-3, 3])
        axes.set_color(self.axis_color)
        axes.add(axes.get_axis_labels())
        self.add(axes)

        # Камера и автоматическое вращение
        self.set_camera_orientation(phi=75 * m.DEGREES, theta=-45 * m.DEGREES)
        self.begin_ambient_camera_rotation(rate=0.15)

        # Извлечение векторов-столбцов
        v1, v2, v3 = M[:, 0], M[:, 1], M[:, 2]

        # Плоскость, натянутая на первые два вектора
        plane = m.Surface(
            lambda u, v: u * v1 + v * v2,
            u_range=[-1.4, 1.4], v_range=[-1.4, 1.4],
            resolution=(12, 12)
        )
        plane.set_fill(self.basis_color, opacity=0.15)
        plane.set_stroke(self.basis_color, width=2, opacity=0.5)
        plane.set_shade_in_3d(True)

        # 3D-стрелки (без явного указания tip_length для совместимости)
        # Arrow3D гарантирует, что стержень и наконечник всегда соединены геометрически
        vec1 = m.Arrow3D(start=m.ORIGIN, end=v1, color=self.basis_color)
        vec2 = m.Arrow3D(start=m.ORIGIN, end=v2, color=self.basis_color)
        vec3 = m.Arrow3D(start=m.ORIGIN, end=v3, color=self.basis_color)

        # Анимация появления плоскости и векторов
        self.play(
            m.FadeIn(plane, run_time=1.5),
            m.Create(vec1, run_time=0.5),
            m.Create(vec2, run_time=0.5),
            m.Create(vec3, run_time=0.5)
        )
        self.wait(1)

        # Матрица на сцене (зафиксирована в 2D-пространстве камеры)
        mat = m.Matrix(M).scale(0.75)
        mat.set_column_colors(self.basis_color, self.basis_color, self.basis_color)
        mat.to_corner(m.UP + m.LEFT, buff=0.5)
        mat.shift(m.DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(mat)
        self.play(m.Create(mat, run_time=0.5))

        # Подписи временно отключены
        self.wait(4)

class MatrixDeterminantGeometry(LinearTransformationScene_):
    """
    Геометрический смысл определителя
    
    Иллюстрация концепции:
    1. Столбцы матрицы A — это два вектора на плоскости.
    2. Модуль определителя |det(A)| равен площади параллелограмма, 
       построенного на этих векторах.
    3. Знак определителя показывает ориентацию:
       - det > 0: сохраняется «правая» ориентация (зелёный вектор → красный против часовой)
       - det < 0: ориентация меняется на «левую» (зелёный вектор → красный по часовой)
    """

    def __init__(self, **kwargs):
        LinearTransformationScene_.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            show_basis_vectors=False,
            **kwargs
        )

    def construct(self):
        # Хелпер для создания сплошных белых подложек
        def add_white_bg(mob):
            bg = m.BackgroundRectangle(mob, fill_color="#FFFFFF", fill_opacity=0.8, stroke_width=0)
            self.add(bg)
            return bg

        # --- Пример 1: Положительный определитель ---
        A = np.array([[3, 1], [0, 2]])
        v1, v2 = [3.0, 0.0], [1.0, 2.0]  # Явные списки для избежания numpy-конфликтов в Polygon

        mat_A = m.Matrix(A).to_edge(m.UP, buff=1).to_edge(m.LEFT).set_column_colors(m.GREEN, m.RED)
        bg_mat_A = add_white_bg(mat_A)
        self.play(m.Create(mat_A), run_time=0.5)

        # 1. Показываем векторы
        arrow1 = m.Vector(v1, color=m.GREEN)
        arrow2 = m.Vector(v2, color=m.RED)
        self.play(m.GrowArrow(arrow1), m.GrowArrow(arrow2), run_time=1)
        self.wait(0.5)

        # 2. Строим параллелограмм (точки как стандартные списки)
        poly_A_points = [
            [0, 0, 0],
            [v1[0], v1[1], 0],
            [v1[0] + v2[0], v1[1] + v2[1], 0],
            [v2[0], v2[1], 0]
        ]
        parallelogram_A = m.Polygon(
            *poly_A_points,
            fill_color=m.PURPLE, 
            fill_opacity=0.3, 
            stroke_color=m.PURPLE, 
            stroke_width=2
        )
        self.play(m.Create(parallelogram_A), run_time=1)
        self.wait(1)

        # 3. Вычисляем определитель и площадь (логичный вывод после геометрии)
        det_text_A = m.MathTex(r"\det(A) = 3 \cdot 2 - 1 \cdot 0 = 6", font_size=26).next_to(mat_A, m.DOWN, buff=0.5)
        det_text_A.set_color(m.DARK_GRAY)
        bg_det_A = add_white_bg(det_text_A)
        self.play(m.Write(det_text_A), run_time=0.5)

        area_text_A = m.Text("Площадь = 6", font_size=22).next_to(det_text_A, m.DOWN, buff=0.2)
        area_text_A.set_color(m.DARK_GRAY)
        bg_area_A = add_white_bg(area_text_A)
        self.play(m.Write(area_text_A), run_time=0.5)
        self.wait(2)

        # Очистка
        self.play(
            m.FadeOut(mat_A), m.FadeOut(bg_mat_A),
            m.FadeOut(det_text_A), m.FadeOut(bg_det_A),
            m.FadeOut(area_text_A), m.FadeOut(bg_area_A),
            m.FadeOut(arrow1), m.FadeOut(arrow2), m.FadeOut(parallelogram_A)
        )
        self.wait(0.5)

        # --- Пример 2: Отрицательный определитель ---
        B = np.array([[1, 2], [2, 1]])
        v1_b, v2_b = [1.0, 2.0], [2.0, 1.0]

        mat_B = m.Matrix(B).to_edge(m.UP, buff=1).to_edge(m.LEFT).set_column_colors(m.GREEN, m.RED)
        bg_mat_B = add_white_bg(mat_B)
        self.play(m.Create(mat_B), run_time=0.5)

        arrow1_b = m.Vector(v1_b, color=m.GREEN)
        arrow2_b = m.Vector(v2_b, color=m.RED)
        self.play(m.GrowArrow(arrow1_b), m.GrowArrow(arrow2_b), run_time=1)
        self.wait(0.5)

        poly_B_points = [
            [0, 0, 0],
            [v1_b[0], v1_b[1], 0],
            [v1_b[0] + v2_b[0], v1_b[1] + v2_b[1], 0],
            [v2_b[0], v2_b[1], 0]
        ]
        parallelogram_B = m.Polygon(
            *poly_B_points,
            fill_color=m.PURPLE, 
            fill_opacity=0.3, 
            stroke_color=m.PURPLE, 
            stroke_width=2
        )
        self.play(m.Create(parallelogram_B), run_time=1)
        self.wait(1)

        det_text_B = m.MathTex(r"\det(B) = 1 \cdot 1 - 2 \cdot 2 = -3", font_size=26).next_to(mat_B, m.DOWN, buff=0.5)
        det_text_B.set_color(m.DARK_GRAY)
        bg_det_B = add_white_bg(det_text_B)
        self.play(m.Write(det_text_B), run_time=0.5)

        area_text_B = m.Text("Площадь = 3", font_size=22).next_to(det_text_B, m.DOWN, buff=0.2)
        area_text_B.set_color(m.DARK_GRAY)
        bg_area_B = add_white_bg(area_text_B)
        self.play(m.Write(area_text_B), run_time=0.5)
        self.wait(3)



class DeterminantVolumeScaling3D(ThreeDScene_):
    """
    Определитель как масштабный коэффициент преобразования (3D)
    
    Иллюстрация концепции:
    1. Матрица A задаёт линейное преобразование пространства.
    2. Единичный куб (объём = 1) превращается в параллелепипед.
    3. Объём полученного параллелепипеда равен модулю определителя |det(A)|.
    4. Визуализируются три вектора-столбца матрицы как рёбра параллелепипеда.
    """
    def __init__(self, **kwargs):
        ThreeDScene_.__init__(self, **kwargs)

    def construct(self):
        # Цветовая схема столбцов как в LT3D
        self.basis_i_color = m.GREEN
        self.basis_j_color = m.RED
        self.basis_k_color = m.GOLD

        # Матрица преобразования (det = 6)
        A = np.array([
            [2, 1, 0],
            [1, 2, 0],
            [0, 0, 2]
        ])
        det_val = int(np.round(np.linalg.det(A)))

        # Оси и камера (стандартная настройка из LT3D)
        axes = m.ThreeDAxes(x_range=[-2, 5], y_range=[-2, 5], z_range=[-2, 5])
        axes.set_color(m.GRAY)
        axes.add(axes.get_axis_labels())
        self.add(axes)

        self.set_camera_orientation(phi=75 * m.DEGREES, theta=-45 * m.DEGREES)
        self.begin_ambient_camera_rotation(rate=0.15)

        # Единичный куб (вершины от 0 до 1 по всем осям)
        cube = m.Cube(
            side_length=1, 
            fill_color=m.BLUE, 
            fill_opacity=0.15, 
            stroke_color=m.BLUE_E, 
            stroke_width=1.5
        )
        cube.shift(0.5 * (m.RIGHT + m.UP + m.OUT))
        self.play(m.Create(cube), run_time=1)
        self.wait(0.5)

        # Матрица на экране (зафиксирована в 2D)
        mat = m.Matrix(A).scale(0.75)
        mat.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)
        mat.to_corner(m.UP + m.LEFT, buff=0.5)
        self.add_fixed_in_frame_mobjects(mat)
        self.play(m.Create(mat), run_time=0.5)
        self.wait(0.5)

        # Преобразование куба матрицей (нативный метод, без артефактов проекции)
        self.play(m.ApplyMatrix(A, cube), run_time=2)
        self.wait(1)

        # Векторы-столбцы матрицы (рёбра полученного параллелепипеда)
        v1, v2, v3 = A[:, 0], A[:, 1], A[:, 2]
        vec1 = m.Arrow3D(start=m.ORIGIN, end=v1, color=self.basis_i_color)
        vec2 = m.Arrow3D(start=m.ORIGIN, end=v2, color=self.basis_j_color)
        vec3 = m.Arrow3D(start=m.ORIGIN, end=v3, color=self.basis_k_color)

        self.play(
            m.Create(vec1, run_time=0.4),
            m.Create(vec2, run_time=0.4),
            m.Create(vec3, run_time=0.4)
        )
        self.wait(1)

        # Итоговая формула (разделена для совместимости с LaTeX)
        formula_math = m.MathTex(r"|\det(A)|", "=", str(det_val)).scale(0.8)
        formula_text = m.Text("= объём параллелепипеда", font_size=24, color=m.DARK_GRAY)
        formula = m.VGroup(formula_math, formula_text).arrange(m.RIGHT, buff=0.2)
        formula.to_corner(m.DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(formula)
        self.play(m.Write(formula), run_time=0.5)
        self.wait(3)



class DeterminantVolumeScale(m.ThreeDScene):
    # определитель трехмерной матрицы как объем параллелепипеда на ее векторах
    def create_matrix(self, np_matrix):
        mat = m.Matrix(np_matrix)
        mat.scale(0.75)
        
        # Исправление: Явно красим скобки в черный, чтобы они были видны на белом фоне
        if hasattr(mat, 'get_brackets'):
            mat.get_brackets().set_color(m.BLACK)
            
        # Применение цветов к столбцам (если метод доступен)
        if hasattr(mat, 'set_column_colors'):
            mat.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)
        mat.to_corner(m.UP + m.LEFT, buff=0.5)
        return mat

    def construct(self):
        # Установка белого фона
        self.camera.background_color = m.WHITE
        
        # Определение цветов
        self.basis_i_color = m.GREEN
        self.basis_j_color = m.RED
        self.basis_k_color = m.GOLD
        self.text_color = m.DARK_GRAY  # Серый цвет для текста

        # Матрица преобразования: 
        # Включает наклон (shear), чтобы показать параллелепипед, а не просто кубоид.
        # Определитель = 2 * 1 * 1.5 = 3.
        Mat = np.array([
            [2, 0, 0],
            [1, 1, 0],
            [0, 0, 1.5]
        ])

        # Начальная матрица (единичная)
        Id = np.eye(3)

        # Настройка 3D осей
        axes = m.ThreeDAxes()
        axes.set_color(m.GRAY)
        
        # Ориентация камеры
        self.set_camera_orientation(phi=75 * m.DEGREES, theta=-45 * m.DEGREES)

        # Текстовые обозначения базисных векторов
        basis_vector_helper = m.Tex(r"$\hat{i}$", r",", r"$\hat{j}$", r",", r"$\hat{k}$", color=self.text_color)
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)
        basis_vector_helper.to_corner(m.UP + m.RIGHT)
        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # Создание матриц (начальной и конечной)
        matrix_initial = self.create_matrix(Id)
        matrix_final = self.create_matrix(Mat)
        
        self.add_fixed_in_frame_mobjects(matrix_initial)

        self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.1)

        # Создание куба (единичный объем)
        cube = m.Cube(side_length=1, fill_color=m.BLUE, stroke_width=2, fill_opacity=0.2)
        # Сдвигаем куб так, чтобы его угол был в (0,0,0), а ребра совпадали с осями
        cube.shift(m.RIGHT * 0.5 + m.UP * 0.5 + m.OUT * 0.5) 
        cube.set_stroke(m.BLUE)

        # Исходные векторы
        i_vec = m.Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = m.Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = m.Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        # Трансформированные векторы
        i_vec_new = m.Vector(Mat @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = m.Vector(Mat @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = m.Vector(Mat @ np.array([0, 0, 1]), color=self.basis_k_color)

        # --- НАСТРОЙКА ТЕКСТА ---
        # Текст "Объём = 1": чуть меньше (0.8) и сдвинут выше/правее
        vol_text = m.Text("Объём = 1", color=self.text_color).scale(0.7)
        vol_text.next_to(cube, m.UP + m.RIGHT).shift(m.UP * 0.3 + m.RIGHT * 0.3)
        self.add_fixed_in_frame_mobjects(vol_text)

        # Текст "Объём = 3": еще меньше (0.7) и сдвинут выше/правее
        new_vol_text = m.Text("Объём = 3", color=self.text_color).scale(0.7)
        new_vol_text.next_to(cube, m.UP + m.RIGHT).shift(m.UP * 0.5 + m.RIGHT * 0.5)
        #self.add_fixed_in_frame_mobjects(new_vol_text)

        # Текст определителя
        det_info = m.Tex(r"$|\det(A)| = 3$", color=self.text_color).scale(0.8)
        det_info.next_to(new_vol_text, m.DOWN)
        #self.add_fixed_in_frame_mobjects(det_info)

        # Анимация появления куба и векторов
        self.play(
            m.Create(cube),
            m.GrowArrow(i_vec),
            m.GrowArrow(j_vec),
            m.GrowArrow(k_vec),
            m.Write(basis_vector_helper),
            m.Write(matrix_initial),
            m.Write(vol_text)
        )

        self.wait()

        # Анимация трансформации (куб, векторы, матрица)
        matrix_anim = m.ApplyMatrix(Mat, cube)

        self.play(
            matrix_anim,
            m.Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(), run_time=matrix_anim.get_run_time()),
            m.Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(), run_time=matrix_anim.get_run_time()),
            m.Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(), run_time=matrix_anim.get_run_time()),
            m.Transform(matrix_initial, matrix_final), 
            run_time=2.5
        )

        # Последовательное обновление текста:
        # 1. Исчезает "Объём = 1"
        self.play(m.FadeOut(vol_text, shift=m.UP), run_time=0.5)
        self.add_fixed_in_frame_mobjects(new_vol_text)
        self.add_fixed_in_frame_mobjects(det_info)
        # 2. Появляются "Объём = 3" и формула
        self.play(
            m.FadeIn(new_vol_text, shift=m.DOWN),
            m.FadeIn(det_info, shift=m.DOWN),
            run_time=0.8
        )
        self.wait(2)


class MatrixVectorMult(LinearTransformationScene_):
    '''рисуется 2D матрица в виде параллелепипеда. Матрица выводится на экран. Рисуется вектор. Выводится
вектор, показывается что он умножается на матрицу. Анимируется умножение матрицы на вектор. Результирующий вектор
показывается в формуле'''
    def __init__(self, **kwargs):
        LinearTransformationScene_.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            show_basis_vectors=False,  # Отключаем стандартный базис, чтобы не дублировался
            **kwargs
        )

    def construct(self):
        # 1. Подготовка данных
        mat_A = np.array([[1.5, 0.5], [-0.3, 2.5]])
        vec_x_2d = np.array([2, 1.5])
        
        # Столбцы матрицы (новые базисные векторы) в 3D
        col1 = np.append(mat_A[:, 0], 0)  # [1.5, -0.3, 0]
        col2 = np.append(mat_A[:, 1], 0)  # [0.5, 2.5, 0]
        
        # Результаты вычислений
        res_vec_3d = np.append(mat_A @ vec_x_2d, 0)
        vec_x_3d = np.append(vec_x_2d, 0)

        # Цветовая схема
        C_COL1 = m.GREEN
        C_COL2 = m.RED
        C_VEC  = m.PURPLE

        # --- ШАГ 1: Параллелограмм, векторы и матрица (появляются параллельно) ---
        
        # Два базисных вектора
        arrow_c1 = m.Arrow(m.ORIGIN, col1, color=C_COL1, buff=0)
        arrow_c2 = m.Arrow(m.ORIGIN, col2, color=C_COL2, buff=0)
        
        # Параллелограмм (полупрозрачный, чтобы векторы оставались сверху)
        parallelogram = m.Polygon(
            m.ORIGIN, col1.tolist(), (col1 + col2).tolist(), col2.tolist(),
            fill_color=m.GRAY, fill_opacity=0.2, stroke_color=m.DARK_GRAY, stroke_width=2
        )
        
        # Матрица с раскрашенными столбцами
        matrix_tex = m.Matrix(
            mat_A,
            element_to_mobject_config={"color": m.BLACK}
        ).scale(1).to_edge(m.UP, buff=1).to_edge(m.LEFT, buff=0.5)
        matrix_tex.get_columns()[0].set_color(C_COL1)
        matrix_tex.get_columns()[1].set_color(C_COL2)

        # Анимируем одновременное появление
        self.play(
            m.GrowArrow(arrow_c1),
            m.GrowArrow(arrow_c2),
            m.Create(parallelogram),
            m.Create(matrix_tex),
            run_time=2
        )
        self.wait(0.5)

        # --- ШАГ 2: Исходный вектор x ---
        arrow_x = m.Vector(vec_x_3d.tolist(), color=C_VEC, buff=0)
        self.play(m.GrowArrow(arrow_x), run_time=1)
        self.wait(0.5)

        # --- ШАГ 3: Анимация умножения (Линейная комбинация) ---
        # Убираем геометрию, чтобы освободить место для формул
        self.play(
            m.FadeOut(parallelogram),
            m.FadeOut(arrow_c1),
            m.FadeOut(arrow_c2),
            m.FadeOut(arrow_x),
            run_time=0.5
        )

        # Компонент 1: 2 * col1 (Зелёный)
        # Размещаем строго слева под матрицей
        comp1_end = (2 * col1).tolist()
        comp1 = m.Arrow(m.ORIGIN, comp1_end, color=C_COL1, buff=0)
        comp1_label = m.MathTex(
            r"2 \cdot \begin{bmatrix} 1.5 \\ -0.3 \end{bmatrix}", 
            color=C_COL1
        ).to_edge(m.LEFT, buff=0.5).shift(m.DOWN * 2)
        
        self.play(m.GrowArrow(comp1), m.Write(comp1_label), run_time=1.5)
        self.wait(0.5)
        
        # Компонент 2: 1.5 * col2 (Красный)
        comp2_start = comp1_end
        comp2_end = (comp1_end + 1.5 * col2).tolist()
        comp2 = m.Arrow(comp2_start, comp2_end, color=C_COL2, buff=0)
        comp2_label = m.MathTex(
            r"+ 1.5 \cdot \begin{bmatrix} 0.5 \\ 2.5 \end{bmatrix}", 
            color=C_COL2
        ).next_to(comp1_label, m.RIGHT, buff=0.4)
        
        self.play(m.GrowArrow(comp2), m.Write(comp2_label), run_time=1.5)
        self.wait(0.5)
        
        # --- ШАГ 4: Итоговый вектор и формула ---
        # Всё остаётся выровненным по левому краю
        res_arrow = m.Arrow(m.ORIGIN, res_vec_3d.tolist(), color=C_VEC, buff=0)
        res_label = m.MathTex(
            r"= \vec{x}' = \begin{bmatrix} 3.75 \\ 3.15 \end{bmatrix}", 
            color=m.BLACK
        ).next_to(comp2_label, m.RIGHT, buff=0.4)
        
        self.play(
            m.Create(res_arrow),
            m.Write(res_label),
            run_time=1.5
        )
        self.wait(2)

class RotationPlane2D(LinearTransformationScene_):
    """Анимация матрицы поворота на 30 и -45 градусов"""
    def __init__(self, **kwargs):
        LinearTransformationScene_.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            show_basis_vectors=False,
            **kwargs
        )

    def construct(self):
        # Фиолетовый вектор строго на оси X
        v_start = np.array([3, 0, 0])
        self.add_vector(v_start, color=m.PURPLE)
        self.wait(0.5)

        # Вспомогательная функция для создания матрицы
        def create_rot_matrix(c_val, s_val, angle_deg, symbolic=False):
            if symbolic:
                c_txt = rf"\cos({angle_deg}^\circ)"
                s_txt = rf"\sin({angle_deg}^\circ)"
                row1 = [c_txt, rf"-{s_txt}"]
                row2 = [s_txt, c_txt]
            else:
                c_txt = f"{c_val:.2f}"
                neg_s_txt = f"{-s_val:.2f}"
                s_txt = f"{s_val:.2f}"
                row1 = [c_txt, neg_s_txt]
                row2 = [s_txt, c_txt]

            mat = m.Matrix(
                [row1, row2],
                element_to_mobject_config={"font_size": 32, "color": m.DARK_GRAY}
            )
            cols = mat.get_columns()
            cols[0].shift(m.LEFT * 0.25)
            cols[1].shift(m.RIGHT * 0.25)
            mat.scale(1.1).to_edge(m.UP, buff=1).to_edge(m.LEFT)
            return mat

        # ================= ПОВОРОТ НА +30 ГРАДУСОВ =================
        angle_1 = 30
        rad_1 = np.deg2rad(angle_1)
        c1, s1 = np.cos(rad_1), np.sin(rad_1)

        mat_sym = create_rot_matrix(c1, s1, angle_1, symbolic=True)
        self.play(m.Write(mat_sym), run_time=1)

        mat_num = create_rot_matrix(c1, s1, angle_1, symbolic=False)
        mat_num.move_to(mat_sym)
        self.play(m.Transform(mat_sym, mat_num), run_time=1)
        self.wait(0.2)

        rot_mat_1 = np.array([[c1, -s1], [s1, c1]])
        self.apply_matrix(rot_mat_1)
        self.wait(0.6)

        # ПОКАЗЫВАЕМ ДУГУ
        arc_1 = m.Arc(radius=1.5, start_angle=0, angle=rad_1, color=m.ORANGE, stroke_width=4)
        label_1 = m.MathTex("30^\\circ", font_size=36)
        mid_angle = rad_1 / 2
        label_distance = 1.8
        label_1.move_to([label_distance * np.cos(mid_angle), label_distance * np.sin(mid_angle), 0])
        
        self.play(m.Create(arc_1), m.Write(label_1), run_time=0.6)
        self.wait(1.5)
        
        # ================= УДАЛЕНИЕ ДУГИ И ПОДГОТОВКА К СЛЕДУЮЩЕМУ ПОВОРОТУ =================
        self.play(m.FadeOut(arc_1), m.FadeOut(label_1), run_time=0.3)
        
        # Безопасное удаление из всех внутренних списков сцены
        for mob in [arc_1, label_1]:
            if mob in self.mobjects:
                self.mobjects.remove(mob)
            for attr_name in ["transformable_mobjects", "moving_mobjects", 
                              "foreground_mobjects", "background_mobjects"]:
                if hasattr(self, attr_name) and mob in getattr(self, attr_name):
                    getattr(self, attr_name).remove(mob)
                    
        self.wait(0.05)  # Даём рендер-движку синхронизировать состояние
        
        #Возвращаем координаты
        self.apply_inverse(rot_mat_1)
        
        # удаляем матрицу
        self.play(m.FadeOut(mat_sym), run_time=0.3)
        self.wait(0.5)

        # ================= ПОВОРОТ НА -45 ГРАДУСОВ =================
        angle_2 = -45
        rad_2 = np.deg2rad(angle_2)
        c2, s2 = np.cos(rad_2), np.sin(rad_2)

        mat_sym_2 = create_rot_matrix(c2, s2, angle_2, symbolic=True)
        self.play(m.Write(mat_sym_2), run_time=1)

        mat_num_2 = create_rot_matrix(c2, s2, angle_2, symbolic=False)
        mat_num_2.move_to(mat_sym_2)
        self.play(m.Transform(mat_sym_2, mat_num_2), run_time=1)
        self.wait(0.2)

        rot_mat_2 = np.array([[c2, -s2], [s2, c2]])
        self.apply_matrix(rot_mat_2)
        self.wait(0.6)

        # ДУГА на -45 градусов
        arc_2 = m.Arc(
            radius=1.5,
            start_angle=0,
            angle=rad_2,
            color=m.ORANGE,
            stroke_width=4
        )
        
        # Подпись "-45°"
        label_2 = m.MathTex("-45^\\circ", font_size=36)
        mid_angle_2 = rad_2 / 2
        label_2.move_to(
            np.array([label_distance * np.cos(mid_angle_2), 
                     label_distance * np.sin(mid_angle_2), 0])
        )
        
        self.play(m.Create(arc_2), m.Write(label_2), run_time=0.6)
        self.wait(2)

class ReflectionMatrixScene(LinearTransformationScene_):
    '''Матрица отражения'''
    def __init__(self, **kwargs):
        super().__init__(
            show_coordinates=True,
            leave_ghost_vectors=False,
            show_basis_vectors=False,
            **kwargs
        )

    def construct(self):
        # 1. Исходный вектор (берем не на оси, чтобы было видно отражение)
        # Вектор v = (2, 3)
        v_start = np.array([2, 3, 0])
        self.add_vector(v_start, color=m.PURPLE)
        self.wait(0.5)

        # 2. Матрица отражения S
        # S = [[1, 0], [0, -1]]
        S = np.array([[1, 0], [0, -1]])

        # Создаем визуальное отображение матрицы
        mat = m.Matrix(
            [[1, 0], [0, -1]],
            element_to_mobject_config={"font_size": 40, "color": m.DARK_GRAY}
        )
        mat.scale(1.2).to_edge(m.UP, buff=1).to_edge(m.LEFT)

        # Показываем матрицу
        self.play(m.Write(mat), run_time=1)
        self.wait(1)

        # 3. Применяем преобразование
        # Сетка перевернется, вектор отразится относительно оси X
        self.apply_matrix(S)
        self.wait(1.5)


class ReflectionLineScene(LinearTransformationScene_):
    '''4 отражение относительно линии, проходящей через начало координат'''
    def __init__(self, **kwargs):
        super().__init__(
            show_coordinates=True,
            leave_ghost_vectors=False,
            show_basis_vectors=False,
            **kwargs
        )

    def construct(self):
        # 1. Параметры отражения (α = 30°)
        alpha_deg = 30
        alpha_rad = np.deg2rad(alpha_deg)
        c2a, s2a = np.cos(2*alpha_rad), np.sin(2*alpha_rad)
        S = np.array([[c2a, s2a], 
                      [s2a, -c2a]])

        # 2. Исходный вектор (взят не на осях и не на прямой, чтобы отражение было заметно)
        v_start = np.array([3, 1, 0])
        self.add_vector(v_start, color=m.PURPLE)
        self.wait(0.5)

        # 3. Прямая отражения 
        line_len = 5
        refl_line = m.Line(
            start=[-line_len * np.cos(alpha_rad), -line_len * np.sin(alpha_rad), 0],
            end=[line_len * np.cos(alpha_rad), line_len * np.sin(alpha_rad), 0],
            color=m.YELLOW,
            stroke_width=4
        )

        self.play(m.Create(refl_line), run_time=1.5)
        self.wait(1)

        # 4. Матрица отражения S(α)
        mat_sym = m.Matrix(
            [[rf"\cos(2\alpha)", rf"\sin(2\alpha)"],
             [rf"\sin(2\alpha)", rf"-\cos(2\alpha)"]],
            element_to_mobject_config={"font_size": 32, "color": m.DARK_GRAY}
        )
        mat_sym.scale(1.1).to_edge(m.UP, buff=1).to_edge(m.LEFT)

        mat_num = m.Matrix(
            [[f"{c2a:.2f}", f"{s2a:.2f}"],
             [f"{s2a:.2f}", f"{-c2a:.2f}"]],
            element_to_mobject_config={"font_size": 32, "color": m.DARK_GRAY}
        )
        mat_num.move_to(mat_sym)

        self.play(m.Write(mat_sym), run_time=1)
        self.play(m.Transform(mat_sym, mat_num), run_time=1.5)
        self.wait(0.5)

        # 5. Применяем отражение
        self.apply_matrix(S)
        self.wait(1.5)

                   
        self.wait(0.05)  # Синхронизация рендера

class PermutationMatrixScene(LinearTransformationScene_):
    """5 Перестановка в двумерном пространстве. 
    Показывается матрица перестановок и анимируется ее действие.]"""
    def __init__(self, **kwargs):
        super().__init__(
            show_coordinates=True,
            leave_ghost_vectors=False,
            show_basis_vectors=False,
            **kwargs
        )

    def construct(self):
        # 1. ИСПРАВЛЕНИЕ: Берем вектор [2, 3] вместо [3, 7].
        v_start = np.array([2, 3, 0])
        self.add_vector(v_start, color=m.PURPLE)
        self.wait(0.5)

        # 2. Матрица перестановки P (меняет X и Y местами)
        P = np.array([[0, 1], [1, 0]])

        # Создаем визуальное отображение матрицы
        mat = m.Matrix(
            [[0, 1], [1, 0]],
            element_to_mobject_config={"font_size": 40, "color": m.DARK_GRAY}
        )
        mat.scale(1.2).to_edge(m.UP, buff=1).to_edge(m.LEFT)

        # Показываем матрицу
        self.play(m.Write(mat), run_time=1)
        self.wait(1)

        # 3. Анимация действия
        # Вектор перемещается из (2, 3) в (3, 2)
        self.apply_matrix(P)
        self.wait(1.5)

class Permutation3DScene(ThreeDScene_):
    """6 Перестановка в трехмерном пространстве с параллелепипедом"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.basis_i_color = m.GREEN
        self.basis_j_color = m.RED
        self.basis_k_color = m.GOLD

    def construct(self):
        # 1. Настройка осей и камеры
        axes = m.ThreeDAxes(x_length=6, y_length=6, z_length=6)
        axes.set_color(m.GRAY)
        self.set_camera_orientation(phi=70 * m.DEGREES, theta=-45 * m.DEGREES)
        self.begin_ambient_camera_rotation(rate=0.15)
        self.add(axes)
        self.wait(1)

        # 2. Векторы РАЗНОЙ длины (1, 2, 3)
        i_vec = m.Vector(m.RIGHT * 1, color=self.basis_i_color)
        j_vec = m.Vector(m.UP * 2, color=self.basis_j_color)
        k_vec = m.Vector(m.OUT * 3, color=self.basis_k_color)

        # 3. Метки (исправлено положение k)
        i_label = m.MathTex("i").set_color(self.basis_i_color).next_to(i_vec, m.RIGHT)
        j_label = m.MathTex("j").set_color(self.basis_j_color).next_to(j_vec, m.UP)
        # k_label сдвигаем чуть выше (m.UP), чтобы не перекрывалось осями
        k_label = m.MathTex("k").set_color(self.basis_k_color).next_to(k_vec, m.UP + m.RIGHT*0.5)

        self.add_fixed_in_frame_mobjects(i_label, j_label, k_label)

        # 4. Параллелепипед (объем, натянутый на векторы)
        # Создаем куб, масштабируем его под длины векторов (1, 2, 3) и сдвигаем в первый октант
        box = m.Cube(side_length=1)
        box.scale([1, 2, 3]) 
        box.shift([0.5, 1, 1.5]) # Сдвигаем, чтобы угол был в (0,0,0)
        box.set_stroke(m.WHITE, width=1, opacity=0.5)
        box.set_fill(m.BLUE, opacity=0.1)

        self.play(
            m.GrowArrow(i_vec), m.GrowArrow(j_vec), m.GrowArrow(k_vec),
            m.FadeIn(box),
            m.Write(i_label), m.Write(j_label), m.Write(k_label)
        )
        self.wait(1)


        # ПРИМЕР 1: Циклическая перестановка
        P1 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
        mat1 = m.Matrix(
            [[0, 0, 1], [1, 0, 0], [0, 1, 0]],
            element_to_mobject_config={"font_size": 28}
        )
        mat1.scale(0.8).to_corner(m.UP + m.LEFT).shift(m.DOWN * 0.8)
        self.add_fixed_in_frame_mobjects(mat1)


        self.play(m.Write(mat1))
        self.wait(1)

        # Вычисляем новые положения (умножаем матрицу на исходные векторы)
        # Важно: умножаем на исходные координаты [1,0,0], [0,2,0], [0,0,3]
        i1_new = m.Vector(P1 @ np.array([1, 0, 0]) * 1, color=self.basis_i_color)
        j1_new = m.Vector(P1 @ np.array([0, 1, 0]) * 2, color=self.basis_j_color)
        k1_new = m.Vector(P1 @ np.array([0, 0, 1]) * 3, color=self.basis_k_color)

        # Трансформируем и параллелепипед
        box1_new = m.Cube(side_length=1)
        box1_new.scale([1, 2, 3]) # Сохраняем пропорции
        box1_new.shift([0.5, 1, 1.5])
        box1_new.apply_matrix(P1) # Применяем матрицу к форме
        box1_new.set_stroke(m.WHITE, width=1, opacity=0.5)
        box1_new.set_fill(m.BLUE, opacity=0.1)

        self.play(
            m.Transform(i_vec, i1_new),
            m.Transform(j_vec, j1_new),
            m.Transform(k_vec, k1_new),
            m.Transform(box, box1_new),
            run_time=2
        )
        self.wait(2)

        self.play(m.FadeOut(mat1), run_time=0.5)
        self.remove(mat1)
        self.wait(0.5)

        # Возврат в исходное состояние
        '''self.play(
            m.Transform(i_vec, m.Vector(m.RIGHT * 1, color=self.basis_i_color)),
            m.Transform(j_vec, m.Vector(m.UP * 2, color=self.basis_j_color)),
            m.Transform(k_vec, m.Vector(m.OUT * 3, color=self.basis_k_color)),
            m.Transform(box, m.Cube(side_length=1).scale([1, 2, 3]).shift([0.5, 1, 1.5]).set_stroke(m.WHITE, width=1, opacity=0.5).set_fill(m.BLUE, opacity=0.1)),
            run_time=1.5
        )
        self.wait(1)'''

        # ПРИМЕР 2: Замена осей X и Y
        P2 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
        mat2 = m.Matrix(
            [[0, 1, 0], [1, 0, 0], [0, 0, 1]],
            element_to_mobject_config={"font_size": 28}
        )
        mat2.scale(0.8).to_corner(m.UP + m.LEFT).shift(m.DOWN * 0.8)
        self.add_fixed_in_frame_mobjects(mat2)


        self.play(m.Write(mat2))
        self.wait(1)

        i2_new = m.Vector(P2 @ np.array([1, 0, 0]) * 1, color=self.basis_i_color)
        j2_new = m.Vector(P2 @ np.array([0, 1, 0]) * 2, color=self.basis_j_color)
        k2_new = m.Vector(P2 @ np.array([0, 0, 1]) * 3, color=self.basis_k_color) # k не меняется

        box2_new = m.Cube(side_length=1)
        box2_new.scale([1, 2, 3])
        box2_new.shift([0.5, 1, 1.5])
        box2_new.apply_matrix(P2)
        box2_new.set_stroke(m.WHITE, width=1, opacity=0.5)
        box2_new.set_fill(m.BLUE, opacity=0.1)

        self.play(
            m.Transform(i_vec, i2_new),
            m.Transform(j_vec, j2_new),
            m.Transform(k_vec, k2_new),
            m.Transform(box, box2_new),
            run_time=2
        )
        self.wait(2)

        self.play(
            m.FadeOut(mat2), 
            m.FadeOut(i_vec), m.FadeOut(j_vec), m.FadeOut(k_vec),
            m.FadeOut(box),
            m.FadeOut(i_label), m.FadeOut(j_label), m.FadeOut(k_label)
        )
        self.wait(1)
class UpperTriangularShearScene(LinearTransformationScene_):
    """7а Демонстрация сдвига (shear) с помощью верхнетреугольной матрицы в 2D"""
    def __init__(self, **kwargs):
        super().__init__(
            show_coordinates=True,
            leave_ghost_vectors=False,
            show_basis_vectors=False,
            **kwargs
        )

    def construct(self):
        # Матрица верхнетреугольного сдвига
        # Общий вид: [[a, b], [0, c]]. При a=1, c=1, b=1 получаем чистый сдвиг
        U = np.array([[1, 1], [0, 1]])

        # Визуализация матрицы
        mat = m.Matrix(
            [[1, 1], [0, 1]],
            element_to_mobject_config={"font_size": 32, "color": m.DARK_GRAY}
        )
        mat.scale(1.1).to_edge(m.UP, buff=1).to_edge(m.LEFT).shift(m.DOWN * 0.8)

        self.play(m.Write(mat), run_time=1)
        self.wait(0.5)

        # Тестовый вектор для наглядности
        # Возьмём (2, 2). После сдвига станет (2 + 1*2, 2) = (4, 2)
        v_start = np.array([2, 2, 0])
        self.add_vector(v_start, color=m.PURPLE)
        self.wait(0.5)

        # Применяем преобразование
        # Вертикальная сетка останется вертикальной, горизонтальная наклонится
        self.apply_matrix(U)
        self.wait(1.5)

class UpperTriangularScene(ThreeDScene_):
    """8 Демонстрация влияния верхнетреугольной матрицы на трёхмерное пространство"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        # 1. Настройка осей и камеры
        axes = m.ThreeDAxes(x_length=10, y_length=10, z_length=10)
        axes.set_color(m.GRAY)
        
        # Настраиваем камеру: угол обзора
        self.set_camera_orientation(phi=55 * m.DEGREES, theta=-30 * m.DEGREES)
        
        self.begin_ambient_camera_rotation(rate=0.15)
        self.add(axes)
        self.wait(0.5)

        # 2. Исходный параллелепипед (ещё меньше, чтобы точно поместился)
        # Размеры: X=0.3, Y=0.6, Z=0.6
        box = m.Cube(side_length=1)
        box.scale([0.3, 0.6, 0.6])
        box.shift([0.15, 0.3, 0.3]) 
        box.set_stroke(m.WHITE, width=1.5, opacity=0.8)
        box.set_fill(m.BLUE, opacity=0.15)

        # 3. Цветные вектора-рёбра
        v_i = m.Vector([0.3, 0, 0], color=m.GREEN, buff=0)
        v_j = m.Vector([0, 0.6, 0], color=m.RED, buff=0)
        v_k = m.Vector([0, 0, 0.6], color=m.GOLD, buff=0)

        self.play(
            m.Create(box),
            m.GrowArrow(v_i), m.GrowArrow(v_j), m.GrowArrow(v_k),
            run_time=1.5
        )
        self.wait(0.5)

        # 4. Матрица U (сдвинута ниже и уменьшена)
        U = np.array([[2, 5, -1], [0, 3, 4], [0, 0, 7]])
        mat = m.Matrix(
            [[2, 5, -1], [0, 3, 4], [0, 0, 7]],
            element_to_mobject_config={"font_size": 20, "color": m.DARK_GRAY}
        )
        mat.scale(0.6).to_corner(m.UP + m.LEFT).shift(m.DOWN * 1.5)
        self.add_fixed_in_frame_mobjects(mat)

        self.play(m.Write(mat), run_time=1)
        self.wait(1)

        # 5. Вычисляем конечные положения
        v_i_new = m.Vector(U @ [0.3, 0, 0], color=m.GREEN, buff=0)
        v_j_new = m.Vector(U @ [0, 0.6, 0], color=m.RED, buff=0)
        v_k_new = m.Vector(U @ [0, 0, 0.6], color=m.GOLD, buff=0)

        box_new = m.Cube(side_length=1)
        box_new.scale([0.3, 0.6, 0.6])
        box_new.shift([0.15, 0.3, 0.3])
        box_new.apply_matrix(U)
        box_new.set_stroke(m.WHITE, width=1.5, opacity=0.8)
        box_new.set_fill(m.BLUE, opacity=0.15)

        # 6. Анимация трансформации
        self.play(
            m.Transform(box, box_new),
            m.Transform(v_i, v_i_new),
            m.Transform(v_j, v_j_new),
            m.Transform(v_k, v_k_new),
            run_time=3
        )
        self.wait(1.5)


        # 7. Очистка
        self.play(
            m.FadeOut(mat), 
            m.FadeOut(box), m.FadeOut(v_i), m.FadeOut(v_j), m.FadeOut(v_k)
        )
        self.wait(0.5)

class SymmetricMatrixScene(m.Scene):
    """9 Сравнение произвольной и симметричной матриц"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = m.WHITE

    def construct(self):
        # ================= ФУНКЦИЯ СОЗДАНИЯ ПЛОСКОСТИ =================
        def create_plane():
            plane = m.NumberPlane(
                x_range=[-3, 3, 1],
                y_range=[-3, 3, 1],
                background_line_style={
                    "stroke_color": m.GRAY,
                    "stroke_width": 1,
                    "stroke_opacity": 0.3
                },
                axis_config={"stroke_color": m.BLACK, "stroke_width": 2}
            )
            plane.add_coordinates()
            plane.coordinate_labels.set_color(m.BLACK)
            return plane

        # 1. Плоскости
        plane_L = create_plane().shift(m.LEFT * 3.5)
        plane_R = create_plane().shift(m.RIGHT * 3.5)

        # 2. Окружности (строго на пересечении осей)
        circle_L = m.Circle(radius=0.8, color=m.BLUE, stroke_width=3)
        circle_L.move_to(plane_L.c2p(0, 0))

        circle_R = m.Circle(radius=0.8, color=m.GREEN, stroke_width=3)
        circle_R.move_to(plane_R.c2p(0, 0))

        self.play(m.Create(plane_L), m.Create(plane_R))
        self.play(m.Create(circle_L), m.Create(circle_R))
        self.wait(0.5)

        # 3. МАТРИЦЫ (Данные для математики + Визуал для отображения)
        
        # === ИСПРАВЛЕНИЕ: Объявляем numpy-массивы ДО визуальных объектов ===
        mat_A = np.array([[1.5, 1.0], [-0.5, 1.2]])  # Для ApplyMatrix
        mat_S = np.array([[2.0, 0], [0, 0.8]])       # Для ApplyMatrix

        # ЛЕВАЯ (Синяя) - Визуальное отображение
        mat_L = m.Matrix(
            [[1.5, 1.0], [-0.5, 1.2]],
            element_to_mobject_config={"font_size": 22, "color": m.BLUE}
        )
        mat_L.scale(0.6)
        mat_L.get_brackets().set_color(m.BLUE)
        mat_L.get_brackets().set_stroke(width=1.5)
        mat_L.move_to(m.LEFT * 4.5 + m.UP * 2.5)

        title_L = m.VGroup(
            m.Text("Произвольная", color=m.BLUE, font_size=16),
            m.MathTex("A", color=m.BLUE, font_size=16)
        ).arrange(m.RIGHT)
        title_L.next_to(mat_L, m.DOWN)

        # ПРАВАЯ (Зеленая) - Визуальное отображение
        mat_R = m.Matrix(
            [[2.0, 0], [0, 0.8]],
            element_to_mobject_config={"font_size": 22, "color": m.GREEN}
        )
        mat_R.scale(0.6)
        mat_R.get_brackets().set_color(m.GREEN)
        mat_R.get_brackets().set_stroke(width=1.5)
        mat_R.move_to(m.RIGHT * 4.5 + m.UP * 2.5)

        title_R = m.VGroup(
            m.Text("Симметричная", color=m.GREEN, font_size=16),
            m.MathTex("S", color=m.GREEN, font_size=16)
        ).arrange(m.RIGHT)
        title_R.next_to(mat_R, m.DOWN)

        self.play(m.Write(mat_L), m.Write(title_L), m.Write(mat_R), m.Write(title_R))
        self.wait(1)

        # 4. Анимация (теперь mat_A и mat_S объявлены и доступны)
        self.play(
            m.ApplyMatrix(mat_A, circle_L, about_point=plane_L.c2p(0, 0)),
            run_time=2
        )
        self.play(
            m.ApplyMatrix(mat_S, circle_R, about_point=plane_R.c2p(0, 0)),
            run_time=2
        )
        self.wait(1)

        # 5. Подпись
        caption = m.Text(
            "Симметричная матрица: растяжение вдоль ортогональных осей, без вращения",
            font_size=22, color=m.BLACK
        ).to_edge(m.DOWN)
        self.play(m.Write(caption))
        self.wait(3)

        # 6. Очистка
        self.play(m.FadeOut(m.VGroup(
            plane_L, plane_R, circle_L, circle_R,
            mat_L, mat_R, title_L, title_R, caption
        )))

class CovarianceEllipseScene(m.Scene):
    """10 Визуализация ковариационной матрицы через облако точек и эллипс рассеяния"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = m.WHITE
        # Фиксируем seed для воспроизводимости анимации
        np.random.seed(42)

    def construct(self):
        # Настройка осей
        axes = m.Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=6,
            y_length=6
        )
        axes.set_color(m.BLACK)
        axes.add_coordinates()
        axes.coordinate_labels.set_color(m.BLACK)
        
        self.add(axes)
        self.wait(0.5)

        # Используем настоящее случайное распределение
        n_points = 100  # Количество точек
        
        # Базовые точки из стандартного нормального распределения N(0,1)
        base_points = np.random.randn(n_points, 2)

        # ШАГ 1: КРУГ (Равные дисперсии, нет корреляции) 
        cov1 = np.array([[1, 0], [0, 1]])
        # Точки уже из N(0,I), так что просто используем их
        points_1_coords = base_points * 0.8  # Немного уменьшим масштаб
        
        mat1 = self.create_matrix(cov1, color=m.BLUE)
        cap1 = m.Text("(a) Равные дисперсии → Круг", color=m.BLACK, font_size=24).to_edge(m.DOWN)
        
        # Создаём VGroup из точек
        points_1 = m.VGroup(*[
            m.Dot(axes.c2p(p[0], p[1]), radius=0.04, color=m.BLUE_E) 
            for p in points_1_coords
        ])
        
        # Эллипс (круг) для визуализации
        contour_1 = m.Circle(radius=1.5, color=m.BLUE, stroke_width=2)
        contour_1.set_fill(m.BLUE, opacity=0.1)
        contour_1.move_to(axes.c2p(0, 0))

        self.play(
            m.Create(contour_1), 
            m.FadeIn(points_1),
            m.Write(mat1),
            m.Write(cap1),
            run_time=2
        )
        self.wait(1)
        
        self.play(
            m.FadeOut(contour_1), m.FadeOut(points_1), 
            m.FadeOut(mat1), m.FadeOut(cap1)
        )

        #  ШАГ 2: ЭЛЛИПС ПО ОСЯМ (Разные дисперсии) 
        cov2 = np.array([[3, 0], [0, 1]]) 
        # Преобразуем точки: умножаем на sqrt(дисперсий)
        trans2 = np.array([[np.sqrt(3), 0], [0, 1]])
        points_2_coords = base_points @ trans2.T
        
        mat2 = self.create_matrix(cov2, color=m.BLUE)
        cap2 = m.Text("(b) Разные дисперсии → Эллипс по осям", color=m.BLACK, font_size=24).to_edge(m.DOWN)

        points_2 = m.VGroup(*[
            m.Dot(axes.c2p(p[0], p[1]), radius=0.04, color=m.BLUE_E) 
            for p in points_2_coords
        ])
        
        # Эллипс: ширина и высота пропорциональны sqrt(собственных значений)
        contour_2 = m.Ellipse(
            width=2 * np.sqrt(3) * 1.5, 
            height=2 * 1 * 1.5, 
            color=m.BLUE, 
            stroke_width=2
        )
        contour_2.set_fill(m.BLUE, opacity=0.1)
        contour_2.move_to(axes.c2p(0, 0))

        self.play(
            m.Create(contour_2), 
            m.FadeIn(points_2),
            m.Write(mat2),
            m.Write(cap2),
            run_time=2
        )
        self.wait(1)

        self.play(
            m.FadeOut(contour_2), m.FadeOut(points_2), 
            m.FadeOut(mat2), m.FadeOut(cap2)
        )

        # ШАГ 3: ПОВЁРНУТЫЙ ЭЛЛИПС (Корреляция) 
        cov3 = np.array([[2, 1], [1, 2]])
        # Для такой ковариации используем разложение Холецкого или собственное разложение
        # Собственные значения: 3 и 1, угол поворота 45°
        angle = np.deg2rad(45)
        rot = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        scale = np.array([[np.sqrt(3), 0], [0, 1]])
        trans3 = rot @ scale
        
        points_3_coords = base_points @ trans3.T
        
        mat3 = self.create_matrix(cov3, color=m.BLUE)
        cap3 = m.Text("(c) Корреляция → Повёрнутый эллипс", color=m.BLACK, font_size=24).to_edge(m.DOWN)

        points_3 = m.VGroup(*[
            m.Dot(axes.c2p(p[0], p[1]), radius=0.04, color=m.BLUE_E) 
            for p in points_3_coords
        ])
        
        contour_3 = m.Ellipse(
            width=2 * np.sqrt(3) * 1.5, 
            height=2 * 1 * 1.5, 
            color=m.BLUE, 
            stroke_width=2
        )
        contour_3.set_fill(m.BLUE, opacity=0.1)
        contour_3.rotate(angle)
        contour_3.move_to(axes.c2p(0, 0))

        self.play(
            m.Create(contour_3), 
            m.FadeIn(points_3),
            m.Write(mat3),
            m.Write(cap3),
            run_time=2
        )
        self.wait(3)

        self.play(m.FadeOut(*self.mobjects))

    def create_matrix(self, cov_matrix, color):
        """Вспомогательная функция для создания красивой матрицы"""
        mat = m.Matrix(
            cov_matrix,
            element_to_mobject_config={"font_size": 24, "color": color}
        )
        mat.scale(0.7)
        mat.get_brackets().set_color(m.BLACK)
        mat.get_brackets().set_stroke(width=2)
        mat.to_corner(m.UP + m.LEFT, buff=1)
        return mat
    
class MahalanobisDistanceScene(m.Scene):
    """Визуализация расстояния Махаланобиса vs евклидова расстояния"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = m.WHITE
        np.random.seed(42)

    def construct(self):
        # ================= НАСТРОЙКА ОСЕЙ =================
        axes = m.Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=6,
            y_length=6
        )
        axes.set_color(m.BLACK)
        axes.add_coordinates()
        axes.coordinate_labels.set_color(m.BLACK)
        self.add(axes)
        self.wait(0.5)

        # ================= ГЕНЕРАЦИЯ ДАННЫХ =================
        # Ковариационная матрица с корреляцией
        cov = np.array([[2, 1.5], [1.5, 2]])
        mean = np.array([0, 0])
        
        # Генерируем коррелированные точки
        n_points = 150
        base_points = np.random.randn(n_points, 2)
        # Применяем преобразование для получения нужной ковариации
        L = np.linalg.cholesky(cov)
        points_coords = base_points @ L.T * 0.8
        
        # Визуализация точек
        points = m.VGroup(*[
            m.Dot(axes.c2p(p[0], p[1]), radius=0.03, color=m.BLUE_E) 
            for p in points_coords
        ])
        
        # Эллипс рассеяния
        eigvals, eigvecs = np.linalg.eigh(cov)
        angle = np.arctan2(eigvecs[1, 0], eigvecs[0, 0])
        ellipse = m.Ellipse(
            width=2 * np.sqrt(eigvals[0]) * 2.5 * 0.8,
            height=2 * np.sqrt(eigvals[1]) * 2.5 * 0.8,
            color=m.BLUE,
            stroke_width=2
        )
        ellipse.set_fill(m.BLUE, opacity=0.1)
        ellipse.rotate(angle)
        ellipse.move_to(axes.c2p(0, 0))
        
        self.play(m.Create(ellipse), m.FadeIn(points), run_time=2)
        self.wait(0.5)

        # ================= ДВЕ ТОЧКИ =================
        # Выбираем две точки: одну в центре облака, другую на периферии
        point_A = np.array([0.5, 0.5])  # Близко к центру
        point_B = np.array([2.5, 2.5])  # Дальше, но вдоль главной оси
        
        dot_A = m.Dot(axes.c2p(*point_A), radius=0.08, color=m.RED)
        dot_B = m.Dot(axes.c2p(*point_B), radius=0.08, color=m.GREEN)
        
        # Евклидово расстояние (прямая линия)
        euclid_line = m.Line(
            axes.c2p(*point_A), 
            axes.c2p(*point_B), 
            color=m.RED,
            stroke_width=3
        )
        euclid_dist = np.linalg.norm(point_A - point_B)
        
        label_euclid = m.Text(
            f"Евклидово: {euclid_dist:.2f}",
            color=m.RED,
            font_size=20
        ).to_corner(m.UP + m.LEFT)
        
        self.play(
            m.Create(dot_A), m.Create(dot_B),
            m.Create(euclid_line),
            m.Write(label_euclid),
            run_time=2
        )
        self.wait(1)

        # ================= РАССТОЯНИЕ МАХАЛАНОБИСА =================
        # Вычисляем обратную ковариационную матрицу
        cov_inv = np.linalg.inv(cov)
        
        # Расстояние Махаланобиса
        diff = point_A - point_B
        mahal_dist = np.sqrt(diff @ cov_inv @ diff)
        
        # Показываем формулу
        formula = m.MathTex(
            r"D_M(\mathbf{x}, \mathbf{y}) = \sqrt{(\mathbf{x} - \mathbf{y})^T \Sigma^{-1} (\mathbf{x} - \mathbf{y})}",
            font_size=24
        ).to_edge(m.UP)
        
        # "Отбеливание" пространства - показываем преобразованные точки
        # Применяем L^{-1} к точкам, где L - разложение Холецкого
        L_inv = np.linalg.inv(L)
        point_A_white = point_A @ L_inv.T * 0.8
        point_B_white = point_B @ L_inv.T * 0.8
        
        # Создаём правую часть сцены для "отбеленного" пространства
        axes_white = m.Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=4,
            y_length=4
        )
        axes_white.set_color(m.BLACK)
        axes_white.shift(m.RIGHT * 4)
        axes_white.add_coordinates()
        axes_white.coordinate_labels.set_color(m.BLACK)
        
        # Круг (единичная ковариация)
        circle_white = m.Circle(
            radius=1.5,
            color=m.GREEN,
            stroke_width=2
        )
        circle_white.set_fill(m.GREEN, opacity=0.1)
        circle_white.move_to(axes_white.c2p(0, 0))
        
        # Точки в отбеленном пространстве
        dot_A_white = m.Dot(
            axes_white.c2p(*point_A_white),
            radius=0.08,
            color=m.RED
        )
        dot_B_white = m.Dot(
            axes_white.c2p(*point_B_white),
            radius=0.08,
            color=m.GREEN
        )
        
        # Линия расстояния Махаланобиса
        mahal_line = m.Line(
            axes_white.c2p(*point_A_white),
            axes_white.c2p(*point_B_white),
            color=m.GREEN,
            stroke_width=3
        )
        
        label_mahal = m.Text(
            f"Махаланобис: {mahal_dist:.2f}",
            color=m.GREEN,
            font_size=20
        ).to_corner(m.UP + m.RIGHT)
        
        label_white = m.Text(
            "«Отбеленное» пространство:\nковариация = I",
            color=m.BLACK,
            font_size=16
        ).next_to(axes_white, m.DOWN)
        
        self.play(
            m.Write(formula),
            m.Create(axes_white),
            m.Create(circle_white),
            m.Create(dot_A_white),
            m.Create(dot_B_white),
            m.Create(mahal_line),
            m.Write(label_mahal),
            m.Write(label_white),
            run_time=3
        )
        self.wait(2)

        # ================= ФИНАЛЬНАЯ ПОДПИСЬ =================
        caption = m.Text(
            "Евклидово расстояние не учитывает форму распределения,\n"
            "а расстояние Махаланобиса измеряет в единицах стандартного отклонения",
            color=m.BLACK,
            font_size=18
        ).to_edge(m.DOWN)
        
        self.play(m.Write(caption), run_time=2)
        self.wait(3)

        # Очистка
        self.play(m.FadeOut(*self.mobjects))

class MahalanobisTwoPointsScene(m.Scene):
    """Анимация отбеливания: Евклидово расстояние между двумя точками превращается в расстояние Махаланобиса"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = m.WHITE
        np.random.seed(42)

    def construct(self):
        # 1. Оси
        axes = m.Axes(x_range=[-4, 4, 1], y_range=[-3, 3, 1], x_length=6, y_length=4)
        axes.set_color(m.BLACK)
        axes.add_coordinates()
        axes.coordinate_labels.set_color(m.BLACK)
        self.add(axes)
        
        # 2. Данные: Коррелированное облако
        cov = np.array([[2, 1.5], [1.5, 2]])
        L = np.linalg.cholesky(cov)
        n_points = 150
        base_points = np.random.randn(n_points, 2)
        points_coords = (base_points @ L.T) * 0.8
        
        points = m.VGroup(*[m.Dot(axes.c2p(*p), radius=0.04, color=m.BLUE_E) for p in points_coords])
        
        # Эллипс рассеяния
        eigvals, eigvecs = np.linalg.eigh(cov)
        angle = np.arctan2(eigvecs[1, 0], eigvecs[0, 0])
        ellipse = m.Ellipse(
            width=2 * np.sqrt(eigvals[0]) * 2.0 * 0.8,
            height=2 * np.sqrt(eigvals[1]) * 2.0 * 0.8,
            color=m.BLUE, stroke_width=2
        )
        ellipse.set_fill(m.BLUE, opacity=0.1)
        ellipse.rotate(angle)
        ellipse.move_to(axes.c2p(0, 0))
        
        # 3. ДВЕ ТОЧКИ
        p1 = np.array([-1.0, -0.5]) * 0.8
        p2 = np.array([2.0, 1.5]) * 0.8
        
        dot1 = m.Dot(axes.c2p(*p1), radius=0.08, color=m.RED)
        dot2 = m.Dot(axes.c2p(*p2), radius=0.08, color=m.GREEN)
        
        # Исходное Евклидово расстояние (жёлтая линия)
        euclid_line = m.Line(axes.c2p(*p1), axes.c2p(*p2), color=m.PURPLE, stroke_width=3)
        euclid_dist = np.linalg.norm(p1 - p2)
        label_euclid = m.Text(f"Евклидово: {euclid_dist:.2f}", color=m.DARK_GRAY, font_size=20)
        label_euclid.next_to(euclid_line, m.UP)
        label_euclid.shift(m.LEFT * 1.8 + m.UP * 0.5)
        
        # Показываем исходную сцену
        self.play(
            m.Create(ellipse), m.FadeIn(points),
            m.Create(dot1), m.Create(dot2), m.Create(euclid_line),
            m.Write(label_euclid),
            run_time=2
        )
        self.wait(1)

        # 4. Матрица отбеливания W = Σ^(-1/2)
        eigvals, eigvecs = np.linalg.eigh(cov)
        W = eigvecs @ np.diag(1 / np.sqrt(eigvals)) @ eigvecs.T
        
        # Вычисляем, где окажутся точки после отбеливания
        p1_w = p1 @ W.T
        p2_w = p2 @ W.T
        mahal_dist = np.linalg.norm(p1_w - p2_w)
        
        label_mahal = m.Text(f"Махаланобис: {mahal_dist:.2f}", color=m.DARK_GRAY, font_size=20)
        label_mahal.move_to(label_euclid.get_center())
        
        
        # 5. АНИМАЦИЯ ТРАНСФОРМАЦИИ
        # Применяем матрицу W ко всем объектам одновременно
        self.play(
            m.ApplyMatrix(W, m.VGroup(ellipse, points, euclid_line, dot1, dot2)),
            run_time=2.5
        )
        self.wait(0.5)
        
        # 6. Финальное состояние
        # Линия теперь лежит в отбеленном пространстве, её длина = расстояние Махаланобиса
        final_line = m.Line(axes.c2p(*p1_w), axes.c2p(*p2_w), color=m.ORANGE, stroke_width=4)
        
        self.play(
            m.Transform(euclid_line, final_line),
            m.Transform(label_euclid, label_mahal),
            run_time=1
        )
        
        line1 = m.Text("Евклидово  расстояние  не  учитывает  форму  распределения,", 
                       font_size=18, color=m.BLACK)
        line2 = m.Text("Махаланобис  измеряет  в  единицах  стандартного  отклонения", 
                       font_size=18, color=m.BLACK)
        
        # Объединяем и выравниваем по центру
        caption = m.VGroup(line1, line2).arrange(m.DOWN, buff=0.25)
        caption.to_edge(m.DOWN, buff=1)  # <-- Увеличенный отступ от нижнего края
        
        self.play(m.Write(caption))
        self.wait(3)

if __name__ == '__main__':
    import os
    from pathlib import Path

    SCENES = [
        #"LTExample",
        #"LT3D",
        #"LT2d23d",
        #"LT3d22d",
        #"LT2d21d",
        #"LT2d21dreversed",
        #"MatrixMatrixMul2",
        #"MatrixMatrixMulResult",
        #"MatrixMatrixMulNotSymmetrical",
        #"LT3D_scale1",
        #"LT3D_scale2",
        #"LT3D_scale2_down",
        #"LT3D_scale2_reversed",
        #"MatrixDeterminantScene",
        #"LinearTransformExample",
        #"DegenerateVolume3D",
        #"MatrixDeterminantGeometry",
        #"DeterminantVolumeScaling3D",
        #"DeterminantVolumeScale",
        #'MatrixVectorMult',
        #'RotationPlane2D',
        #'ReflectionMatrixScene',
        #'ReflectionLineScene',
        #'PermutationMatrixScene',
        #'Permutation3DScene',
        #'UpperTriangularShearScene',
        #'UpperTriangularScene',
        #'SymmetricMatrixScene',
        #'CovarianceEllipseScene',
        'MahalanobisTwoPointsScene',
    ]
    file_path = Path(__file__).resolve()

    for SCENE in SCENES:
        os.system(f"manim {Path(__file__).resolve()} {SCENE} -qh")
        os.system(f"manim {Path(__file__).resolve()} {SCENE} -s")