import manim as m
import numpy as np
from theming import Scene_, ThreeDScene_
from pathlib import Path
import os

# ========== НАСТРОЙКА СТИЛЕЙ ==========
# Единые стили для подписей
LABEL_STYLES = {
    "function_label": {
        "font": "Arial",
        "font_size": 26,
        "color": m.BLACK,
        "weight": "NORMAL"
    },
    "domain_label": {
        "font": "Arial",
        "font_size": 24,
        "color": m.BLUE,
        "weight": "NORMAL"
    },
    "codomain_label": {
        "font": "Arial",
        "font_size": 24,
        "color": m.RED,
        "weight": "NORMAL"
    }
}

def create_label(text, style_name, **kwargs):
    """
    Создает текстовую метку с заданным стилем.
    
    Args:
        text: Текст метки
        style_name: Ключ из LABEL_STYLES
        **kwargs: Дополнительные параметры для переопределения
    """
    style = LABEL_STYLES[style_name].copy()
    style.update(kwargs)
    return m.Text(text, **style)

# ========== СЦЕНЫ ==========

class DerivativeGeometricMeaning(Scene_):
    """
    Глава 5, Анимация 1: Геометрический смысл производной.
    Точка B фиксирована, точка A приближается к B. Секущая стремится к касательной.
    """
    def construct(self):
        # 1. Координатная плоскость
        axes = m.Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-0.5, 5, 1],
            x_length=9,
            y_length=6,
            axis_config={"color": m.GRAY, "stroke_width": 1.5, "include_tip": False},
            x_axis_config={"numbers_to_include": [-2, -1, 0, 1, 2], "font_size": 18},
            y_axis_config={"numbers_to_include": [1, 2, 3, 4], "font_size": 18},
        )
        axes.shift(m.DOWN * 0.3)

        self.play(m.Create(axes), run_time=0.8)
        self.wait(0.2)

        # 2. График функции y = x² — обрезан справа до 2.3
        graph = axes.plot(
            lambda x: x**2,
            x_range=[-2.2, 2.3],
            color=m.BLUE,
            stroke_width=2.5,
        )

        graph_label = m.MathTex(
            r"y = \sin(x)",
            font_size=32,
            color=m.BLUE,  # настоящий синий, не голубой #58C4DD
        )
        graph_label.to_corner(m.UL, buff=0.5)

        self.play(m.Create(graph), run_time=1.2)
        self.play(m.Write(graph_label), run_time=0.4)
        self.wait(0.3)

        # 3. Фиксированная точка B в x=1
        x_B = 1
        y_B = x_B**2
        point_B = m.Dot(
            axes.coords_to_point(x_B, y_B),
            color=m.ORANGE,
            radius=0.08,
        )

        label_B = create_label("B", "domain_label", font_size=22)
        label_B.next_to(point_B, m.UP + m.RIGHT, buff=0.2)

        self.play(m.Create(point_B), m.Write(label_B), run_time=0.6)
        self.wait(0.3)

        # 4. Касательная в точке B (фиксированная)
        tangent = axes.plot(
            lambda x: 2 * (x - x_B) + y_B,
            x_range=[x_B - 1, x_B + 1],
            color=m.GREEN,
            stroke_width=2,
            stroke_opacity=0.7,
        )

        self.play(m.Create(tangent), run_time=0.8)
        self.wait(0.5)

        # 5. ValueTracker для h (расстояние от B до A)
        h_tracker = m.ValueTracker(0.8)

        # 6. Точка A (движущаяся, приближается к B)
        def get_point_A():
            h = h_tracker.get_value()
            x_A = x_B + h
            y_A = x_A**2
            return axes.coords_to_point(x_A, y_A)

        point_A = m.Dot(
            get_point_A(),
            color=m.RED,
            radius=0.08,
        )
        point_A.add_updater(lambda mob: mob.move_to(get_point_A()))

        label_A = create_label("A", "domain_label", font_size=22)
        label_A.add_updater(lambda mob: mob.next_to(point_A, m.UP + m.LEFT, buff=0.2))

        self.play(m.Create(point_A), m.Write(label_A), run_time=0.6)
        self.wait(0.3)

        # 7. Секущая через A и B
        def get_secant():
            h = h_tracker.get_value()
            x_A = x_B + h
            y_A = x_A**2
            
            slope = (y_A - y_B) / h
            
            return axes.plot(
                lambda x: slope * (x - x_B) + y_B,
                x_range=[x_B - 0.3, x_A + 0.3],
                color=m.RED,
                stroke_width=2,
            )

        secant = get_secant()
        secant.add_updater(lambda mob: mob.become(get_secant()))

        self.play(m.Create(secant), run_time=0.6)
        self.wait(0.3)

        # 8. Формула наклона — мелкая, чёрная, в правом верхнем углу
        '''slope_formula = create_label(
            "k = (f(x₀+h) − f(x₀)) / h",
            "function_label",
            font_size=18,
        )
        slope_formula.to_corner(m.UR, buff=0.6)

        self.play(m.Write(slope_formula), run_time=0.6)
        self.wait(0.5)'''

        # 9. Анимация: h уменьшается, A приближается к B
        self.play(
            h_tracker.animate.set_value(0.05),
            run_time=6,
            rate_func=m.smooth,
        )
        self.wait(0.5)

        # 10. Финальная подпись
        final_note = create_label(
            "Чем меньше h, тем ближе секущая к касательной",
            "function_label",
            font_size=22,
        )
        final_note.to_edge(m.UP, buff=0.8)

        self.play(m.Write(final_note), run_time=0.8)
        self.wait(2)

        # Очистка апдейтеров
        point_A.clear_updaters()
        label_A.clear_updaters()
        secant.clear_updaters()
class DerivativeAsFunction(Scene_):
    """
    Глава 5, Анимация 2: Производная как функция.
    Показывает f(x) = x³ - 3x и f'(x) = 3x² - 3 на одних осях.
    Пунктирные линии связывают экстремумы f с нулями f'.
    """
    def construct(self):
        # 1. Координатная плоскость
        axes = m.Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-4, 4, 1],
            x_length=9,
            y_length=6,
            axis_config={"color": m.GRAY, "stroke_width": 1.5, "include_tip": False},
            x_axis_config={"numbers_to_include": [-2, -1, 0, 1, 2], "font_size": 18},
            y_axis_config={"numbers_to_include": [-3, -2, -1, 1, 2, 3], "font_size": 18},
        )
        axes.shift(m.DOWN * 0.3)

        self.play(m.Create(axes), run_time=0.8)
        self.wait(0.2)

        # 2. График f(x) = x³ - 3x
        f_graph = axes.plot(
            lambda x: x**3 - 3*x,
            x_range=[-2.2, 2.2],
            color=m.BLUE,
            stroke_width=2.5,
        )

        f_label = create_label("f(x) = x³ − 3x", "domain_label", font_size=20)
        f_label.set_color(m.BLUE)
        f_label.next_to(f_graph.get_end(), m.RIGHT, buff=0.1)

        self.play(m.Create(f_graph), run_time=1.2)
        self.play(m.Write(f_label), run_time=0.4)
        self.wait(0.3)

        # 3. График f'(x) = 3x² - 3
        fp_graph = axes.plot(
            lambda x: 3*x**2 - 3,
            x_range=[-2.2, 2.2],
            color=m.RED,
            stroke_width=2.5,
        )

        fp_label = create_label("f'(x) = 3x² − 3", "codomain_label", font_size=20)
        fp_label.to_edge(m.UP, buff=0.8)      # небольшой отступ сверху
        fp_label.shift(m.LEFT * 1.2)         # большой отступ слева (сдвиг вправо от левого края)

        self.play(m.Create(fp_graph), run_time=1.2)
        self.play(m.Write(fp_label), run_time=0.4)
        self.wait(0.5)

        # 4. Точки экстремумов f(x) при x = ±1
        # f(-1) = -1 + 3 = 2 (локальный максимум)
        # f(1) = 1 - 3 = -2 (локальный минимум)
        extremum_points = m.VGroup()
        for x_ext, y_ext in [(-1, 2), (1, -2)]:
            dot = m.Dot(
                axes.coords_to_point(x_ext, y_ext),
                color=m.BLUE,
                radius=0.08,
            )
            extremum_points.add(dot)

        self.play(m.Create(extremum_points), run_time=0.6)
        self.wait(0.3)

        # 5. Нули f'(x) при x = ±1 (f'(±1) = 0)
        zero_points = m.VGroup()
        for x_zero in [-1, 1]:
            dot = m.Dot(
                axes.coords_to_point(x_zero, 0),
                color=m.RED,
                radius=0.08,
            )
            zero_points.add(dot)

        self.play(m.Create(zero_points), run_time=0.6)
        self.wait(0.3)

        # 6. Вертикальные пунктирные линии, связывающие экстремумы с нулями
        dashed_lines = m.VGroup()
        for x_val in [-1, 1]:
            # Линия от (x, f(x)) до (x, 0)
            y_top = x_val**3 - 3*x_val  # значение f(x)
            line = m.DashedLine(
                start=axes.coords_to_point(x_val, y_top),
                end=axes.coords_to_point(x_val, 0),
                color=m.YELLOW,
                stroke_width=2,
                dash_length=0.1,
            )
            dashed_lines.add(line)

        self.play(m.Create(dashed_lines), run_time=0.8)
        self.wait(2)

