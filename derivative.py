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
       "NewtonMethod"
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