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

class FunctionIntroduction(Scene_):
    """
    Глава 4, Анимация 1: Интуитивное определение функции.
    Демонстрирует функцию как отображение между двумя множествами.
    """
    def construct(self):
        # 1. Создаем два множества: область определения (X) и область значений (Y)
        # Множество X (слева)
        set_x = m.Rectangle(
            width=3, height=4, 
            color=m.BLUE, 
            fill_opacity=0.1,
            stroke_width=3
        )
        set_x_label = m.MathTex("X", color=m.BLUE, font_size=36)
        set_x_label.next_to(set_x, m.UP, buff=0.3)
        set_x_group = m.VGroup(set_x, set_x_label)
        set_x_group.shift(m.LEFT * 3.5)

        # Элементы множества X
        x_elements = [
            m.Dot(point=set_x.get_center() + np.array([-1, 1.2, 0]), color=m.BLUE, radius=0.08),
            m.Dot(point=set_x.get_center() + np.array([0.5, 0.8, 0]), color=m.BLUE, radius=0.08),
            m.Dot(point=set_x.get_center() + np.array([-0.8, -0.2, 0]), color=m.BLUE, radius=0.08),
            m.Dot(point=set_x.get_center() + np.array([0.8, -0.8, 0]), color=m.BLUE, radius=0.08),
            m.Dot(point=set_x.get_center() + np.array([-0.5, -1.5, 0]), color=m.BLUE, radius=0.08),
        ]
        
        x_labels = [
            m.MathTex("x_1", font_size=20, color=m.BLUE).next_to(x_elements[0], m.LEFT, buff=0.2),
            m.MathTex("x_2", font_size=20, color=m.BLUE).next_to(x_elements[1], m.RIGHT, buff=0.2),
            m.MathTex("x_3", font_size=20, color=m.BLUE).next_to(x_elements[2], m.LEFT, buff=0.2),
            m.MathTex("x_4", font_size=20, color=m.BLUE).next_to(x_elements[3], m.RIGHT, buff=0.2),
            m.MathTex("x_5", font_size=20, color=m.BLUE).next_to(x_elements[4], m.LEFT, buff=0.2),
        ]

        # Множество Y (справа)
        set_y = m.Rectangle(
            width=3, height=4, 
            color=m.RED, 
            fill_opacity=0.1,
            stroke_width=3
        )
        set_y_label = m.MathTex("Y", color=m.RED, font_size=36)
        set_y_label.next_to(set_y, m.UP, buff=0.3)
        set_y_group = m.VGroup(set_y, set_y_label)
        set_y_group.shift(m.RIGHT * 3.5)

        # Элементы множества Y (теперь 5 элементов для взаимно-однозначного соответствия)
        y_elements = [
            m.Dot(point=set_y.get_center() + np.array([-1, 1.2, 0]), color=m.RED, radius=0.08),
            m.Dot(point=set_y.get_center() + np.array([0.8, 0.7, 0]), color=m.RED, radius=0.08),
            m.Dot(point=set_y.get_center() + np.array([-0.5, 0.0, 0]), color=m.RED, radius=0.08),
            m.Dot(point=set_y.get_center() + np.array([0.5, -0.8, 0]), color=m.RED, radius=0.08),
            m.Dot(point=set_y.get_center() + np.array([-0.8, -1.5, 0]), color=m.RED, radius=0.08),
        ]
        
        y_labels = [
            m.MathTex("y_1", font_size=20, color=m.RED).next_to(y_elements[0], m.RIGHT, buff=0.2),
            m.MathTex("y_2", font_size=20, color=m.RED).next_to(y_elements[1], m.LEFT, buff=0.2),
            m.MathTex("y_3", font_size=20, color=m.RED).next_to(y_elements[2], m.RIGHT, buff=0.2),
            m.MathTex("y_4", font_size=20, color=m.RED).next_to(y_elements[3], m.LEFT, buff=0.2),
            m.MathTex("y_5", font_size=20, color=m.RED).next_to(y_elements[4], m.RIGHT, buff=0.2),
        ]

        # 2. Создаем все элементы на сцене
        self.play(
            m.Create(set_x_group),
            m.Create(set_y_group),
            run_time=1
        )
        
        self.play(
            *[m.Create(x_elements[i]) for i in range(5)],
            *[m.Write(x_labels[i]) for i in range(5)],
            *[m.Create(y_elements[i]) for i in range(5)],
            *[m.Write(y_labels[i]) for i in range(5)],
            run_time=1.5
        )
        
        self.wait(0.5)

        # 3. Подписи "Область определения" и "Область значений"
        domain_label = create_label("Область определения", "domain_label")
        domain_label.next_to(set_x, m.DOWN, buff=0.3)
        
        codomain_label = create_label("Область значений", "codomain_label")
        codomain_label.next_to(set_y, m.DOWN, buff=0.3)
        
        self.play(
            m.Write(domain_label),
            m.Write(codomain_label),
            run_time=0.8
        )
        
        self.wait(0.5)

        # 4. Рисуем четкие стрелки x_i -> y_i (взаимно-однозначное соответствие)
        mappings = [
            (0, 0),  # x1 -> y1
            (1, 1),  # x2 -> y2
            (2, 2),  # x3 -> y3
            (3, 3),  # x4 -> y4
            (4, 4),  # x5 -> y5
        ]
        
        arrows = []
        for xi, yi in mappings:
            start = x_elements[xi].get_center()
            end = y_elements[yi].get_center()
            
            arrow = m.Arrow(
                start=start,
                end=end,
                color=m.YELLOW,
                stroke_width=2,
                buff=0.1,
                max_tip_length_to_length_ratio=0.15
            )
            arrows.append(arrow)
        
        # Показываем стрелки с небольшой задержкой для наглядности
        for i, arrow in enumerate(arrows):
            self.play(m.Create(arrow), run_time=0.25)
            # Подсвечиваем соответствующую пару
            self.play(
                x_elements[i].animate.set_color(m.YELLOW),
                y_elements[i].animate.set_color(m.YELLOW),
                run_time=0.1
            )
        
        self.wait(0.5)

        # 5. Основная подпись
        function_label = create_label(
            "Функция: каждому x соответствует ровно один y",
            "function_label"
        )
        function_label.to_edge(m.DOWN, buff=0.8)
        
        self.play(m.Write(function_label), run_time=1)
        
        self.wait(0.5)

        # 6. Снимаем подсветку с элементов
        for i in range(5):
            self.play(
                x_elements[i].animate.set_color(m.BLUE),
                y_elements[i].animate.set_color(m.RED),
                run_time=0.1
            )
        
        self.wait(2)