class ZoomToTangent(Scene_):
    """
    Глава 5, Анимация: От производной к линейному приближению.
    Камера приближается к точке на графике, кривая становится прямой.
    """
    def construct(self):
        # 1. Координатная плоскость
        axes = m.Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": m.GRAY, "stroke_width": 1.5, "include_tip": False},
            x_axis_config={"numbers_to_include": [-2, -1, 0, 1, 2], "font_size": 18},
            y_axis_config={"numbers_to_include": [-1, 1], "font_size": 18},
        )
        axes.shift(m.DOWN * 0.3)

        self.play(m.Create(axes), run_time=0.8)
        self.wait(0.2)

        # 2. График функции y = sin(x)
        graph = axes.plot(
            lambda x: np.sin(x),
            x_range=[-3, 3],
            color=m.BLUE,
            stroke_width=2.5,
        )

        graph_label = m.MathTex(
            r"y = \sin(x)",
            font_size=32,
            color=m.BLUE,  # настоящий синий, не голубой #58C4DD
        )
        graph_label.to_corner(m.UL, buff=1)  # левый верхний угол

        self.play(m.Create(graph), run_time=1.2)
        self.play(m.Write(graph_label), run_time=0.4)
        self.wait(0.5)

        # 3. Точка, к которой будем зумиться (x = 0.5)
        x0 = 0.5
        y0 = np.sin(x0)
        target_point = axes.coords_to_point(x0, y0)

        # Маркер точки
        point_marker = m.Dot(
            target_point,
            color=m.RED,
            radius=0.1,
        )

        label_x0 = m.MathTex(
            rf"x_0 = {x0}",
            font_size=28,
            color=m.RED,  # или любой нужный цвет
        )
        label_x0.next_to(point_marker, m.DOWN, buff=0.3)


        self.play(m.Create(point_marker), m.Write(label_x0), run_time=0.6)
        self.wait(0.5)

        # 4. Касательная в точке x0
        slope = np.cos(x0)
        tangent = axes.plot(
            lambda x: slope * (x - x0) + y0,
            x_range=[x0 - 1.5, x0 + 1.5],
            color=m.GREEN,
            stroke_width=2,
            stroke_opacity=0.7,
        )

        tangent_label = create_label("касательная", "function_label", font_size=20)
        tangent_label.next_to(tangent.get_end(), m.RIGHT, buff=0.2)

        self.play(m.Create(tangent), m.Write(tangent_label), run_time=0.8)
        self.wait(0.5)

        # 5. Подпись перед зумом
        zoom_note = create_label(
            "Приближаемся к точке...",
            "function_label",
            font_size=22,
        )
        zoom_note.to_edge(m.UP, buff=0.3)

        self.play(m.Write(zoom_note), run_time=0.6)
        self.wait(0.5)

        # 6. Анимация зума через масштабирование VGroup
        # Собираем все объекты сцены в одну группу
        scene_group = m.VGroup(
            axes, graph, graph_label,
            point_marker, label_x0,
            tangent, tangent_label,
            zoom_note,
        )

        # Параметры зума
        zoom_factor = 9  # во сколько раз увеличить

        # Анимация: масштабируем относительно целевой точки,
        # затем сдвигаем так, чтобы точка оказалась в центре экрана
        self.play(
            scene_group.animate
                .scale(zoom_factor, about_point=target_point)
                .shift(m.ORIGIN - target_point),
            run_time=6,
            rate_func=m.smooth,
        )
        self.wait(1)

        # 7. Финальная подпись (появляется уже после зума, в новых координатах)
        final_note = create_label(
            "В пределе кривая = касательная",
            "function_label",
            font_size=24,
        )
        # Располагаем внизу экрана в текущих (отмасштабированных) координатах
        final_note.to_edge(m.DOWN, buff=0.8)

        self.play(m.Write(final_note), run_time=0.8)
        self.wait(2)
