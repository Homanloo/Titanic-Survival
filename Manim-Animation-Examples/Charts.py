from manim import *

class ChangeBarValuesExample(Scene):
    def construct(self):
        values=[-10, -8, -6, -4, -2]

        chart = BarChart(
            values,
            y_range=[-10, 10, 2],
            y_axis_config={"font_size": 24},
        )

        label1 = chart.get_bar_labels(font_size=24)
        self.play(Write(chart), Write(label1))
        
        chart2 = BarChart(
             [2, 4, 6, 8, 10],
            y_range=[-10, 10, 2],
            y_axis_config={"font_size": 24},
        )
        
        label2 = chart2.get_bar_labels(font_size=24)

        self.play(Transform(chart, chart2), Transform(label1, label2))
        self.wait(2)


class Pclass(Scene):
    def construct(self):
        values=[0,0,0]

        chart1 = BarChart(
            values,
            y_range=[0, 600, 100],
            x_length=5,
            bar_names=["Class 3", "Class 1", "Class 2"],
            y_axis_config={"font_size": 24},
        )

        title = Text("Passenger Class", font_size=20, color=BLUE)
        title.next_to(chart1, UP)
        
        self.play(Write(chart1), Write(title))
        
        chart2 = BarChart(
             [491, 216, 184],
            y_range=[0, 600, 100],
            x_length=5,
            bar_names=["Class 3", "Class 1", "Class 2"],
            y_axis_config={"font_size": 24},
        )
        
        label2 = chart2.get_bar_labels(font_size=24)
        

        self.play(Transform(chart1, chart2))
        self.play(Write(label2))
        self.wait(2)