class FunctionGraphs(Scene_):
    """
    Глава 4, Анимация 2: Графики основных функций.
    Демонстрирует экспоненту, логарифм и квадратичную параболу.
    """
    def construct(self):
        # 1. Создаем координатную плоскость
        axes = m.Axes(
            x_range=[-4, 5, 1],
            y_range=[-2, 5, 1],
            axis_config={"color": m.GRAY},
            x_axis_config={"numbers_to_include": range(-4, 6, 1)},
            y_axis_config={"numbers_to_include": range(-2, 6, 1)},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Сдвигаем оси вниз
        axes.shift(m.DOWN * 0.8)
        axes_labels.shift(m.DOWN * 0.8)
        
        self.play(m.Create(axes), m.Write(axes_labels), run_time=1)
        self.wait(0.3)

        # 2. Создаем графики функций (без обрезания по y)
        # Экспонента f(x) = e^x (синяя) - ограничиваем только x_range
        exp_graph = axes.plot(
            lambda x: np.exp(x),
            x_range=[-3, 1.8, 0.01],  # до x=1.8, чтобы e^1.8 ≈ 6 не выходила за границы
            color=m.BLUE,
            stroke_width=3
        )
        exp_label = m.MathTex("e^x", color=m.BLUE, font_size=24)
        exp_label.next_to(exp_graph.get_end(), m.LEFT, buff=0.1)
        exp_label.shift(m.DOWN * 0.2)

        # Логарифм f(x) = ln(x) (красная)
        log_graph = axes.plot(
            lambda x: np.log(x) if x > 0 else None,
            x_range=[0.1, 4.5, 0.01],
            color=m.RED,
            stroke_width=3
        )
        log_label = m.MathTex("\\ln x", color=m.RED, font_size=24)
        log_label.next_to(log_graph.get_end(), m.UP, buff=0.1)
        log_label.shift(m.LEFT * 0.2)

        # Парабола f(x) = x^2 (зеленая)
        parabola_graph = axes.plot(
            lambda x: x**2,
            x_range=[-2.3, 2.3, 0.01],  # до x=±2.3, чтобы 2.3^2 ≈ 5.3 не выходила за границы
            color=m.GREEN,
            stroke_width=3
        )
        parabola_label = m.MathTex("x^2", color=m.GREEN, font_size=24)
        parabola_label.next_to(parabola_graph.get_end(), m.DOWN, buff=0.1)
        parabola_label.shift(m.LEFT * 0.2)

        # 3. Рисуем все графики одновременно
        self.play(
            m.Create(exp_graph),
            m.Create(log_graph),
            m.Create(parabola_graph),
            run_time=1.5
        )
        
        # 4. Добавляем подписи к графикам
        self.play(
            m.Write(exp_label),
            m.Write(log_label),
            m.Write(parabola_label),
            run_time=0.8
        )        

        self.wait(2)
class ActivationFunctions(Scene_):
    """
    Глава 4, Анимация 3: Функции активации: сигмоида и ReLU.
    Демонстрирует S-образную кривую сигмоиды и "коленку" ReLU.
    """
    def construct(self):
        # 1. Создаем координатную плоскость
        axes = m.Axes(
            x_range=[-6, 6, 1],
            y_range=[-0.5, 1.5, 0.5],
            axis_config={"color": m.GRAY},
            x_axis_config={"numbers_to_include": range(-6, 7, 1)},
            y_axis_config={"numbers_to_include": [-0.5, 0, 0.5, 1, 1.5]},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Сдвигаем оси вниз для места подписям
        axes.shift(m.DOWN * 0.5)
        axes_labels.shift(m.DOWN * 0.5)
        
        self.play(m.Create(axes), m.Write(axes_labels), run_time=1)
        self.wait(0.3)

        # 2. Сигмоида f(x) = 1 / (1 + e^(-x)) (синяя)
        sigmoid_graph = axes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            x_range=[-6, 6, 0.01],
            color=m.BLUE,
            stroke_width=3
        )
        sigmoid_label = m.MathTex("\\sigma(x) = \\frac{1}{1 + e^{-x}}", color=m.BLUE, font_size=24)
        sigmoid_label.next_to(axes.coords_to_point(3, 0.8), m.RIGHT, buff=0.1)
        
        # Горизонтальные асимптоты для сигмоиды (пунктирные линии)
        asymptote_0 = m.DashedLine(
            start=axes.coords_to_point(-6, 0),
            end=axes.coords_to_point(6, 0),
            color=m.BLUE,
            stroke_width=1,
            dash_length=0.1
        )
        asymptote_1 = m.DashedLine(
            start=axes.coords_to_point(-6, 1),
            end=axes.coords_to_point(6, 1),
            color=m.BLUE,
            stroke_width=1,
            dash_length=0.1
        )
        asymptote_0_label = m.MathTex("0", color=m.BLUE, font_size=20)
        asymptote_0_label.next_to(asymptote_0.get_left(), m.LEFT, buff=0.1)
        asymptote_1_label = m.MathTex("1", color=m.BLUE, font_size=20)
        asymptote_1_label.next_to(asymptote_1.get_left(), m.LEFT, buff=0.1)

        # 3. ReLU f(x) = max(0, x) (красная)
        relu_graph = axes.plot(
            lambda x: max(0, x),
            x_range=[-6, 1.5, 0.01],
            color=m.RED,
            stroke_width=3
        )
        relu_label = m.MathTex("\\text{ReLU}(x) = \\max(0, x)", color=m.RED, font_size=24)
        relu_label.next_to(axes.coords_to_point(3, 1.2), m.UP, buff=0.1)

        # 4. Рисуем сигмоиду с асимптотами
        self.play(
            m.Create(sigmoid_graph),
            m.Create(asymptote_0),
            m.Create(asymptote_1),
            m.Write(asymptote_0_label),
            m.Write(asymptote_1_label),
            run_time=1.5
        )
        self.play(m.Write(sigmoid_label), run_time=0.6)
        self.wait(0.5)

        # 5. Рисуем ReLU
        self.play(m.Create(relu_graph), run_time=1.5)
        self.play(m.Write(relu_label), run_time=0.6)

        # 6. Добавляем пояснительные подписи
        '''sigmoid_note = m.Text(
            "S-образная кривая, значения от 0 до 1",
            font_size=20,
            color=m.BLUE
        )
        sigmoid_note.next_to(sigmoid_label, m.DOWN, buff=0.2)
        sigmoid_note.align_to(sigmoid_label, m.LEFT)

        relu_note = m.Text(
            "Ноль для x < 0, линейный рост для x > 0",
            font_size=20,
            color=m.RED
        )
        relu_note.next_to(relu_label, m.DOWN, buff=0.2)
        relu_note.align_to(relu_label, m.LEFT)

        self.play(
            m.Write(sigmoid_note),
            m.Write(relu_note),
            run_time=0.8
        )'''


        self.wait(2)

class SqueezeTheorem(Scene_):
    """
    Глава 4, Анимация 4: Теорема о двух милиционерах (принцип сжатой последовательности).
    Демонстрирует три последовательности: нижнюю (синюю), верхнюю (красную) 
    и зажатую между ними (зелёную), которые стягиваются к одному пределу L.
    """
    def construct(self):
        # 1. Создаем координатную плоскость
        axes = m.Axes(
            x_range=[0, 11, 1],
            y_range=[-0.5, 2.5, 0.5],
            axis_config={"color": m.GRAY},
            x_axis_config={"numbers_to_include": range(0, 12, 1)},
            y_axis_config={"numbers_to_include": [0, 0.5, 1, 1.5, 2, 2.5]},
        )
        axes_labels = axes.get_axis_labels(x_label="n", y_label="y")
        
        axes.shift(m.DOWN * 0.3)
        axes_labels.shift(m.DOWN * 0.3)
        
        self.play(m.Create(axes), m.Write(axes_labels), run_time=1)
        self.wait(0.3)

        # 2. Предел L = 1 (горизонтальная пунктирная линия)
        L = 1
        limit_line = m.DashedLine(
            start=axes.coords_to_point(0.5, L),
            end=axes.coords_to_point(10.5, L),
            color=m.YELLOW,
            stroke_width=2,
            dash_length=0.1
        )
        limit_label = m.MathTex("L = 1", color=m.YELLOW, font_size=28)
        limit_label.next_to(axes.coords_to_point(10.5, L), m.RIGHT, buff=0.2)
        
        self.play(m.Create(limit_line), m.Write(limit_label), run_time=0.8)
        self.wait(0.3)

        # 3. Создаем три последовательности (только дискретные точки)
        n_values = list(range(1, 11))  # n = 1, 2, ..., 10
        
        # Нижняя последовательность: a_n = 1 - 1/n (синяя)
        a_dots = []
        for n in n_values:
            point = axes.coords_to_point(n, 1 - 1/n)
            dot = m.Dot(point, color=m.BLUE, radius=0.08)
            a_dots.append(dot)
        
        # Верхняя последовательность: b_n = 1 + 1/n (красная)
        b_dots = []
        for n in n_values:
            point = axes.coords_to_point(n, 1 + 1/n)
            dot = m.Dot(point, color=m.RED, radius=0.08)
            b_dots.append(dot)

        # Зажатая последовательность: x_n = 1 + sin(n)/n (зеленая)
        x_dots = []
        for n in n_values:
            point = axes.coords_to_point(n, 1 + np.sin(n)/n)
            dot = m.Dot(point, color=m.GREEN, radius=0.1)
            x_dots.append(dot)

        # 4. Показываем все три последовательности с ускоряющимся темпом
        # Нижняя последовательность (с ускорением)
        for i, dot in enumerate(a_dots):
            wait_time = 0.15 / (1 + i * 0.1)  # ускоряемся
            self.play(m.Create(dot), run_time=wait_time)
        
        # Подпись a_n правее
        a_label = m.MathTex("a_n", color=m.BLUE, font_size=24)
        a_label.next_to(a_dots[-1].get_center(), m.RIGHT, buff=0.3)
        a_label.shift(m.DOWN * 0.15)
        self.play(m.Write(a_label), run_time=0.3)
        self.wait(0.2)

        # Верхняя последовательность (с ускорением)
        for i, dot in enumerate(b_dots):
            wait_time = 0.15 / (1 + i * 0.1)
            self.play(m.Create(dot), run_time=wait_time)
        
        # Подпись b_n правее
        b_label = m.MathTex("b_n", color=m.RED, font_size=24)
        b_label.next_to(b_dots[-1].get_center(), m.RIGHT, buff=0.3)
        b_label.shift(m.UP * 0.15)
        self.play(m.Write(b_label), run_time=0.3)
        self.wait(0.2)

        # Зажатая последовательность (с ускорением)
        for i, dot in enumerate(x_dots):
            wait_time = 0.15 / (1 + i * 0.1)
            self.play(m.Create(dot), run_time=wait_time)
        
        # Подпись x_n правее
        x_label = m.MathTex("x_n", color=m.GREEN, font_size=24)
        x_label.next_to(x_dots[-1].get_center(), m.RIGHT, buff=0.3)
        x_label.shift(m.UP * 0.2)
        self.play(m.Write(x_label), run_time=0.3)
        self.wait(0.5)

        # 5. Неравенство (черным цветом, чуть ниже)
        inequality = m.MathTex(
            "a_n \\leq x_n \\leq b_n",
            font_size=32,
            color=m.BLACK
        )
        inequality.to_edge(m.UP, buff=1.8)
        
        self.play(m.Write(inequality), run_time=0.6)
        self.wait(2)

class ConvergenceRates(Scene_):
    """
    Глава 4, Анимация: Скорость сходимости.
    Демонстрирует разницу между линейной и квадратичной сходимостью.
    """
    def construct(self):
        # 1. Параметры последовательностей (как в примере)
        n_max = 8
        q = 0.5
        a0 = 0.5
        y_min_log = -10

        n_values = list(range(n_max + 1))
        linear = [q**n for n in n_values]
        quadratic = [a0]
        for _ in range(n_max):
            quadratic.append(quadratic[-1] ** 2)

        def safe_log10(x):
            return np.log10(x) if x > 10**y_min_log else y_min_log

        linear_log = [safe_log10(v) for v in linear]
        quad_log = [safe_log10(v) for v in quadratic]

        # 2. Оси — сдвигаем правее, чтобы метки Y поместились
        axes = m.Axes(
            x_range=[0, n_max, 1],
            y_range=[y_min_log, 0.5, 2],
            axis_config={"color": m.GRAY},
            x_axis_config={"numbers_to_include": n_values},
            y_axis_config={"numbers_to_include": [], "include_tip": False},
        )
        axes.shift(m.RIGHT * 0.5 + m.DOWN * 0.3)

        x_label = m.MathTex("n", font_size=28).next_to(
            axes.x_axis.get_end(), m.RIGHT, buff=0.2
        )
        y_label = m.MathTex("\\log_{10}|a_n - A|", font_size=28).next_to(
            axes.y_axis.get_top(), m.UP, buff=0.2
        )

        # Метки Y — уменьшенный размер шрифта
        y_ticks = m.VGroup()
        for k in range(0, y_min_log - 1, -2):
            y_val = float(k)
            tick_line = m.Line(
                start=axes.c2p(-0.15, y_val),
                end=axes.c2p(0.15, y_val),
                color=m.GRAY,
            )
            tick_label = m.MathTex(f"10^{{{k}}}", font_size=16)
            tick_label.next_to(tick_line, m.LEFT, buff=0.15)
            y_ticks.add(tick_line, tick_label)

        self.play(
            m.Create(axes), m.Write(x_label), m.Write(y_label),
            m.FadeIn(y_ticks),
            run_time=1.2,
        )
        self.wait(0.3)

        # 3. Линейная сходимость
        lin_dots = m.VGroup()
        lin_lines = m.VGroup()
        for i, n in enumerate(n_values):
            pt = axes.c2p(n, linear_log[i])
            dot = m.Dot(pt, color=m.BLUE, radius=0.08)
            lin_dots.add(dot)
            if i > 0:
                prev_pt = axes.c2p(n_values[i - 1], linear_log[i - 1])
                lin_lines.add(m.Line(prev_pt, pt, color=m.BLUE, stroke_width=2))

        self.play(m.Create(lin_dots), run_time=0.8)
        self.play(m.Create(lin_lines), run_time=0.6)

        # Формулы из примера — справа от графика, ниже
        lin_formula = m.MathTex(
            "a_{n+1} = a_n / 2", color=m.BLUE, font_size=24
        )
        lin_formula.to_edge(m.RIGHT, buff=1.2)
        lin_formula.shift(m.UP * 1.0)
        
        # ИСПРАВЛЕНО: используем m.Text для кириллицы
        lin_limit = m.Text(
            "предел = 0", color=m.BLUE, font_size=20
        )
        lin_limit.next_to(lin_formula, m.DOWN, buff=0.2)
        
        self.play(m.Write(lin_formula), m.Write(lin_limit), run_time=0.6)
        self.wait(0.3)

        # 4. Квадратичная сходимость
        quad_dots = m.VGroup()
        quad_lines = m.VGroup()
        for i, n in enumerate(n_values):
            pt = axes.c2p(n, quad_log[i])
            dot = m.Dot(pt, color=m.RED, radius=0.08)
            quad_dots.add(dot)
            if i > 0:
                prev_pt = axes.c2p(n_values[i - 1], quad_log[i - 1])
                quad_lines.add(m.Line(prev_pt, pt, color=m.RED, stroke_width=2))

        self.play(m.Create(quad_dots), run_time=0.8)
        self.play(m.Create(quad_lines), run_time=0.6)

        quad_formula = m.MathTex(
            "a_{n+1} = a_n^2", color=m.RED, font_size=24
        )
        quad_formula.to_edge(m.RIGHT, buff=1.2)
        quad_formula.shift(m.DOWN * 1.0)
        
        # ИСПРАВЛЕНО: используем m.Text для кириллицы
        quad_limit = m.Text(
            "предел = 0", color=m.RED, font_size=20
        )
        quad_limit.next_to(quad_formula, m.DOWN, buff=0.2)
        
        self.play(m.Write(quad_formula), m.Write(quad_limit), run_time=0.6)
        self.wait(2)

class ConvexityDefinition(Scene_):
    """
    Глава 4, Анимация 6: Определение выпуклости функции.
    Демонстрирует график выпуклой функции, хорду между двумя точками,
    промежуточную точку на хорде и точку на графике, а также зазор выпуклости.
    """
    def construct(self):
        # 1. Координатная плоскость (увеличиваем диапазон, чтобы всё поместилось)
        axes = m.Axes(
            x_range=[-0.5, 5, 1],
            y_range=[-0.5, 6, 1],
            axis_config={"color": m.GRAY},
            x_axis_config={"numbers_to_include": range(0, 6, 1)},
            y_axis_config={"numbers_to_include": range(0, 7, 1)},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        axes.shift(m.DOWN * 0.6)
        axes_labels.shift(m.DOWN * 0.6)
        
        self.play(m.Create(axes), m.Write(axes_labels), run_time=0.8)
        self.wait(0.3)

        # 2. График выпуклой функции f(x) = 0.3 * x^2
        f = lambda x: 0.3 * x ** 2
        graph = axes.plot(f, x_range=[0, 4.2, 0.01], color=m.BLUE, stroke_width=3)
        graph_label = m.MathTex("f(x)", color=m.BLUE, font_size=26)
        graph_label.next_to(axes.coords_to_point(4.2, f(4.2)), m.UR, buff=0.15)

        self.play(m.Create(graph), run_time=1.2)
        self.play(m.Write(graph_label), run_time=0.4)
        self.wait(0.3)

        # 3. Две точки: x = 0.8 и y = 3.6
        x_val = 0.8
        y_val = 3.6
        lam = 0.5

        px = axes.coords_to_point(x_val, f(x_val))
        py = axes.coords_to_point(y_val, f(y_val))

        dot_x = m.Dot(px, color=m.YELLOW, radius=0.09)
        dot_y = m.Dot(py, color=m.YELLOW, radius=0.09)

        label_x = m.MathTex("x", color=m.YELLOW, font_size=24)
        label_x.next_to(px, m.DOWN + m.LEFT, buff=0.15)
        label_y = m.MathTex("y", color=m.YELLOW, font_size=24)
        label_y.next_to(py, m.DOWN + m.RIGHT, buff=0.15)

        self.play(
            m.Create(dot_x), m.Create(dot_y),
            m.Write(label_x), m.Write(label_y),
            run_time=0.8
        )
        self.wait(0.3)

        # 4. Отрезок (хорда) между точками
        chord = m.Line(px, py, color=m.GREEN, stroke_width=3)

        self.play(m.Create(chord), run_time=0.8)
        self.wait(0.3)

        # 5. Промежуточные точки
        x_mid_val = lam * x_val + (1 - lam) * y_val
        y_chord_val = lam * f(x_val) + (1 - lam) * f(y_val)
        y_graph_val = f(x_mid_val)

        p_chord = axes.coords_to_point(x_mid_val, y_chord_val)
        p_graph = axes.coords_to_point(x_mid_val, y_graph_val)

        dot_chord = m.Dot(p_chord, color=m.RED, radius=0.05)
        dot_graph = m.Dot(p_graph, color=m.RED, radius=0.05)

        # Вертикальная линия от графика к хорде
        vertical_line = m.DashedLine(
            start=p_graph,
            end=p_chord,
            color=m.RED,
            stroke_width=3,
            dash_length=0.08
        )

        self.play(m.Create(dot_chord), m.Create(dot_graph), run_time=0.6)
        self.play(m.Create(vertical_line), run_time=0.5)
        self.wait(0.3)

        # 6. Подписи для промежуточных точек — разносим, чтобы не накладывались
        # Подпись верхней точки (на хорде) — слева и выше
        '''chord_point_label = m.MathTex(
            r"\lambda f(x) + (1-\lambda) f(y)",
            color=m.RED, font_size=22
        )
        chord_point_label.next_to(dot_chord, m.LEFT, buff=0.25)
        chord_point_label.shift(m.UP * 0.1)

        # Подпись нижней точки (на графике) — справа и ниже
        graph_point_label = m.MathTex(
            r"f(\lambda x + (1-\lambda) y)",
            color=m.ORANGE, font_size=22
        )
        graph_point_label.next_to(dot_graph, m.RIGHT, buff=0.25)
        graph_point_label.shift(m.DOWN * 0.1)

        self.play(m.Write(chord_point_label), run_time=0.6)
        self.play(m.Write(graph_point_label), run_time=0.6)
        self.wait(0.3)'''

        # 7. Подпись "зазор выпуклости" — слева от вертикальной линии, чтобы не пересекалась с графиком
        gap_label = m.Text(
            "зазор выпуклости",
            color=m.RED,
            font_size=22
        )
        gap_label.next_to(vertical_line, m.RIGHT, buff=0.7)

        self.play(m.Write(gap_label), run_time=0.5)
        self.wait(0.3)

        # 8. Формула выпуклости
        convexity_formula = m.MathTex(
            r"f(\lambda x + (1-\lambda) y) \leq \lambda f(x) + (1-\lambda) f(y)",
            font_size=24,
            color=m.BLACK
        )
        convexity_formula.to_edge(m.UP, buff=1.6)
        self.play(m.Write(convexity_formula), run_time=0.8)
        self.wait(0.3)

        # 9. Заголовок
        '''title = m.Text(
            "Определение выпуклости функции",
            font_size=30,
            color=m.BLACK
        )
        title.to_edge(m.UP, buff=0.3)
        self.play(m.Write(title), run_time=0.6)'''

        self.wait(2)

class ParametricCircle(Scene_):
    """
    Глава 4, Анимация 7: Параметрическая кривая — окружность.
    Точка с координатами (cos t, sin t) движется по окружности,
    рядом показаны графики cos t и sin t как функций времени.
    """
    def construct(self):
        # Единый единичный отрезок для обеих систем координат
        unit = 0.85

        # ========== ЛЕВАЯ ЧАСТЬ: ОКРУЖНОСТЬ ==========
        axes_left = m.Axes(
            x_range=[-1.5, 1.5, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=3 * unit,
            y_length=3 * unit,
            axis_config={"color": m.GRAY, "stroke_width": 2, "include_tip": False},
            x_axis_config={"numbers_to_include": [-1, 0, 1], "font_size": 20},
            y_axis_config={"numbers_to_include": [-1, 0, 1], "font_size": 20},
        )
        axes_left.shift(m.LEFT * 4.0 + m.DOWN * 0.5)

        circle = m.Circle(radius=axes_left.x_axis.unit_size, color=m.BLUE, stroke_width=3)
        circle.move_to(axes_left.coords_to_point(0, 0))

        circle_label = m.MathTex(r"\vec{r}(t) = (\cos t,\ \sin t)", color=m.BLUE, font_size=22)
        circle_label.next_to(circle, m.UP, buff=0.5)

        # ========== ПРАВАЯ ЧАСТЬ: ГРАФИКИ ==========
        axes_right = m.Axes(
            x_range=[0, 2 * np.pi, np.pi / 2],
            y_range=[-1.5, 1.5, 1],
            x_length=2 * np.pi * unit,
            y_length=3 * unit,
            axis_config={"color": m.GRAY, "stroke_width": 2, "include_tip": False},
            x_axis_config={
                "numbers_to_include": [0, np.pi, 2 * np.pi],
                "font_size": 20,
            },
            y_axis_config={"numbers_to_include": [-1, 0, 1], "font_size": 20},
        )
        axes_right.shift(m.RIGHT * 2.0 + m.DOWN * 0.5)

        # Скрываем стандартные числовые подписи по оси t и ставим символьные
        axes_right.x_axis.numbers.set_opacity(0)
        tick_0 = m.MathTex("0", font_size=20, color=m.GRAY)
        tick_0.next_to(axes_right.coords_to_point(0, 0), m.DOWN, buff=0.2)
        tick_pi = m.MathTex(r"\pi", font_size=20, color=m.GRAY)
        tick_pi.next_to(axes_right.coords_to_point(np.pi, 0), m.DOWN, buff=0.2)
        tick_2pi = m.MathTex(r"2\pi", font_size=20, color=m.GRAY)
        tick_2pi.next_to(axes_right.coords_to_point(2 * np.pi, 0), m.DOWN, buff=0.2)
        pi_labels = m.VGroup(tick_0, tick_pi, tick_2pi)

        t_label = m.MathTex("t", font_size=24)
        t_label.next_to(axes_right.x_axis, m.DOWN, buff=0.5)

        cos_graph = axes_right.plot(
            lambda t: np.cos(t),
            x_range=[0, 2 * np.pi, 0.01],
            color=m.RED,
            stroke_width=2.5
        )
        cos_label = m.MathTex(r"\cos t", color=m.RED, font_size=22)
        cos_label.next_to(axes_right.coords_to_point(np.pi, 1), m.UP, buff=0.1)

        sin_graph = axes_right.plot(
            lambda t: np.sin(t),
            x_range=[0, 2 * np.pi, 0.01],
            color=m.GREEN,
            stroke_width=2.5
        )
        sin_label = m.MathTex(r"\sin t", color=m.GREEN, font_size=22)
        sin_label.next_to(axes_right.coords_to_point(np.pi / 2, 1), m.UP, buff=0.1)

        # ========== ДВИЖУЩИЕСЯ ЭЛЕМЕНТЫ ==========
        t_tracker = m.ValueTracker(0.01)  # небольшое смещение, чтобы избежать вырожденных случаев

        origin_left = axes_left.coords_to_point(0, 0)

        def point_pos():
            t = t_tracker.get_value()
            return axes_left.coords_to_point(np.cos(t), np.sin(t))

        # Точка на окружности
        moving_dot = m.Dot(point_pos(), color=m.BLUE, radius=0.08)
        def update_dot(mob):
            mob.move_to(point_pos())
        moving_dot.add_updater(update_dot)

        # Радиус-вектор
        radius_vector = m.Arrow(
            start=origin_left,
            end=point_pos(),
            color=m.BLUE, stroke_width=2, buff=0,
            max_tip_length_to_length_ratio=0.15
        )
        def update_radius(mob):
            new_arrow = m.Arrow(
                start=origin_left,
                end=point_pos(),
                color=m.YELLOW, stroke_width=2, buff=0,
                max_tip_length_to_length_ratio=0.15
            )
            mob.become(new_arrow)
        radius_vector.add_updater(update_radius)

        # Горизонтальная пунктирная линия (проекция sin)
        h_line = m.DashedLine(
            start=axes_left.coords_to_point(0, np.sin(t_tracker.get_value())),
            end=point_pos(),
            color=m.GREEN, stroke_width=2, dash_length=0.05
        )
        def update_h(mob):
            t = t_tracker.get_value()
            new_line = m.DashedLine(
                start=axes_left.coords_to_point(0, np.sin(t)),
                end=point_pos(),
                color=m.GREEN, stroke_width=2, dash_length=0.05
            )
            mob.become(new_line)
        h_line.add_updater(update_h)

        # Вертикальная пунктирная линия (проекция cos)
        v_line = m.DashedLine(
            start=axes_left.coords_to_point(np.cos(t_tracker.get_value()), 0),
            end=point_pos(),
            color=m.RED, stroke_width=2, dash_length=0.05
        )
        def update_v(mob):
            t = t_tracker.get_value()
            new_line = m.DashedLine(
                start=axes_left.coords_to_point(np.cos(t), 0),
                end=point_pos(),
                color=m.RED, stroke_width=2, dash_length=0.05
            )
            mob.become(new_line)
        v_line.add_updater(update_v)

        # Маркер t на правой оси
        t_marker = m.DashedLine(
            start=axes_right.coords_to_point(t_tracker.get_value(), -1.5),
            end=axes_right.coords_to_point(t_tracker.get_value(), 1.5),
            color=m.YELLOW, stroke_width=2, dash_length=0.05
        )
        def update_t_marker(mob):
            t = t_tracker.get_value()
            new_line = m.DashedLine(
                start=axes_right.coords_to_point(t, -1.5),
                end=axes_right.coords_to_point(t, 1.5),
                color=m.YELLOW, stroke_width=2, dash_length=0.05
            )
            mob.become(new_line)
        t_marker.add_updater(update_t_marker)

        # Точка на графике cos
        cos_dot = m.Dot(
            axes_right.coords_to_point(t_tracker.get_value(), np.cos(t_tracker.get_value())),
            color=m.RED, radius=0.09
        )
        def update_cos_dot(mob):
            t = t_tracker.get_value()
            mob.move_to(axes_right.coords_to_point(t, np.cos(t)))
        cos_dot.add_updater(update_cos_dot)

        # Точка на графике sin
        sin_dot = m.Dot(
            axes_right.coords_to_point(t_tracker.get_value(), np.sin(t_tracker.get_value())),
            color=m.GREEN, radius=0.09
        )
        def update_sin_dot(mob):
            t = t_tracker.get_value()
            mob.move_to(axes_right.coords_to_point(t, np.sin(t)))
        sin_dot.add_updater(update_sin_dot)

        # ========== АНИМАЦИЯ ==========
        # 1. Оси и подписи
        self.play(
            m.Create(axes_left),
            m.Create(axes_right),
            m.Write(pi_labels),
            m.Write(t_label),
            run_time=0.8
        )
        self.wait(0.2)

        # 2. Графики
        self.play(m.Create(cos_graph), m.Create(sin_graph), run_time=1)
        self.play(m.Write(cos_label), m.Write(sin_label), run_time=0.5)
        self.wait(0.2)

        # 3. Окружность
        self.play(m.Create(circle), run_time=0.8)
        self.play(m.Write(circle_label), run_time=0.5)
        self.wait(0.2)

        # 4. Движущиеся элементы
        self.play(
            m.Create(moving_dot),
            m.Create(radius_vector),
            m.Create(h_line),
            m.Create(v_line),
            m.Create(t_marker),
            m.Create(cos_dot),
            m.Create(sin_dot),
            run_time=0.5
        )
        self.wait(0.3)

        # 5. Движение точки от 0 до 2π
        self.play(
            t_tracker.animate.set_value(2 * np.pi),
            run_time=8,
            rate_func=m.linear
        )
        self.wait(0.5)

        # 6. Пояснение внизу
        note = m.Text(
            "t — параметр (время), (cos t, sin t) — точка на окружности",
            font_size=22, color=m.BLACK
        )
        note.to_edge(m.DOWN, buff=0.3)
        self.play(m.Write(note), run_time=0.8)

        self.wait(2)

class VectorFieldDeformation(Scene_):
    """
    Глава 4, Анимация 8: Деформация пространства нелинейным отображением.
    На плоскости нарисована регулярная сетка из синих линий;
    применяется отображение f(x, y) = (x + 0.5·sin(y), y + 0.3·x²/(1 + x²)),
    линии сетки плавно изгибаются, превращаясь в искажённую сетку.
    """
    def construct(self):
        # 1. Координатная плоскость
        axes = m.Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=9,
            y_length=6.5,
            axis_config={"color": m.GRAY, "stroke_width": 1.5, "include_tip": False},
            x_axis_config={"numbers_to_include": [-3, -2, -1, 0, 1, 2, 3], "font_size": 18},
            y_axis_config={"numbers_to_include": [-2, -1, 0, 1, 2], "font_size": 18},
        )
        axes.shift(m.DOWN * 0.3)

        self.play(m.Create(axes), run_time=0.8)
        self.wait(0.2)

        # 2. Регулярная сетка (синие линии)
        grid_lines = m.VGroup()
        grid_step = 1
        x_vals = np.arange(-3, 4, grid_step)
        y_vals = np.arange(-2, 3, grid_step)

        # Вертикальные линии сетки
        for x in x_vals:
            line = axes.plot(
                lambda y, x=x: x,
                x_range=[-2, 2, 0.05],
                color=m.BLUE,
                stroke_width=1.5,
                stroke_opacity=0.7,
            )
            grid_lines.add(line)

        # Горизонтальные линии сетки
        for y in y_vals:
            line = axes.plot(
                lambda x, y=y: y,
                x_range=[-3, 3, 0.05],
                color=m.BLUE,
                stroke_width=1.5,
                stroke_opacity=0.7,
            )
            grid_lines.add(line)

        self.play(m.Create(grid_lines), run_time=1.5)
        self.wait(0.3)

        # 3. Отдельные точки на сетке (узлы пересечений) — маркеры
        node_points = []
        for x in x_vals:
            for y in y_vals:
                node_points.append(m.Dot(
                    axes.coords_to_point(x, y),
                    color=m.BLUE_A,
                    radius=0.05,
                    fill_opacity=0.8,
                ))
        nodes = m.VGroup(*node_points)

        self.play(m.Create(nodes), run_time=0.8)
        self.wait(0.3)

        # 4. Определяем нелинейное отображение
        def f(x, y):
            new_x = x + 0.5 * np.sin(y)
            new_y = y + 0.3 * x ** 2 / (1 + x ** 2)
            return new_x, new_y

        # 5. Создаём деформированные линии (те же параметрические кривые, 
        #    но каждая точка сдвинута отображением f)
        deformed_lines = m.VGroup()

        for x in x_vals:
            # Кривая: (x, y) для y от -2 до 2, преобразованная через f
            ys = np.linspace(-2, 2, 80)
            points = []
            for y in ys:
                nx, ny = f(x, y)
                points.append(axes.coords_to_point(nx, ny))
            curve = m.VMobject()
            curve.set_points_as_corners(points)
            curve.set_color(m.BLUE)
            curve.set_stroke(width=1.5, opacity=0.7)
            deformed_lines.add(curve)

        for y in y_vals:
            xs = np.linspace(-3, 3, 120)
            points = []
            for x in xs:
                nx, ny = f(x, y)
                points.append(axes.coords_to_point(nx, ny))
            curve = m.VMobject()
            curve.set_points_as_corners(points)
            curve.set_color(m.BLUE)
            curve.set_stroke(width=1.5, opacity=0.7)
            deformed_lines.add(curve)

        # 6. Деформированные точки
        deformed_nodes = m.VGroup()
        for x in x_vals:
            for y in y_vals:
                nx, ny = f(x, y)
                deformed_nodes.add(m.Dot(
                    axes.coords_to_point(nx, ny),
                    color=m.BLUE_A,
                    radius=0.05,
                    fill_opacity=0.8,
                ))

        # 7. Формула отображения
        formula = m.MathTex(
            r"\vec{f}(x, y) = \begin{pmatrix} x + 0.5\sin(y) \\ y + 0.3\dfrac{x^2}{1 + x^2} \end{pmatrix}",
            font_size=28,
            color=m.BLACK,
        )
        formula.to_edge(m.UP, buff=0.3)

        title = m.Text(
            "Деформация пространства нелинейным отображением",
            font_size=26,
            color=m.BLACK,
        )
        title.next_to(formula, m.DOWN, buff=0.2)

        self.play(m.Write(formula), run_time=0.8)
        self.play(m.Write(title), run_time=0.5)
        self.wait(0.3)

        # 8. Анимируем деформацию
        self.play(
            m.Transform(grid_lines, deformed_lines),
            m.Transform(nodes, deformed_nodes),
            run_time=4,
            rate_func=m.smooth,
        )
        self.wait(0.5)

        # 9. Пояснительная подпись внизу
        note = m.Text(
            "Каждая точка переходит в новое место — пространство «деформируется»",
            font_size=22,
            color=m.BLACK,
        )
        note.to_edge(m.DOWN, buff=0.3)
        self.play(m.Write(note), run_time=0.8)

        self.wait(2)

class VectorFieldDeformation2(Scene_):
    """
    Глава 4, Анимация 8: Деформация пространства нелинейным отображением.
    С эффектом "луковой шелухи" — исходное положение остаётся бледным фоном.
    """
    def construct(self):
        # 1. Координатная плоскость
        axes = m.Axes(
            x_range=[-4, 4, 1],
            y_range=[-2.5, 2.5, 0.5],
            x_length=9,
            y_length=5.5,
            axis_config={"color": m.GRAY, "stroke_width": 1.5, "include_tip": False},
            x_axis_config={"numbers_to_include": [-3, -2, -1, 0, 1, 2, 3], "font_size": 18},
            y_axis_config={"numbers_to_include": [-2, -1, 0, 1, 2], "font_size": 18},
        )
        axes.shift(m.DOWN * 0.6)

        self.play(m.Create(axes), run_time=0.8)
        self.wait(0.2)

        # 2. Параметры сетки
        x_vals = np.arange(-3, 4, 1)
        y_vals = np.arange(-2, 3, 1)
        n_points = 80

        # 3. Отображение
        def f(x, y):
            new_x = x + 0.5 * np.sin(y)
            new_y = y + 0.3 * x**2 / (1 + x**2)
            return new_x, new_y

        # 4. Создаём линии
        grid_lines = m.VGroup()
        deformed_lines = m.VGroup()

        # Вертикальные линии
        for x in x_vals:
            ys = np.linspace(-2.5, 2.5, n_points)
            
            orig_points = [axes.coords_to_point(x, y) for y in ys]
            orig_line = m.VMobject()
            orig_line.set_points_as_corners(orig_points)
            orig_line.set_color(m.BLUE)
            orig_line.set_stroke(width=1.5, opacity=0.7)
            grid_lines.add(orig_line)
            
            def_points = [axes.coords_to_point(*f(x, y)) for y in ys]
            def_line = m.VMobject()
            def_line.set_points_as_corners(def_points)
            def_line.set_color(m.BLUE)
            def_line.set_stroke(width=1.5, opacity=0.7)
            deformed_lines.add(def_line)

        # Горизонтальные линии
        for y in y_vals:
            xs = np.linspace(-3, 3, n_points)
            
            orig_points = [axes.coords_to_point(x, y) for x in xs]
            orig_line = m.VMobject()
            orig_line.set_points_as_corners(orig_points)
            orig_line.set_color(m.BLUE)
            orig_line.set_stroke(width=1.5, opacity=0.7)
            grid_lines.add(orig_line)
            
            def_points = [axes.coords_to_point(*f(x, y)) for x in xs]
            def_line = m.VMobject()
            def_line.set_points_as_corners(def_points)
            def_line.set_color(m.BLUE)
            def_line.set_stroke(width=1.5, opacity=0.7)
            deformed_lines.add(def_line)

        self.play(m.Create(grid_lines), run_time=1.5)
        self.wait(0.3)

        # 5. Узлы сетки
        node_points = []
        deformed_node_points = []
        for x in x_vals:
            for y in y_vals:
                node_points.append(m.Dot(
                    axes.coords_to_point(x, y),
                    color=m.BLUE_A,
                    radius=0.05,
                    fill_opacity=0.8,
                ))
                nx, ny = f(x, y)
                deformed_node_points.append(m.Dot(
                    axes.coords_to_point(nx, ny),
                    color=m.BLUE_A,
                    radius=0.05,
                    fill_opacity=0.8,
                ))
        
        nodes = m.VGroup(*node_points)
        deformed_nodes = m.VGroup(*deformed_node_points)

        self.play(m.Create(nodes), run_time=0.8)
        self.wait(0.3)

        # 6. Формула — на месте, где раньше был title (чуть выше центра верхней части)
        formula = m.MathTex(
            r"f(x,y) = \left(x + \tfrac{1}{2}\sin y,\; y + \tfrac{0.3x^2}{1+x^2}\right)",
            font_size=24,
            color=m.BLACK,
        )
        formula.to_edge(m.UP, buff=0.8)  # ← было -0.12, теперь 0.5 (ниже)

        self.play(m.Write(formula), run_time=0.9)
        self.wait(0.3)

        # 7. Создаём "призрачные" копии исходных объектов для эффекта луковой шелухи
        ghost_grid = grid_lines.copy()
        ghost_grid.set_stroke(opacity=0.2)  # очень бледные
        
        ghost_nodes = nodes.copy()
        ghost_nodes.set_fill(opacity=0.2)

        # 8. Анимация деформации с луковой шелухой
        self.play(
            # Показываем призрачные копии на месте
            m.FadeIn(ghost_grid, run_time=0.5),
            m.FadeIn(ghost_nodes, run_time=0.5),
        )
        self.wait(0.3)
        
        # Трансформируем основные объекты, призраки остаются
        self.play(
            m.Transform(grid_lines, deformed_lines),
            m.Transform(nodes, deformed_nodes),
            run_time=4,
            rate_func=m.smooth,
        )
        self.wait(2)

# ========== НАСТРОЙКА ДЛЯ РЕНДЕРИНГА ==========

# Устанавливаем директорию для вывода
OUTPUT_DIR = Path(__file__).parent / "analysis"
OUTPUT_DIR.mkdir(exist_ok=True)
os.environ["MANIM_MEDIA_DIR"] = str(OUTPUT_DIR)

if __name__ == '__main__':
    import subprocess

    SCENES = [
        #"FunctionIntroduction",
        #"FunctionGraphs",
        #"ActivationFunctions",
        #"SqueezeTheorem",
        #"ConvergenceRates",
        #"ConvexityDefinition",
        #"ParametricCircle",
        "VectorFieldDeformation2"
        # Здесь будут другие сцены из главы 4
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