class GradientDescent(Scene_):
    """
    Глава 5, Анимация: Градиентный спуск на параболе L(w) = (w-3)².
    Шарик скатывается от w=0 к минимуму w=3, касательная показывает направление шага.
    """
    def construct(self):
        # 1. Координатная плоскость
        axes = m.Axes(
            x_range=[-1, 6, 1],
            y_range=[-1, 10, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": m.GRAY, "stroke_width": 1.5, "include_tip": False},
            x_axis_config={"numbers_to_include": [0, 1, 2, 3, 4, 5], "font_size": 18},
            y_axis_config={"numbers_to_include": [2, 4, 6, 8], "font_size": 18},
        )
        axes.shift(m.DOWN * 0.3)

        self.play(m.Create(axes), run_time=0.8)
        self.wait(0.2)

        # 2. График параболы L(w) = (w-3)²
        parabola = axes.plot(
            lambda w: (w - 3)**2,
            x_range=[-0.1, 5.5],
            color=m.BLUE,
            stroke_width=2.5,
        )

        parabola_label = m.MathTex(
            r"L(w) = (w - 3)^2",
            font_size=28,
            color=m.BLUE,
        )
        parabola_label.to_corner(m.UL, buff=1)
        parabola_label.shift(m.RIGHT * 2)

        self.play(m.Create(parabola), run_time=1.2)
        self.play(m.Write(parabola_label), run_time=0.4)
        self.wait(0.3)

        # 3. Точка минимума (w=3, L=0)
        min_point = m.Dot(
            axes.coords_to_point(3, 0),
            color=m.GREEN,
            radius=0.1,
        )
        min_label = m.MathTex(
            r"w^* = 3",
            font_size=24,
            color=m.GREEN,
        )
        min_label.next_to(min_point, m.DOWN, buff=0.3)

        self.play(m.Create(min_point), m.Write(min_label), run_time=0.6)
        self.wait(0.5)

        # 4. ValueTracker для текущей позиции w
        w_tracker = m.ValueTracker(0.0)  # начинаем с w=0
        learning_rate = 0.3  # скорость обучения (меньше 0.5 для наглядности)

        # 5. Шарик (текущая точка)
        def get_ball_position():
            w = w_tracker.get_value()
            L = (w - 3)**2
            return axes.coords_to_point(w, L)

        ball = m.Dot(
            get_ball_position(),
            color=m.RED,
            radius=0.12,
        )
        ball.add_updater(lambda mob: mob.move_to(get_ball_position()))

        # Подпись текущей позиции
        w_label = m.MathTex(
            "w = 0.0",
            font_size=24,
            color=m.RED,
        )
        w_label.add_updater(lambda mob: mob.next_to(ball, m.UP, buff=0.3))
        w_label.add_updater(lambda mob: mob.set_text(f"w = {w_tracker.get_value():.2f}"))

        self.play(m.Create(ball), m.Write(w_label), run_time=0.6)
        self.wait(0.5)

        # 6. Касательная в текущей точке
        def get_tangent():
            w = w_tracker.get_value()
            L = (w - 3)**2
            slope = 2 * (w - 3)  # L'(w) = 2(w-3)
            
            # Уравнение касательной: y = slope * (w - w_current) + L_current
            return axes.plot(
                lambda x: slope * (x - w) + L,
                x_range=[w - 1, w + 1],
                color=m.ORANGE,
                stroke_width=2,
                stroke_opacity=0.8,
            )

        tangent = get_tangent()
        tangent.add_updater(lambda mob: mob.become(get_tangent()))

        self.play(m.Create(tangent), run_time=0.8)
        self.wait(0.5)

        # 7. Формула обновления
        update_formula = m.MathTex(
            r"w_{t+1} = w_t - \eta \cdot L'(w_t)",
            font_size=26,
            color=m.BLACK,
        )
        update_formula.to_corner(m.UR, buff=1.5)

        eta_label = m.MathTex(
            r"\eta = 0.3",
            font_size=22,
            color=m.BLACK,
        )
        eta_label.next_to(update_formula, m.DOWN, buff=0.2)

        self.play(m.Write(update_formula), m.Write(eta_label), run_time=0.8)
        self.wait(0.5)

        # 8. Анимация градиентного спуска (несколько шагов)
        # Шаг 1: w = 0 → w = 0 + 0.3*6 = 1.8
        self.play(
            w_tracker.animate.set_value(1.8),
            run_time=2,
            rate_func=m.smooth,
        )
        self.wait(0.5)

        # Шаг 2: w = 1.8 → w = 1.8 + 0.3*2.4 = 2.52
        self.play(
            w_tracker.animate.set_value(2.52),
            run_time=2,
            rate_func=m.smooth,
        )
        self.wait(0.5)

        # Шаг 3: w = 2.52 → w = 2.52 + 0.3*0.96 = 2.808
        self.play(
            w_tracker.animate.set_value(2.808),
            run_time=2,
            rate_func=m.smooth,
        )
        self.wait(0.5)

        # Шаг 4: w = 2.808 → w ≈ 2.966
        self.play(
            w_tracker.animate.set_value(2.966),
            run_time=2,
            rate_func=m.smooth,
        )
        self.wait(0.5)

        # Финальный шаг к минимуму
        self.play(
            w_tracker.animate.set_value(3.0),
            run_time=1.5,
            rate_func=m.smooth,
        )
        self.wait(1)

        # 9. Финальная подпись
        final_note = create_label(
            "Градиентный спуск сходится к минимуму",
            "function_label",
            font_size=22,
        )
        final_note.to_edge(m.DOWN, buff=0.3)

        self.play(m.Write(final_note), run_time=0.8)
        self.wait(2)

        # Очистка апдейтеров
        ball.clear_updaters()
        w_label.clear_updaters()
        tangent.clear_updaters()

class ActivationFunctions(Scene_):
    """
    Глава 5, Анимация: Сравнение ReLU, softplus и асимптоты y=x.
    Показывает, как softplus плавно аппроксимирует ReLU.
    """
    def construct(self):
        # 1. Координатная плоскость
        axes = m.Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 4, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": m.GRAY, "stroke_width": 1.5, "include_tip": False},
            x_axis_config={"numbers_to_include": [-2, -1, 0, 1, 2], "font_size": 18},
            y_axis_config={"numbers_to_include": [1, 2, 3], "font_size": 18},
        )
        axes.shift(m.DOWN * 0.3)

        self.play(m.Create(axes), run_time=0.8)
        self.wait(0.2)

        # 2. Асимптота y = x (пунктир, серый)
        asymptote = m.DashedLine(
            start=axes.c2p(-2.5, -2.5),
            end=axes.c2p(2.5, 2.5),
            color=m.GRAY,
            stroke_width=1.5,
            stroke_opacity=0.5,
            dash_length=0.15,
        )

        asymptote_label = m.MathTex(
            r"y = x",
            font_size=22,
            color=m.GRAY,
        )
        asymptote_label.next_to(asymptote.get_end(), m.RIGHT, buff=0.2)

        self.play(m.Create(asymptote), m.Write(asymptote_label), run_time=0.8)
        self.wait(0.3)

        # 3. ReLU: max(0, x)
        relu = axes.plot(
            lambda x: max(0, x),
            x_range=[-2.5, 2.5],
            color=m.BLUE,
            stroke_width=2.5,
        )

        relu_label = m.MathTex(
            r"\text{ReLU}(x) = \max(0, x)",
            font_size=22,
            color=m.BLUE,
        )
        relu_label.to_corner(m.UL, buff=1)
        relu_label.shift(m.RIGHT * 1.5)

        self.play(m.Create(relu), run_time=1.2)
        self.play(m.Write(relu_label), run_time=0.4)
        self.wait(0.3)

        # 4. Softplus: ln(1 + e^x)
        softplus = axes.plot(
            lambda x: np.log(1 + np.exp(x)),
            x_range=[-2.5, 2.5],
            color=m.RED,
            stroke_width=2.5,
        )

        softplus_label = m.MathTex(
            r"\text{softplus}(x) = \ln(1 + e^x)",
            font_size=22,
            color=m.RED,
        )
        softplus_label.next_to(relu_label, m.DOWN, buff=0.3)
        softplus_label.align_to(relu_label, m.LEFT)

        self.play(m.Create(softplus), run_time=1.2)
        self.play(m.Write(softplus_label), run_time=0.4)
        self.wait(0.5)

        # 6. Финальная подпись
        final_note = create_label(
            "Softplus → ReLU при |x| → ∞",
            "function_label",
            font_size=24,
        )
        final_note.to_edge(m.UR, buff=1)

        self.play(m.Write(final_note), run_time=0.8)
        self.wait(2)

class TaylorApproximation(Scene_):
    """
    Глава 5, Анимация: Приближения Тейлора для e^x.
    Последовательно накладываются полиномы возрастающего порядка.
    """
    def construct(self):
        # 1. Координатная плоскость
        axes = m.Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 5, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": m.GRAY, "stroke_width": 1.5, "include_tip": False},
            x_axis_config={"numbers_to_include": [-2, -1, 0, 1, 2], "font_size": 18},
            y_axis_config={"numbers_to_include": [1, 2, 3, 4], "font_size": 18},
        )
        axes.shift(m.DOWN * 0.3)

        self.play(m.Create(axes), run_time=0.8)
        self.wait(0.2)

        # 2. График функции e^x
        exp_graph = axes.plot(
            lambda x: np.exp(x),
            x_range=[-2.5, 2.5],
            color=m.BLACK,
            stroke_width=3,
        )

        exp_label = m.MathTex(
            r"e^x",
            font_size=28,
            color=m.BLACK,
        )
        exp_label.next_to(exp_graph.get_end(), m.RIGHT, buff=0.2)
        exp_label.shift(m.UP * 0.3)

        self.play(m.Create(exp_graph), run_time=1.2)
        self.play(m.Write(exp_label), run_time=0.4)
        self.wait(0.5)

        # 3. Приближения Тейлора (разные цвета для каждого порядка)
        colors = [m.RED, m.ORANGE, m.GREEN, m.BLUE, m.PURPLE]
        
        # P0(x) = 1
        taylor_0 = axes.plot(
            lambda x: 1,
            x_range=[-2.5, 2.5],
            color=colors[0],
            stroke_width=2,
        )
        
        label_0 = m.MathTex(
            r"P_0(x) = 1",
            font_size=20,
            color=colors[0],
        )
        label_0.to_corner(m.UL, buff=1)

        self.play(m.Create(taylor_0), m.Write(label_0), run_time=1)
        self.wait(0.8)

        # P1(x) = 1 + x
        taylor_1 = axes.plot(
            lambda x: 1 + x,
            x_range=[-2.5, 2.5],
            color=colors[1],
            stroke_width=2,
        )
        
        label_1 = m.MathTex(
            r"P_1(x) = 1 + x",
            font_size=20,
            color=colors[1],
        )
        label_1.next_to(label_0, m.DOWN, buff=0.2)

        self.play(m.Create(taylor_1), m.Write(label_1), run_time=1)
        self.wait(0.8)

        # P2(x) = 1 + x + x²/2
        taylor_2 = axes.plot(
            lambda x: 1 + x + x**2/2,
            x_range=[-2.5, 2.5],
            color=colors[2],
            stroke_width=2,
        )
        
        label_2 = m.MathTex(
            r"P_2(x) = 1 + x + \frac{x^2}{2}",
            font_size=20,
            color=colors[2],
        )
        label_2.next_to(label_1, m.DOWN, buff=0.2)

        self.play(m.Create(taylor_2), m.Write(label_2), run_time=1)
        self.wait(0.8)

        # P3(x) = 1 + x + x²/2 + x³/6
        taylor_3 = axes.plot(
            lambda x: 1 + x + x**2/2 + x**3/6,
            x_range=[-2.5, 2.5],
            color=colors[3],
            stroke_width=2,
        )
        
        label_3 = m.MathTex(
            r"P_3(x) = 1 + x + \frac{x^2}{2} + \frac{x^3}{6}",
            font_size=20,
            color=colors[3],
        )
        label_3.next_to(label_2, m.DOWN, buff=0.2)

        self.play(m.Create(taylor_3), m.Write(label_3), run_time=1)
        self.wait(0.8)

        # P4(x) = 1 + x + x²/2 + x³/6 + x⁴/24
        taylor_4 = axes.plot(
            lambda x: 1 + x + x**2/2 + x**3/6 + x**4/24,
            x_range=[-2.5, 2.5],
            color=colors[4],
            stroke_width=2,
        )
        
        label_4 = m.MathTex(
            r"P_4(x) = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24}",
            font_size=20,
            color=colors[4],
        )
        label_4.next_to(label_3, m.DOWN, buff=0.2)

        self.play(m.Create(taylor_4), m.Write(label_4), run_time=1)
        self.wait(1)

        # 4. Финальная подпись
        final_note = create_label(
            "Чем выше порядок, тем лучше приближение в окрестности нуля",
            "function_label",
            font_size=22,
        )
        final_note.to_edge(m.DOWN, buff=0.3)

        self.play(m.Write(final_note), run_time=0.8)
        self.wait(2)

