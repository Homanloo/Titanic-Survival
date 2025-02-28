from manim import *

class RawData(Scene):
    def construct(self):
        table = Table(
            [['1', '0', '3', 'Braund, Mr. Owen Harris', 'male', '22.0', '1', '0', 'A/5 21171', '7.25', 'nan', 'S'],
             ['2', '1', '1', 'Cumings, Mrs. John Bradley', 'female', '38.0', '1', '0', 'PC 17599', '71.2833', 'C85', 'C'],
             ['3', '1', '3', 'Heikkinen, Miss. Laina', 'female', '26.0', '0', '0', 'STON/O2. 3101282', '7.925', 'nan', 'S'],
             ['4', '1', '1', 'Futrelle, Mrs. Jacques Heath', 'female', '35.0', '1', '0', '113803', '53.1', 'C123', 'S'],
             ['5', '0', '3', 'Allen, Mr. William Henry', 'male', '35.0', '0', '0', '373450', '8.05', 'nan', 'S']],
            col_labels=[Text('PassengerId'), Text('Survived'), Text('Pclass'), Text('Name'), Text('Sex'), Text('Age'), Text('SibSp'),
                         Text('Parch'), Text('Ticket'), Text('Fare'), Text('Cabin'), Text('Embarked')],
            include_outer_lines=True,
            line_config={"stroke_width": 0.5, "color": WHITE}).scale(0.2)
        self.play(table.create())
        self.wait()