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

# ========== НАСТРОЙКА ДЛЯ РЕНДЕРИНГА ==========

# Устанавливаем директорию для вывода
OUTPUT_DIR = Path(__file__).parent / "analysis"
OUTPUT_DIR.mkdir(exist_ok=True)
os.environ["MANIM_MEDIA_DIR"] = str(OUTPUT_DIR)

if __name__ == '__main__':
    import subprocess

    SCENES = [
        "FunctionIntroduction",
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