class NewtonMethod(Scene_):
    """
    Глава 5, Анимация: Метод Ньютона для оптимизации.
    Квадратичные приближения Тейлора быстро сходятся к минимуму.
    """
    def construct(self):
        # 1. Координатная плоскость
        axes = m.Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 10, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": m.GRAY, "stroke_width": 1.5, "include_tip": False},
            x_axis_config={"numbers_to_include": [0, 1, 2, 3, 4], "font_size": 18},
            y_axis_config={"numbers_to_include": [2, 4, 6, 8], "font_size": 18},
        )
        axes.shift(m.DOWN * 0.3)

        self.play(m.Create(axes), run_time=0.8)
        self.wait(0.2)

        # 2. График функции потерь L(x) = (x-3)² + 0.5·(x-3)⁴
        def L(x):
            return (x - 3)**2 + 0.5 * (x - 3)**4

        def L_prime(x):
            return 2 * (x - 3) + 2 * (x - 3)**3

        def L_double_prime(x):
            return 2 + 6 * (x - 3)**2

        loss_graph = axes.plot(
            L,
            x_range=[-0.5, 4.5],
            color=m.BLUE,
            stroke_width=2.5,
        )

        # ИСПРАВЛЕНО: надпись L(x) ниже и левее
        loss_label = m.MathTex(
            r"L(x) = (x-3)^2 + \frac{1}{2}(x-3)^4",
            font_size=22,
            color=m.BLUE,
        )
        loss_label.to_corner(m.UL, buff=0.8)  # левый край
        #loss_label.shift(m.UP * 1.5)  # ниже верхнего края

        self.play(m.Create(loss_graph), run_time=1.2)
        self.play(m.Write(loss_label), run_time=0.4)
        self.wait(0.3)

        # 3. Точка минимума
        min_point = m.Dot(
            axes.coords_to_point(3, 0),
            color=m.GREEN,
            radius=0.1,
        )
        min_label = m.MathTex(
            r"x^* = 3",
            font_size=24,
            color=m.GREEN,
        )
        min_label.next_to(min_point, m.DOWN, buff=0.3)

        self.play(m.Create(min_point), m.Write(min_label), run_time=0.6)
        self.wait(0.5)

        # 4. Формула метода Ньютона
        newton_formula = m.MathTex(
            r"x_{k+1} = x_k - \frac{L'(x_k)}{L''(x_k)}",
            font_size=26,
            color=m.BLACK,
        )
        # ИСПРАВЛЕНО: надпись newton_formula ниже
        newton_formula.to_corner(m.UR, buff=0.8)  # правый край
        #newton_formula.shift(m.UP * 1.5)  # ниже верхнего края

        self.play(m.Write(newton_formula), run_time=0.8)
        self.wait(0.5)

        # 5. Начальная точка x₀ = 0
        x_current = 0.0

        point_0 = m.Dot(
            axes.coords_to_point(x_current, L(x_current)),
            color=m.RED,
            radius=0.1,
        )
        label_0 = m.MathTex(
            "x_0 = 0",
            font_size=22,
            color=m.RED,
        )
        label_0.next_to(point_0, m.UP, buff=0.3)

        self.play(m.Create(point_0), m.Write(label_0), run_time=0.6)
        self.wait(0.5)

        # 6. Итерации метода Ньютона
        colors = [m.ORANGE, m.GREEN, m.PURPLE, m.YELLOW]
        x_values = [0.0]
        parabolas_group = m.VGroup()  # группа всех парабол для управления прозрачностью

        for k in range(4):
            x_k = x_values[-1]
            L_k = L(x_k)
            L_prime_k = L_prime(x_k)
            L_double_prime_k = L_double_prime(x_k)

            # Шаг Ньютона
            x_next = x_k - L_prime_k / L_double_prime_k
            x_values.append(x_next)

            # Построить параболу-приближение в точке x_k
            def parabola(x, xk=x_k, Lk=L_k, Lpk=L_prime_k, Lppk=L_double_prime_k):
                return Lk + Lpk * (x - xk) + 0.5 * Lppk * (x - xk)**2

            parabola_curve = axes.plot(
                parabola,
                x_range=[x_k - 1.5, x_k + 1.5],
                color=colors[k],
                stroke_width=2,
                stroke_opacity=0.8,
            )
            parabolas_group.add(parabola_curve)

            parabola_label = m.MathTex(
                f"P_{k}(x)",
                font_size=20,
                color=colors[k],
            )
            parabola_label.next_to(parabola_curve.get_end(), m.RIGHT, buff=0.2)

            self.play(m.Create(parabola_curve), m.Write(parabola_label), run_time=1)
            self.wait(0.5)

            # Вершина параболы = следующая точка x_{k+1}
            vertex_point = m.Dot(
                axes.coords_to_point(x_next, L(x_next)),
                color=colors[k],
                radius=0.1,
            )
            vertical_line = m.DashedLine(
                start=axes.coords_to_point(x_next, parabola(x_next)),  # вершина параболы
                end=axes.coords_to_point(x_next, L(x_next)),           # реальная функция
                color=m.WHITE,
                stroke_width=1.5,
                dash_length=0.1,
            )

            '''error_label = m.MathTex(
                "\\text{ошибка}",
                font_size=16,
                color=m.WHITE,
            )
            error_label.next_to(vertical_line, m.RIGHT, buff=0.2)'''

            self.play(m.Create(vertical_line), run_time=0.6)
            self.wait(0.5)
            vertex_label = m.MathTex(
                f"x_{k+1} = {x_next:.2f}",
                font_size=20,
                color=colors[k],
            )
            vertex_label.next_to(vertex_point, m.UP, buff=0.3)

            self.play(m.Create(vertex_point), m.Write(vertex_label), run_time=0.8)
            self.wait(0.8)

            # ИСПРАВЛЕНО: старые параболы становятся бледнее, а не исчезают
            if k < 3:
                # Делаем все предыдущие параболы бледнее
                for i, para in enumerate(parabolas_group[:-1]):
                    self.play(
                        para.animate.set_stroke(opacity=0.2),
                        run_time=0.3,
                    )
                
                # Убираем старые точки и подписи
                self.play(
                    m.FadeOut(point_0 if k == 0 else vertex_point),
                    m.FadeOut(label_0 if k == 0 else vertex_label),
                    run_time=0.3,
                )

            point_0 = vertex_point
            label_0 = vertex_label

        self.wait(2)

