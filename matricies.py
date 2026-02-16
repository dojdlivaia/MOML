from manim import *
import numpy as np
from math import sin, ceil

class LinearTransformExample(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
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

class LTNonSquare(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
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

        self.matrix_text = Matrix(matrix).scale(1).to_edge(UP, buff=1).to_edge(LEFT)
        self.play(Create(self.matrix_text), run_time=0.3)
        self.wait()

        self.add_vector(vec := Vector([2, 1.5]))
        self.apply_matrix(matrix)
        self.wait()

class LT2d23d(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
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

        self.matrix_text = Matrix(matrix).scale(1).to_edge(UP, buff=1).to_edge(LEFT)
        self.play(Create(self.matrix_text), run_time=0.3)
        self.wait()
        matrix = np.concat([matrix, np.array([[0, 0]])], axis=0)
        print(matrix)

        self.add_vector(vec := Vector(vec_))
        self.apply_matrix(matrix)
        self.wait()

        print(np.dot(matrix, vec_.T))
        vec = vec.become(Vector(np.dot(matrix, vec_.T)))
        label = vec.coordinate_label(integer_labels=False, n_dim=1).shift(UP * 0.5)
        self.play(Create(label), run_time=0.3)
        self.wait()

class LinearTransform(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs
        )

    def apply_custom_matrix(self, matrix):
        matrix = np.array(matrix).T

        self.matrix_text = Matrix(matrix).scale(1).to_edge(UP, buff=1).to_edge(LEFT)
        self.play(Create(self.matrix_text), run_time=0.3)
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
        # self.play(Uncreate(self.matrix_text), run_time=0.3)

class MatrixVectorMul(LinearTransform):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            **kwargs
        )

    def apply_custom_matrix(self, matrix):
        matrix = np.array(matrix).T

        self.matrix_text = Matrix(matrix).scale(1).to_edge(UP, buff=1).to_edge(LEFT)
        self.play(Create(self.matrix_text), run_time=0.3)
        self.wait()

        vec = self.add_vector([2, 1.5])
        label = vec.coordinate_label(integer_labels=False)
        self.play(Create(label), run_time=0.3)
        self.wait()
        self.play(Uncreate(label), run_time=0.3)

        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait()

        self.wait(0.5)
        vec = vec.become(Vector([3.75, 3.15], color=YELLOW))
        label = vec.coordinate_label(integer_labels=False)
        self.play(Create(label), run_time=0.3)
        self.wait()
        self.play(Uncreate(label), run_time=0.3)

        self.play(Create(label), run_time=0.3)
        self.wait()
        self.play(Uncreate(label), run_time=0.3)

        self.moving_mobjects = []
        self.apply_inverse(matrix)
        self.play(Uncreate(self.matrix_text), run_time=0.3)
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

class SVD(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            **kwargs
        )

    def construct(self):
        matrix = np.array([[0.8, 0], [0.5, 3]]).T

        s = 0.7

        self.play(Create(A := Matrix(matrix).scale(s).to_edge(DOWN, buff=1).to_edge(LEFT)), run_time=0.01)

        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait()

        i = Vector([matrix[0][0], matrix[1][0]], color=GREEN)
        j = Vector([matrix[0][1], matrix[1][1]], color=RED)
        self.play(Create(i), run_time=0.01)
        self.play(Create(j), run_time=0.01)

        self.moving_mobjects = []
        self.apply_inverse(matrix)
        self.wait()

        U, S, Vh = np.linalg.svd(matrix, full_matrices=True)
        print(Vh)
        print(np.diag(S))
        print(U)

        self.play(Create(t1 := Text("=").scale(s).next_to(A, RIGHT)), run_time=0.01)
        self.play(Create(U_label := Matrix(np.round(U,2), stroke_width=7).scale(s).next_to(t1, RIGHT)), run_time=0.01)
        self.play(Create(t2 := Tex(r"$\times$").scale(s).next_to(U_label, RIGHT)), run_time=0.01)
        self.play(Create(S_label := Matrix(np.round(np.diag(S),2), stroke_width=7).scale(s).next_to(t2, RIGHT)), run_time=0.01)
        self.play(Create(t3 := Tex(r"$\times$").scale(s).next_to(S_label, RIGHT)), run_time=0.01)
        self.play(Create(V_label := Matrix(np.round(Vh,2), stroke_width=7).scale(s).next_to(t3, RIGHT)), run_time=0.01)
        self.wait()

        self.play(V_label.animate.set_color(YELLOW), run_time=0.3)
        self.play(Create(t := Text("Поворот", color=YELLOW).scale(s).next_to(V_label, UP)), run_time=0.01)
        self.moving_mobjects = []
        self.apply_matrix(Vh)
        self.play(Uncreate(t))
        self.play(V_label.animate.set_color(WHITE), run_time=0.3)
        self.wait()

        self.play(S_label.animate.set_color(YELLOW), run_time=0.3)
        self.play(Create(t := Text("Масштабирование", color=YELLOW).scale(s).next_to(S_label, UP)), run_time=0.01)
        self.moving_mobjects = []
        self.apply_matrix(np.diag(S))
        self.play(Uncreate(t))
        self.play(S_label.animate.set_color(WHITE), run_time=0.3)
        self.wait()

        self.play(U_label.animate.set_color(YELLOW), run_time=0.3)
        self.play(Create(t := Text("Поворот", color=YELLOW).scale(s).next_to(U_label, UP)), run_time=0.01)
        self.moving_mobjects = []
        self.apply_matrix(U)
        self.play(Uncreate(t))
        self.play(U_label.animate.set_color(WHITE), run_time=0.3)
        self.wait()


class AddFunction(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False,
            leave_ghost_vectors=False,
            **kwargs
        )

    def construct(self):
        s = 1
        self.play(Create(Tex(r"$f(\vec{v}) = \vec{v} + \begin{bmatrix} 1  \\ 2 \end{bmatrix}$").scale(s).to_edge(UP, buff=1).to_edge(LEFT)), run_time=0.5)
        self.moving_mobjects = []

        self.play(Create(Vector([3, -2])), run_time=0.3)

        self.apply_nonlinear_transformation(lambda vec: vec + np.array([1, 2, 0])) 
        self.wait()   

        self.play(Create(Vector([4, 0], color=YELLOW)), run_time=0.3)
        self.wait()   


class AddNotLinear(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=True,
            leave_ghost_vectors=False,
            **kwargs
        )

    def construct(self):
        s = 1
        self.play(Create(Tex(r"$f(\vec{v}) = \vec{v} + \begin{bmatrix} 1  \\ 2 \end{bmatrix}$").scale(s).to_edge(UP, buff=1).to_edge(LEFT)), run_time=0.5)
        self.moving_mobjects = []

        self.play(Create(Vector([1, 1])), run_time=0.3)

        self.apply_nonlinear_transformation(lambda vec: vec + np.array([1, 2, 0])) 
        self.wait()   

        self.play(Create(Vector([2, 3], color=YELLOW)), run_time=0.3)
        self.wait()   


class NonLinearTransform(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
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


class LT3D(ThreeDScene):
    def create_matrix(self, np_matrix):
        m = Matrix(np_matrix)

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(UP + LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = GREEN,
        self.basis_j_color = RED,
        self.basis_k_color = GOLD

        M = np.array([
            [2, 2, -1],
            [-2, 1, 2],
            [3, 1, -0]
        ])

        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)

        basis_vector_helper.to_corner(UP + RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE_E)

        i_vec = Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = Vector(M @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            Create(cube),
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(k_vec),
            Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)


class LT3D_scale1(ThreeDScene):
    def create_matrix(self, np_matrix):
        m = Matrix(np_matrix)

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(UP + LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = GREEN,
        self.basis_j_color = RED,
        self.basis_k_color = GOLD

        M = np.array([
            [2, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])

        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)

        basis_vector_helper.to_corner(UP + RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE_E)

        i_vec = Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = Vector(M @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            Create(cube),
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(k_vec),
            Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)


class LT3D_scale2(ThreeDScene):
    def create_matrix(self, np_matrix):
        m = Matrix(np_matrix)

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(UP + LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = GREEN,
        self.basis_j_color = RED,
        self.basis_k_color = GOLD

        M = np.array([
            [2, 0, 0],
            [0, 1, 0],
            [0, 0, 2.5]
        ])

        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)

        basis_vector_helper.to_corner(UP + RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE_E)

        i_vec = Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = Vector(M @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            Create(cube),
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(k_vec),
            Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)


class LT3D_scale2_down(ThreeDScene):
    def create_matrix(self, np_matrix):
        m = Matrix(np_matrix)

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(UP + LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = GREEN,
        self.basis_j_color = RED,
        self.basis_k_color = GOLD

        M = np.array([
            [2, 0, 0],
            [0, 1, 0],
            [0, 0, 0.3]
        ])

        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)

        basis_vector_helper.to_corner(UP + RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE_E)

        i_vec = Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = Vector(M @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            Create(cube),
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(k_vec),
            Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)


class LT3D_scale2_reversed(ThreeDScene):
    def create_matrix(self, np_matrix):
        m = Matrix(np_matrix)

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(UP + LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = GREEN,
        self.basis_j_color = RED,
        self.basis_k_color = GOLD

        M = np.array([
            [2, 0, 0],
            [0, 1, 0],
            [0, 0, -1.5]
        ])

        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)

        basis_vector_helper.to_corner(UP + RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE_E)

        i_vec = Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = Vector(M @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            Create(cube),
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(k_vec),
            Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)


class LT3D_Shift(ThreeDScene):
    def create_matrix(self, np_matrix):
        m = Matrix(np_matrix)

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(UP + LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = GREEN,
        self.basis_j_color = RED,
        self.basis_k_color = GOLD

        M = np.array([
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0]
        ])

        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)

        basis_vector_helper.to_corner(UP + RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE_E)

        i_vec = Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = Vector(M @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            Create(cube),
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(k_vec),
            Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)


class LT3D_Upper(ThreeDScene):
    def create_matrix(self, np_matrix):
        m = Matrix(np_matrix)

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(UP + LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = GREEN,
        self.basis_j_color = RED,
        self.basis_k_color = GOLD

        M = np.array([
            [1, -1, 1],
            [0, 1, 1],
            [0, 0, 1]
        ])

        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)

        basis_vector_helper.to_corner(UP + RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE_E)

        i_vec = Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = Vector(np.array([0, 0, 1]), color=self.basis_k_color)

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = Vector(M @ np.array([0, 0, 1]), color=self.basis_k_color)

        self.play(
            Create(cube),
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(k_vec),
            Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)


class LT3d22d(ThreeDScene):
    def create_matrix(self, np_matrix):
        m = Matrix(np_matrix[:2,:])

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(UP + LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = GREEN,
        self.basis_j_color = RED,
        self.basis_k_color = GOLD

        M = np.array([
            [2, 2, -1],
            [-2, 1, 2],
            [0, 0, 0]
        ])

        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color(self.basis_i_color)
        basis_vector_helper[2].set_color(self.basis_j_color)
        basis_vector_helper[4].set_color(self.basis_k_color)

        basis_vector_helper.to_corner(UP + RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)
        times = Tex(r"$\times$").scale(0.75).next_to(matrix, RIGHT)
        vector = Matrix(np.array([[1, 1, 1]]).T)
        vector.scale(0.75)
        vector.next_to(times, RIGHT)

        self.add_fixed_in_frame_mobjects(matrix)
        self.add_fixed_in_frame_mobjects(times)
        self.add_fixed_in_frame_mobjects(vector)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        i_vec = Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec = Vector(np.array([0, 0, 1]), color=self.basis_k_color)
        x_vec = Vector(np.array([1, 1, 1]), color=WHITE)

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        k_vec_new = Vector(M @ np.array([0, 0, 1]), color=self.basis_k_color)
        x_vec_new = Vector(M @ np.array([1, 1, 1]), color=WHITE)

        self.play(
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(k_vec),
            GrowArrow(x_vec),
            Write(basis_vector_helper)
        )

        self.wait()

        self.play(
            Transform(i_vec, i_vec_new, run_time=1),
            Transform(j_vec, j_vec_new, run_time=1),
            Transform(k_vec, k_vec_new, run_time=1),
            Transform(x_vec, x_vec_new, run_time=1)
        )

        self.wait(2)

        # self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES, zoom=1, run_time=2)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time =2)
        self.stop_ambient_camera_rotation()

        eq = Tex(r"=").scale(0.75).next_to(vector, RIGHT)
        res = (M @ np.array([1, 1, 1]).reshape((-1, 1)))[:2,:]
        print(res)
        res = Matrix(res).scale(0.75).next_to(eq, RIGHT)
        
        i_label = i_vec_new.coordinate_label(n_dim=2, integer_labels=False, color=self.basis_i_color)
        j_label = j_vec_new.coordinate_label(n_dim=2, integer_labels=False, color=self.basis_j_color)
        k_label = k_vec_new.coordinate_label(n_dim=2, integer_labels=False, color=self.basis_k_color)
        res_label = x_vec_new.coordinate_label(n_dim=2, integer_labels=False)

        self.play(
            Create(eq),
            Create(res),
            Create(i_label),
            Create(j_label),
            Create(k_label),
            Create(res_label),
        )

        self.wait(1)


class LT2d23d(ThreeDScene):
    def create_matrix(self, np_matrix):
        m = Matrix(np_matrix[:,:2])

        m.scale(0.75)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(UP + LEFT,buff=0.5)

        return m

    def construct(self):

        self.x_axis_label = "$x$",
        self.y_axis_label = "$y$",
        self.basis_i_color = GREEN,
        self.basis_j_color = RED,
        self.basis_k_color = GOLD

        M = np.array([
            [2, 1, 0],
            [-2, 1, 0],
            [2, -1, 0]
        ])

        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        # matrix
        matrix = self.create_matrix(M)
        times = Tex(r"$\times$").scale(0.75).next_to(matrix, RIGHT)
        vector = Matrix(np.array([[1, 1]]).T)
        vector.scale(0.75)
        vector.next_to(times, RIGHT)

        self.add_fixed_in_frame_mobjects(matrix)
        self.add_fixed_in_frame_mobjects(times)
        self.add_fixed_in_frame_mobjects(vector)

        # axes & camera
        self.add(axes)

        i_vec = Vector(np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec = Vector(np.array([0, 1, 0]), color=self.basis_j_color)
        x_vec = Vector(np.array([1, 1, 0]), color=WHITE)

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color=self.basis_i_color)
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color=self.basis_j_color)
        x_vec_new = Vector(M @ np.array([1, 1, 0]), color=WHITE)

        self.play(
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(x_vec),
        )

        self.wait()

        self.play(
            Transform(i_vec, i_vec_new, run_time=1),
            Transform(j_vec, j_vec_new, run_time=1),
            Transform(x_vec, x_vec_new, run_time=1)
        )

        eq = Tex(r"=").scale(0.75).next_to(vector, RIGHT)
        res = (M @ np.array([1, 1, 1]).reshape((-1, 1)))
        print(res)
        res = Matrix(res).scale(0.75).next_to(eq, RIGHT)
        
        i_label = i_vec_new.coordinate_label(n_dim=3, integer_labels=False, color=self.basis_i_color)
        j_label = j_vec_new.coordinate_label(n_dim=3, integer_labels=False, color=self.basis_j_color)
        res_label = x_vec_new.coordinate_label(n_dim=3, integer_labels=False)
        self.add_fixed_orientation_mobjects(i_label)
        self.add_fixed_orientation_mobjects(j_label)
        self.add_fixed_orientation_mobjects(res_label)

        self.move_camera(phi=75 * DEGREES, theta=-90 * DEGREES, run_time=2)
        self.begin_ambient_camera_rotation(rate=0.3)

        self.wait(10)

class LT2d21d(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
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

        self.matrix_text = Matrix(matrix).scale(1).to_edge(UP, buff=1).to_edge(LEFT)
        times = Tex(r"$\times$").scale(0.75).next_to(self.matrix_text, RIGHT)
        vector = Matrix(np.array([[1, 2]]).T)
        vector.scale(0.75)
        vector.next_to(times, RIGHT)
        self.play(Create(self.matrix_text), Create(times), Create(vector), run_time=0.3)
        self.wait()

        matrix = np.concat([matrix, np.array([[0, 0]])], axis=0)
        print(matrix)

        self.add_vector(vec := Vector(vec_))
        self.apply_matrix(matrix)
        self.wait()

        print(np.dot(matrix, vec_.T))
        vec = vec.become(Vector(np.dot(matrix, vec_.T)))
        label = vec.coordinate_label(integer_labels=False, n_dim=1).shift(UP * 0.5)
        self.play(Create(label), run_time=0.3)

        eq = Tex(r"=").scale(0.75).next_to(vector, RIGHT)
        res = np.dot(matrix, vec_.T).reshape((-1, 1))
        print(res)
        res = Matrix(res[:1,:]).scale(0.75).next_to(eq, RIGHT)
        self.play(Create(eq), Create(res), run_time=0.3)

        self.wait(2)

class LT2d21dreversed(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
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

        self.matrix_text = Matrix(matrix).scale(1).to_edge(UP, buff=1).to_edge(LEFT)
        times = Tex(r"$\times$").scale(0.75).next_to(self.matrix_text, RIGHT)
        vector = Matrix(np.array([[1.5, 2]]).T)
        vector.scale(0.75)
        vector.next_to(times, RIGHT)
        self.play(Create(self.matrix_text), Create(times), Create(vector), run_time=0.3)
        self.wait()

        matrix = np.concat([matrix, np.array([[0, 0]])], axis=0)
        print(matrix)

        self.add_vector(vec := Vector(vec_))
        self.apply_matrix(matrix)
        self.wait()

        print(np.dot(matrix, vec_.T))
        vec = vec.become(Vector(np.dot(matrix, vec_.T)))
        label = vec.coordinate_label(integer_labels=False, n_dim=1).shift(UP * 0.5)
        self.play(Create(label), run_time=0.3)

        eq = Tex(r"=").scale(0.75).next_to(vector, RIGHT)
        res = np.dot(matrix, vec_.T).reshape((-1, 1))
        print(res)
        res = Matrix(res[:1,:]).scale(0.75).next_to(eq, RIGHT)
        self.play(Create(eq), Create(res), run_time=0.3)

        self.wait(2)

class MatrixMatrixMul1(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs
        )

    def apply_custom_matrix(self, matrix):
        matrix = np.array(matrix).T

        self.matrix_text = Matrix(matrix).scale(1).to_edge(UP, buff=1).to_edge(LEFT)
        self.play(Create(self.matrix_text), run_time=0.3)
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
        self.play(Uncreate(self.matrix_text), run_time=0.3)

        self.wait()
        matrix = [
            [-1, 1],
            [-2, -1]
        ]
        self.apply_custom_matrix(matrix)
        self.play(Uncreate(self.matrix_text), run_time=0.3)
        self.wait()

class MatrixMatrixMul2(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
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

        matrix1_text = Matrix(matrix).scale(1).to_edge(UP, buff=1).to_edge(LEFT)
        self.play(Create(matrix1_text), run_time=0.3)
        self.wait()

        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait()

        self.play(Uncreate(matrix1_text), run_time=0.3)

        matrix = [
            [1, -1],
            [1, 0.5]
        ]
        matrix = np.array(matrix).T

        matrix2_text = Matrix(matrix).scale(1).to_edge(UP, buff=1).to_edge(LEFT)
        self.play(Create(matrix2_text), run_time=0.3)
        self.wait()

        self.apply_matrix(matrix)
        self.wait()

class MatrixMatrixMul(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
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

        matrix1_text = Matrix(matrix).scale(1).to_edge(UP, buff=1).to_edge(LEFT)
        self.play(Create(matrix1_text), run_time=0.3)
        self.wait()

        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait()



        matrix = [
            [1, -1],
            [2, 1]
        ]

        self.play(Uncreate(matrix1_text), run_time=0.3)
        matrix = np.array(matrix).T

        matrix2_text = Matrix(matrix).scale(1).to_edge(UP, buff=1).to_edge(LEFT)
        self.play(Create(matrix2_text), run_time=0.3)
        self.wait()

        self.apply_matrix(matrix)
        self.wait()

class MatrixMatrixMulResult(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
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

        matrix1_text = Matrix(matrix).to_edge(UP, buff=1).to_edge(LEFT).set_column_colors(GREEN, RED)
        self.play(Create(matrix1_text), run_time=0.3)
        self.wait()

        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait()

        i1 = Matrix([[1.0], [-1.0]]).set_column_colors(GREEN).move_to(1.5 * RIGHT + 2 * DOWN)
        j1 = Matrix([[1.0], [0.5]]).set_column_colors(RED).move_to(1.5 * RIGHT + 1 * UP)
        self.play(Create(i1), Create(j1), run_time=0.3)
        self.wait(3)
        self.play(Uncreate(i1), Uncreate(j1), run_time=0.3)

        matrix = [
            [1, -1],
            [2, 1]
        ]

        # self.play(Uncreate(matrix1_text), run_time=0.3)
        matrix = np.array(matrix).T

        matrix2_text = Matrix(matrix).to_edge(UP, buff=1).to_edge(LEFT)
        times = Tex(r"$\times$").next_to(matrix2_text, RIGHT)
        self.play(matrix1_text.animate.next_to(times, RIGHT))
        self.play(Create(matrix2_text), run_time=0.3)
        self.play(Create(times), run_time=0.3)
        self.wait(2)

        self.apply_matrix(matrix)

        i1 = Matrix([[-1.0], [-2.0]]).set_column_colors(GREEN).move_to(2 * LEFT + 2 * DOWN)
        j1 = Matrix([[2.0], [-0.5]]).set_column_colors(RED).move_to(3 * RIGHT + 0.5 * DOWN)
        self.play(Create(i1), Create(j1), run_time=0.3)

        eq = Text("=").next_to(matrix1_text, RIGHT)
        matrix3_text = Matrix([[-1.0, 2.0], [-2.0, -0.5]]).next_to(eq, RIGHT).set_column_colors(GREEN, RED)
        self.play(Create(eq), Create(matrix3_text), run_time=0.3)

        self.wait()

class MatrixMatrixMulNotSymmetrical(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
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

        matrix1_text = Matrix(matrix).to_edge(UP, buff=1).to_edge(LEFT).set_column_colors(GREEN, RED)
        self.play(Create(matrix1_text), run_time=0.3)
        self.wait()

        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait()

        i1 = Matrix([[1], [-1]]).set_column_colors(GREEN).move_to(2 * RIGHT + 1 * DOWN)
        j1 = Matrix([[2], [1]]).set_column_colors(RED).move_to(3 * RIGHT + 1 * UP)
        self.play(Create(i1), Create(j1), run_time=0.3)
        self.wait(3)
        self.play(Uncreate(i1), Uncreate(j1), run_time=0.3)

        matrix = [
            [1, -1],
            [1, 0.5]
        ]

        matrix = np.array(matrix).T

        matrix2_text = Matrix(matrix).to_edge(UP, buff=1).to_edge(LEFT)
        times = Tex(r"$\times$").next_to(matrix2_text, RIGHT)
        self.play(matrix1_text.animate.next_to(times, RIGHT))
        self.play(Create(matrix2_text), run_time=0.3)
        self.play(Create(times), run_time=0.3)
        self.wait(2)

        self.apply_matrix(matrix)

        i1 = Matrix([[0.0], [-1.0]]).set_column_colors(GREEN).move_to(1 * LEFT + 1 * DOWN)
        j1 = Matrix([[3.0], [-1.0]]).set_column_colors(RED).move_to(4 * RIGHT + 1 * DOWN)
        self.play(Create(i1), Create(j1), run_time=0.3)

        eq = Text("=").next_to(matrix1_text, RIGHT)
        matrix3_text = Matrix([[0.0, 3.0], [-1.0, -1.0]]).next_to(eq, RIGHT).set_column_colors(GREEN, RED)
        self.play(Create(eq), Create(matrix3_text), run_time=0.3)

        self.wait()