class PartialDerivatives(ThreeDScene_):
    """
    Глава 4, Анимация 9: Частные производные.
    Трёхмерная поверхность f(x, y) = 0.5·(x² + y²) с двумя кривыми:
    красная — при фиксированном y, синяя — при фиксированном x.
    В точке пересечения показаны касательные к этим кривым.
    """
    def construct(self):
        # 1. Трёхмерные оси
        axes = m.ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-0.5, 4, 1],
            x_length=6,
            y_length=6,
            z_length=4,
            axis_config={"color": m.GRAY, "stroke_width": 2, "include_tip": False},
        )
        # Опускаем всю систему координат ниже
        axes.shift(m.DOWN * 2.0)

        # 2. Поверхность f(x, y) = 0.5·(x² + y²)
        def f(x, y):
            return 0.5 * (x ** 2 + y ** 2)

        surface = m.Surface(
            lambda u, v: axes.c2p(u, v, f(u, v)),
            u_range=[-2.5, 2.5],
            v_range=[-2.5, 2.5],
            resolution=(30, 30),
            fill_opacity=0.35,
            stroke_width=0.5,
            stroke_opacity=0.4,
            fill_color=m.BLUE_E,
        )

        # 3. Фиксированные значения x₀ и y₀
        x0 = 1.0
        y0 = -1.2

        z0 = f(x0, y0)
        point_3d = axes.c2p(x0, y0, z0)
        point_dot = m.Dot3D(point_3d, color=m.YELLOW, radius=0.08)

        # 4. Красная кривая: при фиксированном y = y0
        curve_red = m.ParametricFunction(
            lambda t: axes.c2p(t, y0, f(t, y0)),
            t_range=[-2.5, 2.5, 0.05],
            color=m.RED,
            stroke_width=4,
        )

        # 5. Синяя кривая: при фиксированном x = x0
        curve_blue = m.ParametricFunction(
            lambda t: axes.c2p(x0, t, f(x0, t)),
            t_range=[-2.5, 2.5, 0.05],
            color=m.BLUE,
            stroke_width=4,
        )

        # 6. Касательные
        df_dx = x0
        df_dy = y0

        tangent_red_len = 1.5
        tangent_red = m.Line3D(
            start=axes.c2p(x0 - tangent_red_len, y0, z0 - df_dx * tangent_red_len),
            end=axes.c2p(x0 + tangent_red_len, y0, z0 + df_dx * tangent_red_len),
            color=m.RED_A,
            stroke_width=5,
        )

        tangent_blue_len = 1.5
        tangent_blue = m.Line3D(
            start=axes.c2p(x0, y0 - tangent_blue_len, z0 - df_dy * tangent_blue_len),
            end=axes.c2p(x0, y0 + tangent_blue_len, z0 + df_dy * tangent_blue_len),
            color=m.BLUE_A,
            stroke_width=5,
        )

        # 7. 3D-подписи
        red_label = m.MathTex(r"y = y_0", color=m.RED, font_size=26)
        red_label.move_to(axes.c2p(2.3, y0, f(2.3, y0) + 0.3))

        blue_label = m.MathTex(r"x = x_0", color=m.BLUE, font_size=26)
        blue_label.move_to(axes.c2p(x0, 2.3, f(x0, 2.3) + 0.3))

        point_label = m.MathTex(r"(x_0, y_0)", color=m.YELLOW, font_size=24)
        point_label.move_to(axes.c2p(x0, y0, z0 + 0.4))

        # 8. Формула — в левом нижнем углу
        formula = m.MathTex(
            r"\frac{\partial f}{\partial x}\bigg|_{(x_0, y_0)} = " + f"{df_dx:.2f}"
            + r",\quad \frac{\partial f}{\partial y}\bigg|_{(x_0, y_0)} = " + f"{df_dy:.2f}",
            font_size=24,
            color=m.BLACK,
        )
        formula.to_corner(m.DL, buff=0.5)

        # 9. Заголовок — под формулой
        title = m.Text(
            "Частные производные: наклон вдоль осей",
            font_size=22,
            color=m.BLACK,
        )
        title.next_to(formula, m.UP, buff=0.8)
        title.align_to(formula, m.LEFT)

        # 10. Пояснительная подпись — справа внизу
        note = m.Text(
            "Красная касательная — ∂f/∂x, синяя — ∂f/∂y",
            font_size=20,
            color=m.BLACK,
        )
        note.to_corner(m.DR, buff=0.5)

        # ========== АНИМАЦИЯ ==========
        self.set_camera_orientation(phi=65 * m.DEGREES, theta=-55 * m.DEGREES, zoom=0.75)

        # 1. Оси
        self.play(m.Create(axes), run_time=1)
        self.wait(0.2)

        # 2. Поверхность
        self.play(m.Create(surface), run_time=2)
        self.wait(0.3)

        # 3. Точка
        self.play(m.Create(point_dot), run_time=0.5)
        self.wait(0.2)

        # 4. Красная кривая
        self.play(m.Create(curve_red), run_time=1.5)
        self.wait(0.2)

        # 5. Синяя кривая
        self.play(m.Create(curve_blue), run_time=1.5)
        self.wait(0.2)

        # 6. Касательные
        self.play(m.Create(tangent_red), run_time=0.8)
        self.play(m.Create(tangent_blue), run_time=0.8)
        self.wait(0.3)

        # 7. 3D-подписи
        self.play(
            m.Write(red_label),
            m.Write(blue_label),
            m.Write(point_label),
            run_time=0.8,
        )
        self.wait(0.3)

        # 8. Формула, заголовок и подпись на экране
        self.add_fixed_in_frame_mobjects(formula, title, note)
        self.play(m.Write(formula), m.Write(title), m.Write(note), run_time=0.8)
        self.wait(0.3)

        # 9. Вращение камеры
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)
        self.stop_ambient_camera_rotation()

        self.wait(1)

class PartialDerivatives2(ThreeDScene_):
    """
    Глава 6, Анимация 1: Частные производные.
    Трёхмерная поверхность с двумя кривыми (при фиксированных x и y)
    и касательными в точке пересечения.
    """
    def construct(self):
        # 1. Оси
        axes = m.ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-2, 2, 1],
            x_length=6,
            y_length=6,
            z_length=4,
            axis_config={"color": m.GRAY, "stroke_width": 2, "include_tip": False},
        )
        axes.shift(m.DOWN * 0.5)  # было 1.8 — подняли на 0.7

        # 2. Бугристая поверхность
        def f(x, y):
            return 0.5 * np.sin(x) * np.cos(y) + 0.1 * x * y

        surface = m.Surface(
            lambda u, v: axes.c2p(u, v, f(u, v)),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(60, 60),
            fill_opacity=0.45,
            stroke_width=0.3,
            stroke_opacity=0.3,
            fill_color=m.BLUE_E,
        )

        # 3. Точка пересечения
        x0 = 1.0
        y0 = -0.8
        z0 = f(x0, y0)

        point_dot = m.Dot3D(axes.c2p(x0, y0, z0), color=m.YELLOW, radius=0.08)

        # 4. Кривые сечений
        curve_red = m.ParametricFunction(
            lambda t: axes.c2p(t, y0, f(t, y0)),
            t_range=[-3, 3, 0.02],
            color=m.RED,
            stroke_width=4,
        )

        curve_blue = m.ParametricFunction(
            lambda t: axes.c2p(x0, t, f(x0, t)),
            t_range=[-3, 3, 0.02],
            color=m.BLUE,
            stroke_width=4,
        )

        # 5. Частные производные
        df_dx = 0.5 * np.cos(x0) * np.cos(y0) + 0.1 * y0
        df_dy = -0.5 * np.sin(x0) * np.sin(y0) + 0.1 * x0

        # 6. Касательные как параметрические прямые
        tangent_red_len = 1.5
        tangent_red = m.ParametricFunction(
            lambda t: axes.c2p(
                x0 + t,
                y0,
                z0 + df_dx * t,
            ),
            t_range=[-tangent_red_len, tangent_red_len, 0.05],
            color=m.RED_A,
            stroke_width=6,
        )

        tangent_blue_len = 1.5
        tangent_blue = m.ParametricFunction(
            lambda t: axes.c2p(
                x0,
                y0 + t,
                z0 + df_dy * t,
            ),
            t_range=[-tangent_blue_len, tangent_blue_len, 0.05],
            color=m.BLUE_A,
            stroke_width=6,
        )

        # 7. Подписи к кривым
        red_label = m.MathTex(r"y = y_0", color=m.RED, font_size=24)
        red_label.move_to(axes.c2p(2.5, y0, f(2.5, y0) + 0.3))

        blue_label = m.MathTex(r"x = x_0", color=m.BLUE, font_size=24)
        blue_label.move_to(axes.c2p(x0, 2.5, f(x0, 2.5) + 0.3))

        point_label = m.MathTex(r"(x_0, y_0)", color=m.YELLOW, font_size=22)
        point_label.move_to(axes.c2p(x0, y0, z0 + 0.35))

        # 8. Формула

        title = m.Text(
            "Наклон красной касательной — ∂f/∂x, синей — ∂f/∂y",
            font_size=22,
            color=m.BLACK,
        )
        title.to_corner(m.UL, buff=0.8)  

        # ========== АНИМАЦИЯ ==========
        self.set_camera_orientation(phi=65 * m.DEGREES, theta=-55 * m.DEGREES, zoom=0.75)

        self.play(m.Create(axes), run_time=1)
        self.play(m.Create(surface), run_time=2)
        self.wait(0.3)

        # Точка (первое появление — маленькая, полупрозрачная)
        point_dot.set_opacity(0.4)
        self.play(m.Create(point_dot), run_time=0.5)
        self.wait(0.2)

        self.play(m.Create(curve_red), run_time=1.2)
        self.play(m.Create(curve_blue), run_time=1.2)
        self.wait(0.3)

        self.play(m.Create(tangent_red), run_time=0.8)
        self.play(m.Create(tangent_blue), run_time=0.8)
        self.wait(0.3)

        # Акцентная точка — перерисовываем поверх всего
        '''accent_dot = m.Dot3D(axes.c2p(x0, y0, z0), color=m.YELLOW, radius=0.14)
        accent_ring = m.Circle(
            radius=0.25,
            color=m.YELLOW,
            stroke_width=3,
        ).move_to(axes.c2p(x0, y0, z0))
        # Кольцо нужно повернуть в плоскость, но в 3D это сложно —
        # используем Dot3D побольше + меньший контрастный внутри
        accent_inner = m.Dot3D(axes.c2p(x0, y0, z0), color=m.YELLOW, radius=0.16)

        self.play(
            m.FadeIn(accent_dot),
            m.FadeIn(accent_inner),
            run_time=0.6,
        )
        self.wait(0.3)'''

        # Подписи к кривым и точке
        self.play(
            m.Write(red_label),
            m.Write(blue_label),
            m.Write(point_label),
            run_time=0.8,
        )
        self.wait(0.3)

        # Формула и заголовок
        self.add_fixed_in_frame_mobjects( title)
        self.play(m.Write(title), run_time=0.3)
        self.wait(0.3)

        # Вращение камеры
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(6)
        self.stop_ambient_camera_rotation()

        self.wait(1)

class GradientVsNewton(Scene_):
    """
    Глава 4, Анимация 10: Градиентный спуск vs метод Ньютона.
    На карте уровней эллиптической функции потерь показаны два пути
    из одной стартовой точки к минимуму:
    - длинный зигзагообразный путь градиентного спуска (красный),
    - короткий почти прямой путь метода Ньютона (синий).
    """
    def construct(self):
        # 1. Функция потерь: эллиптическая квадратичная форма
        # f(x, y) = 0.5 * (a*x^2 + b*y^2), где a >> b — вытянутая чаша
        a = 4.0
        b = 0.25

        def f(x, y):
            return 0.5 * (a * x ** 2 + b * y ** 2)

        # Градиент
        def grad_f(x, y):
            return np.array([a * x, b * y])

        # Гессиан (постоянный)
        H = np.array([[a, 0], [0, b]])
        H_inv = np.linalg.inv(H)

        # 2. Координатная плоскость
        axes = m.Axes(
            x_range=[-2.5, 2.5, 0.5],
            y_range=[-2.5, 2.5, 0.5],
            x_length=8,
            y_length=8,
            axis_config={"color": m.GRAY, "stroke_width": 1.5, "include_tip": False},
            x_axis_config={"numbers_to_include": [-2, -1, 0, 1, 2], "font_size": 18},
            y_axis_config={"numbers_to_include": [-2, -1, 0, 1, 2], "font_size": 18},
        )
        axes.shift(m.DOWN * 0.3)

        self.play(m.Create(axes), run_time=0.8)
        self.wait(0.2)

        # 3. Карта уровней (контурные эллипсы)
        levels = [0.1, 0.3, 0.6, 1.0, 1.6, 2.4, 3.5, 5.0]

        contour_lines = m.VGroup()
        for level in levels:
            # Эллипс: a*x^2 + b*y^2 = 2*level
            # x^2 / (2*level/a) + y^2 / (2*level/b) = 1
            rx = np.sqrt(2 * level / a)
            ry = np.sqrt(2 * level / b)
            ellipse = m.Ellipse(
                width=2 * rx * axes.x_axis.unit_size,
                height=2 * ry * axes.y_axis.unit_size,
                color=m.BLUE_E,
                stroke_width=1.5,
                stroke_opacity=0.6,
            )
            ellipse.move_to(axes.coords_to_point(0, 0))
            contour_lines.add(ellipse)

        self.play(m.Create(contour_lines), run_time=1.5)
        self.wait(0.3)

        # 4. Минимум (в начале координат)
        minimum_dot = m.Dot(axes.coords_to_point(0, 0), color=m.YELLOW, radius=0.1)
        minimum_label = m.Text("минимум", font_size=20, color=m.YELLOW)
        minimum_label.next_to(minimum_dot, m.UR, buff=0.15)

        self.play(m.Create(minimum_dot), m.Write(minimum_label), run_time=0.5)
        self.wait(0.3)

        # 5. Стартовая точка
        start = np.array([-2.0, 1.8])
        start_point = axes.coords_to_point(start[0], start[1])
        start_dot = m.Dot(start_point, color=m.WHITE, radius=0.1)
        start_label = m.Text("старт", font_size=20, color=m.WHITE)
        start_label.next_to(start_dot, m.UL, buff=0.15)

        self.play(m.Create(start_dot), m.Write(start_label), run_time=0.5)
        self.wait(0.3)

        # ========== 6. Градиентный спуск ==========
        lr_gd = 0.4  # шаг градиентного спуск
        n_steps_gd = 25

        gd_path = [start.copy()]
        p = start.copy()
        for _ in range(n_steps_gd):
            g = grad_f(p[0], p[1])
            p = p - lr_gd * g
            gd_path.append(p.copy())

        # Преобразуем в точки на сцене
        gd_screen_points = [axes.coords_to_point(pt[0], pt[1]) for pt in gd_path]

        # Линия градиентного спуска
        gd_line = m.VMobject()
        gd_line.set_points_as_corners(gd_screen_points)
        gd_line.set_color(m.RED)
        gd_line.set_stroke(width=2.5)

        # Точки на каждом шаге
        gd_dots = m.VGroup(*[
            m.Dot(pt, color=m.RED, radius=0.05) for pt in gd_screen_points[1:]
        ])

        # Метка
        gd_label = m.Text(
            f"Градиентный спуск ({n_steps_gd} шагов)",
            font_size=22, color=m.RED,
        )
        gd_label.to_corner(m.UL, buff=0.4)

        # ========== 7. Метод Ньютона ==========
        # Ньютон: p_{k+1} = p_k - H^{-1} * grad_f(p_k)
        newton_path = [start.copy()]
        p = start.copy()
        for _ in range(6):
            g = grad_f(p[0], p[1])
            p = p - H_inv @ g
            newton_path.append(p.copy())

        newton_screen_points = [axes.coords_to_point(pt[0], pt[1]) for pt in newton_path]

        newton_line = m.VMobject()
        newton_line.set_points_as_corners(newton_screen_points)
        newton_line.set_color(m.BLUE)
        newton_line.set_stroke(width=2.5)

        newton_dots = m.VGroup(*[
            m.Dot(pt, color=m.BLUE, radius=0.05) for pt in newton_screen_points[1:]
        ])

        newton_label = m.Text(
            f"Метод Ньютона ({len(newton_path) - 1} шагов)",
            font_size=22, color=m.BLUE,
        )
        newton_label.to_corner(m.UR, buff=0.4)

        # ========== 8. Заголовок ==========
        title = m.Text(
            "Градиентный спуск vs метод Ньютона",
            font_size=28, color=m.BLACK,
        )
        title.to_edge(m.UP, buff=0.3)

        note = m.Text(
            "Эллиптическая функция потерь: f(x, y) = 2x² + 0.125y²",
            font_size=20, color=m.BLACK,
        )
        note.to_edge(m.DOWN, buff=0.3)

        # ========== АНИМАЦИЯ ==========
        self.play(m.Write(title), m.Write(note), run_time=0.8)
        self.wait(0.3)

        # Градиентный спуск
        self.play(
            m.Create(gd_line),
            *[m.Create(d) for d in gd_dots],
            run_time=3,
            rate_func=m.linear,
        )
        self.play(m.Write(gd_label), run_time=0.5)
        self.wait(0.5)

        # Метод Ньютона
        self.play(
            m.Create(newton_line),
            *[m.Create(d) for d in newton_dots],
            run_time=2,
            rate_func=m.linear,
        )
        self.play(m.Write(newton_label), run_time=0.5)
        self.wait(0.5)

        # Финальный вывод
        conclusion = m.Text(
            "Ньютон использует кривизну и приходит за 1 шаг",
            font_size=22, color=m.YELLOW,
        )
        conclusion.to_edge(m.DOWN, buff=0.8)
        self.play(m.Write(conclusion), run_time=0.8)

        self.wait(2)

class GradientVsNewton3D(ThreeDScene_):
    """
    Глава 4, Анимация 10: Градиентный спуск vs метод Ньютона.
    В 3D-пространстве нарисованы концентрические эллипсы (карта уровней).
    Два шарика скатываются к минимуму:
    - красный зигзагом (градиентный спуск),
    - синий почти прямо (метод Ньютона).
    За шариками остаётся исчезающий след.
    """
    def construct(self):
        # 1. Функция потерь
        a = 4.0
        b = 0.25

        def f(x, y):
            return 0.5 * (a * x ** 2 + b * y ** 2)

        def grad_f(x, y):
            return np.array([a * x, b * y])

        H = np.array([[a, 0], [0, b]])
        H_inv = np.linalg.inv(H)

        # 2. Трёхмерные оси
        axes = m.ThreeDAxes(
            x_range=[-2.5, 2.5, 0.5],
            y_range=[-2.5, 2.5, 0.5],
            z_range=[0, 6, 1],
            x_length=7,
            y_length=7,
            z_length=4,
            axis_config={"color": m.GRAY, "stroke_width": 1.5, "include_tip": False},
        )
        # Опускаем всю сцену ниже
        axes.shift(m.DOWN * 1.5)

        # 3. Карта уровней в 3D — эллипсы на разной высоте z
        levels = [0.3, 0.8, 1.5, 2.5, 4.0, 5.5]
        contour_lines = m.VGroup()
        for level in levels:
            rx = np.sqrt(2 * level / a)
            ry = np.sqrt(2 * level / b)
            ellipse = m.ParametricFunction(
                lambda t, rx=rx, ry=ry, level=level: axes.c2p(
                    rx * np.cos(t), ry * np.sin(t), level
                ),
                t_range=[0, 2 * np.pi, 0.05],
                color=m.BLUE_D,
                stroke_width=2,
                stroke_opacity=0.7,
            )
            contour_lines.add(ellipse)

        # 4. Минимум и старт
        minimum_dot = m.Dot3D(axes.c2p(0, 0, 0), color=m.YELLOW, radius=0.09)
        minimum_label = m.Text("минимум", font_size=18, color=m.YELLOW)
        minimum_label.move_to(axes.c2p(0.4, 0.4, 0.4))

        start = np.array([-2.0, 1.8])
        z_start = f(start[0], start[1])
        start_dot = m.Dot3D(axes.c2p(start[0], start[1], z_start),
                             color=m.WHITE, radius=0.09)
        start_label = m.Text("старт", font_size=18, color=m.WHITE)
        start_label.move_to(axes.c2p(start[0], start[1] + 0.3, z_start + 0.4))

        # ========== 5. Градиентный спуск ==========
        lr_gd = 0.4
        n_steps_gd = 25

        gd_path = [start.copy()]
        p = start.copy()
        for _ in range(n_steps_gd):
            g = grad_f(p[0], p[1])
            p = p - lr_gd * g
            gd_path.append(p.copy())

        gd_3d_points = [
            axes.c2p(pt[0], pt[1], f(pt[0], pt[1])) for pt in gd_path
        ]
        gd_line = m.VMobject()
        gd_line.set_points_as_corners(gd_3d_points)
        gd_line.set_color(m.RED)
        gd_line.set_stroke(width=3)

        # ========== 6. Метод Ньютона ==========
        newton_path = [start.copy()]
        p = start.copy()
        for _ in range(6):
            g = grad_f(p[0], p[1])
            p = p - H_inv @ g
            newton_path.append(p.copy())

        newton_3d_points = [
            axes.c2p(pt[0], pt[1], f(pt[0], pt[1])) for pt in newton_path
        ]
        newton_line = m.VMobject()
        newton_line.set_points_as_corners(newton_3d_points)
        newton_line.set_color(m.BLUE)
        newton_line.set_stroke(width=3)

        # ========== 7. Шарики и исчезающий след ==========
        # Шарики
        gd_ball = m.Sphere(radius=0.1, color=m.RED).move_to(
            axes.c2p(start[0], start[1], z_start)
        )
        newton_ball = m.Sphere(radius=0.1, color=m.BLUE).move_to(
            axes.c2p(start[0], start[1], z_start)
        )

        # Исчезающий след: маленькие точки, оставляемые за шариком
        # Для градиентного спуска
        gd_trail_dots = []
        for pt in gd_path[::2]:  # берём каждую вторую точку
            dot = m.Dot3D(
                axes.c2p(pt[0], pt[1], f(pt[0], pt[1])),
                color=m.RED,
                radius=0.05,
            )
            dot.set_opacity(0)
            gd_trail_dots.append(dot)

        # Для метода Ньютона
        newton_trail_dots = []
        for pt in newton_path:
            dot = m.Dot3D(
                axes.c2p(pt[0], pt[1], f(pt[0], pt[1])),
                color=m.BLUE,
                radius=0.05,
            )
            dot.set_opacity(0)
            newton_trail_dots.append(dot)

        # ========== 8. Текстовые подписи ==========
        title = m.Text(
            "Градиентный спуск vs метод Ньютона",
            font_size=26, color=m.BLACK,
        )
        title.to_edge(m.UP, buff=0.3)

        note = m.Text(
            "f(x, y) = 2x² + 0.125y²",
            font_size=20, color=m.BLACK,
        )
        note.to_corner(m.DR, buff=0.4)

        gd_label = m.Text("градиентный спуск", font_size=20, color=m.RED)
        gd_label.to_corner(m.UL, buff=0.4)

        newton_label = m.Text("метод Ньютона", font_size=20, color=m.BLUE)
        newton_label.next_to(gd_label, m.DOWN, buff=0.1)
        newton_label.align_to(gd_label, m.LEFT)

        # ========== АНИМАЦИЯ ==========
        self.set_camera_orientation(phi=65 * m.DEGREES, theta=-55 * m.DEGREES, zoom=0.7)
        self.add_fixed_in_frame_mobjects(title, note, gd_label, newton_label)

        # 1. Оси и эллипсы
        self.play(m.Create(axes), run_time=1)
        self.wait(0.2)
        self.play(m.Create(contour_lines), run_time=2)
        self.wait(0.2)

        # 2. Минимум и старт
        self.play(
            m.Create(minimum_dot), m.Write(minimum_label),
            m.Create(start_dot), m.Write(start_label),
            run_time=0.8,
        )
        self.wait(0.3)

        # 3. Подписи
        self.play(m.Write(title), m.Write(note), run_time=0.5)
        self.play(m.Write(gd_label), m.Write(newton_label), run_time=0.5)
        self.wait(0.3)

        # 4. Все точки следа на сцене (пока невидимые)
        self.add(*gd_trail_dots, *newton_trail_dots)

        # 5. Красный путь — градиентный спуск
        self.add(gd_ball)
        self.wait(0.3)

        # Анимируем движение шарика по точкам, оставляя след
        gd_animations = []
        prev_dot = None
        for i, pt in enumerate(gd_path):
            if i % 2 == 0 and i // 2 < len(gd_trail_dots):
                dot = gd_trail_dots[i // 2]
                gd_animations.append(dot.animate.set_opacity(1))
            gd_animations.append(
                gd_ball.animate.move_to(
                    axes.c2p(pt[0], pt[1], f(pt[0], pt[1]))
                )
            )

        # Проигрываем всё разом
        self.play(*gd_animations, run_time=4, rate_func=m.linear)
        self.wait(0.3)

        # 6. Синий путь — метод Ньютона
        self.add(newton_ball)
        self.wait(0.3)

        newton_animations = []
        for i, pt in enumerate(newton_path):
            dot = newton_trail_dots[i]
            newton_animations.append(dot.animate.set_opacity(1))
            newton_animations.append(
                newton_ball.animate.move_to(
                    axes.c2p(pt[0], pt[1], f(pt[0], pt[1]))
                )
            )

        self.play(*newton_animations, run_time=2, rate_func=m.linear)
        self.wait(0.5)

        # 7. Финальный вывод
        conclusion = m.Text(
            "Ньютон учитывает кривизну — почти прямая к минимуму",
            font_size=20, color=m.YELLOW,
        )
        conclusion.to_edge(m.DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(conclusion)
        self.play(m.Write(conclusion), run_time=0.8)

        # 8. Медленное вращение камеры
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)
        self.stop_ambient_camera_rotation()

        self.wait(1)
class GradientDescentVsNewton(ThreeDScene_):
    """
    Глава 6, Анимация: Градиентный спуск vs метод Ньютона на карте уровней.
    Показывает зигзагообразный путь градиентного спуска и прямой путь метода Ньютона.
    """
    def construct(self):
        # 1. Координатная плоскость (2D)
        axes = m.Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": m.GRAY, "stroke_width": 1.5, "include_tip": False},
            x_axis_config={"numbers_to_include": [-3, -2, -1, 0, 1, 2, 3], "font_size": 18},
            y_axis_config={"numbers_to_include": [-2, -1, 1, 2], "font_size": 18},
        )
        axes.shift(m.DOWN * 0.3)

        self.play(m.Create(axes), run_time=1)
        self.wait(0.3)

        # 2. Функция потерь L(x,y) = x² + 4y² (эллиптическая)
        # Контурные линии: x² + 4y² = c (эллипсы)
        contour_levels = [1, 2, 4, 6, 8, 10]
        contours = m.VGroup()
        
        for level in contour_levels:
            # Параметризация эллипса: x = sqrt(level)*cos(t), y = sqrt(level/4)*sin(t)
            ellipse = m.ParametricFunction(
                lambda t, lv=level: np.array([
                    np.sqrt(lv) * np.cos(t),
                    np.sqrt(lv / 4) * np.sin(t),
                    0
                ]),
                t_range=[0, 2 * np.pi],
                color=m.BLUE_E,
                stroke_width=1.5,
                stroke_opacity=0.5,
            )
            contours.add(ellipse)

        self.play(m.Create(contours), run_time=2)
        self.wait(0.5)

        # 3. Минимум функции (0, 0)
        minimum = m.Dot(
            axes.c2p(0, 0),
            color=m.GREEN,
            radius=0.12,
        )
        min_label = m.MathTex(
            r"\text{min}",
            font_size=20,
            color=m.GREEN,
        )
        min_label.next_to(minimum, m.RIGHT, buff=0.2)

        self.play(m.Create(minimum), m.Write(min_label), run_time=0.6)
        self.wait(0.5)

        # 4. Стартовая точка (-3, 2)
        start_x, start_y = -3, 2
        start_point = m.Dot(
            axes.c2p(start_x, start_y),
            color=m.WHITE,
            radius=0.12,
        )
        start_label = m.MathTex(
            r"(x_0, y_0)",
            font_size=20,
            color=m.WHITE,
        )
        start_label.next_to(start_point, m.UP + m.LEFT, buff=0.15)

        self.play(m.Create(start_point), m.Write(start_label), run_time=0.6)
        self.wait(0.5)

        # 5. Траектория градиентного спуска (зигзаг)
        # L(x,y) = x² + 4y², градиент = (2x, 8y)
        # Шаг: (x_new, y_new) = (x - lr*2x, y - lr*8y)
        lr = 0.12  # скорость обучения
        gd_points = [(start_x, start_y)]
        x, y = start_x, start_y
        
        for _ in range(15):  # 15 шагов
            x_new = x - lr * 2 * x
            y_new = y - lr * 8 * y
            gd_points.append((x_new, y_new))
            x, y = x_new, y_new

        # Создать ломаную линию
        gd_path = m.VMobject()
        gd_path.set_points_smoothly([
            axes.c2p(p[0], p[1]) for p in gd_points
        ])
        gd_path.set_color(m.RED)
        gd_path.set_stroke(width=2.5)

        gd_label = m.Text(
            "градиентный спуск",
            font_size=22,
            color=m.RED,
        )
        gd_label.to_corner(m.UL, buff=1)

        self.play(m.Create(gd_path), m.Write(gd_label), run_time=3)
        self.wait(1)

        # 6. Траектория метода Ньютона (прямая)
        # Для квадратичной функции сходится за 1 шаг
        # H = [[2, 0], [0, 8]], H^{-1} = [[0.5, 0], [0, 0.125]]
        # Шаг: (x_new, y_new) = (x, y) - H^{-1} * grad = (0, 0)
        newton_points = [(start_x, start_y), (0, 0)]
        
        newton_path = m.VMobject()
        newton_path.set_points_smoothly([
            axes.c2p(p[0], p[1]) for p in newton_points
        ])
        newton_path.set_color(m.GREEN)
        newton_path.set_stroke(width=3)

        newton_label = m.Text(
            "метод Ньютона",
            font_size=22,
            color=m.GREEN,
        )
        newton_label.next_to(gd_label, m.DOWN, buff=0.3)

        self.play(m.Create(newton_path), m.Write(newton_label), run_time=2)
        self.wait(1)

        # 7. Подпись с формулой
        formula = m.MathTex(
            r"L(x,y) = x^2 + 4y^2",
            font_size=24,
            color=m.BLACK,
        )
        formula.to_corner(m.UR, buff=0.5)

        self.play(m.Write(formula), run_time=0.8)
        self.wait(0.5)

        # 8. Финальная подпись
        final_note = m.Text(
            "Метод Ньютона учитывает кривизну и идёт напрямую к минимуму",
            font_size=20,
            color=m.BLACK,
        )
        final_note.to_edge(m.DOWN, buff=1)

        self.play(m.Write(final_note), run_time=1)
        self.wait(2)
# ========== НАСТРОЙКА ДЛЯ РЕНДЕРИНГА ==========

# Устанавливаем директорию для вывода
OUTPUT_DIR = Path(__file__).parent / "derivative"
OUTPUT_DIR.mkdir(exist_ok=True)
os.environ["MANIM_MEDIA_DIR"] = str(OUTPUT_DIR)

if __name__ == '__main__':
    import subprocess

    SCENES = [
        # Здесь будут другие сцены из главы 5
       #"DerivativeGeometricMeaning",
       #"DerivativeAsFunction",
       #"ZoomToTangent",
       #"GradientDescent",
       #"ActivationFunctions",
       #"TaylorApproximation",
       #"NewtonMethod",
       #"PartialDerivatives2",
       #"GradientVsNewton",
       #"GradientVsNewton3D",
       "GradientDescentVsNewton"
    ]
    
    file_path = Path(__file__).resolve()
    
    for SCENE in SCENES:
        print(f"\nРендеринг сцены: {SCENE}")
        
        # Генерация видео
        subprocess.run([
            "manim", 
            str(file_path), 
            SCENE, 
            "-qh"
        ])
        
        # Генерация последнего кадра
        subprocess.run([
            "manim", 
            str(file_path), 
            SCENE, 
            "-s"
        ])
    
    print(f"\n✅ Все видео и изображения сохранены в: {OUTPUT_DIR}")