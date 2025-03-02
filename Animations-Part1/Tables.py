from manim import *

class RawData(MovingCameraScene):
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
            line_config={"stroke_width": 0.5, "color": WHITE}).scale(0.25)
        table_columns = table.get_col_labels()
        for label in table_columns:
            label.set_color(BLUE)
        self.play(table.create())
        self.wait(2)
        
        def march_table(table):
            n_columns = len(list(table.get_col_labels()))
            for i in range(n_columns):
                self.play(self.camera.frame.animate.set(width=8).move_to(table.get_entries((1, i+1))))
                self.play(Indicate(table.get_entries((1, i+1))))
                self.wait(1)
        
        self.camera.frame.save_state()        
        march_table(table)
        self.play(Restore(self.camera.frame))
        self.wait(2)
        

class Name(Scene):
    def construct(self):
        table1 = Table(
            [["...", "Braund, Mr. Owen Harris", "..."],
            ["...", "Cumings, Mrs. John Bradley", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("Name", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)
        
        table2 = Table(
            [["...", "Braund, Mr. Owen Harris", "Mr", "..."],
            ["...", "Cumings, Mrs. John Bradley", "Mrs", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("Name", color=BLUE, weight=HEAVY),
                        Text("Title", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)
    
        table3 = Table(
            [["...", "Braund, Mr. Owen Harris", "Mr", "0", "..."],
            ["...", "Cumings, Mrs. John Bradley", "Mrs", "0", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("Name", color=BLUE, weight=HEAVY),
                        Text("Title", color=BLUE, weight=HEAVY),
                        Text("IsTitleRare", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)

        self.play(table1.create())
        self.wait(1)
        self.play(ReplacementTransform(table1, table2))
        self.wait(1)
        self.play(ReplacementTransform(table2, table3))
        self.wait(1)


class Age(Scene):
    def construct(self):
        table1 = Table(
            [["...", "65", "..."],
            ["...", "NaN", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("Age", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)
        
        table2 = Table(
            [["...", "65", "..."],
            ["...", "28", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("Age", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)
    
        table3 = Table(
            [["...", "65", "senior", "..."],
            ["...", "28", "adult", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("Age", color=BLUE, weight=HEAVY),
                        Text("AgeGroup", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)

        self.play(table1.create())
        self.wait(1)
        self.play(ReplacementTransform(table1, table2))
        self.wait(1)
        self.play(ReplacementTransform(table2, table3))
        self.wait(1)
        
        
class SibspParch(Scene):
    def construct(self):
        table1 = Table(
            [["...", "1", "3", "..."],
            ["...", "0", "0", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("SibSp", color=BLUE, weight=HEAVY),
                        Text("Parch", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)
        
        table2 = Table(
            [["...", "1", "3", "5", "..."],
            ["...", "0", "0", "1", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("SibSp", color=BLUE, weight=HEAVY),
                        Text("Parch", color=BLUE, weight=HEAVY),
                        Text("FamilySize", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)

        self.play(table1.create())
        self.wait(1)
        self.play(ReplacementTransform(table1, table2))
        self.wait(1)
        
        
class TicketFare(Scene):
    def construct(self):
        table1 = Table(
            [["...", "CA 2144 ", "75.0000", "..."],
            ["...", "PC 17612 ", "1", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("Ticket", color=BLUE, weight=HEAVY),
                        Text("Fare", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)
        
        table2 = Table(
            [["...", "CA 2144 ", "75.0000", "6", "..."],
            ["...", "PC 17612 ", "7.2400", "1", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("Ticket", color=BLUE, weight=HEAVY),
                        Text("Fare", color=BLUE, weight=HEAVY),
                        Text("TicketCount", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)
        
        table3 = Table(
            [["...", "CA 2144 ", "75.0000", "6", "12.5000", "..."],
            ["...", "PC 17612 ", "7.2400", "1", "7.2400", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("Ticket", color=BLUE, weight=HEAVY),
                        Text("Fare", color=BLUE, weight=HEAVY),
                        Text("TicketCount", color=BLUE, weight=HEAVY),
                        Text("AdjustedFare", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)
        
        table4 = Table(
            [["...", "CA 2144 ", "75.0000", "6", "12.5000", "Medium", "..."],
            ["...", "PC 17612 ", "7.2400", "1", "7.2400", "VeryLow", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("Ticket", color=BLUE, weight=HEAVY),
                        Text("Fare", color=BLUE, weight=HEAVY),
                        Text("TicketCount", color=BLUE, weight=HEAVY),
                        Text("AdjustedFare", color=BLUE, weight=HEAVY),
                        Text("Wealth", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)

        self.play(table1.create())
        self.wait(1)
        self.play(ReplacementTransform(table1, table2))
        self.wait(1)
        self.play(ReplacementTransform(table2, table3))
        self.wait(1)
        self.play(ReplacementTransform(table3, table4))
        self.wait(1)


class Cabin(Scene):
    def construct(self):
        table1 = Table(
            [["...", "NaN", "..."],
            ["...", "C85", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("Cabin", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)
        
        table2 = Table(
            [["...", "NaN", "N/A", "..."],
            ["...", "C85", "C", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("Cabin", color=BLUE, weight=HEAVY),
                        Text("Deck", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)
        
        table3 = Table(
            [["...", "NaN", "N/A", "0", "..."],
            ["...", "C85", "C", "1", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("Cabin", color=BLUE, weight=HEAVY),
                        Text("Deck", color=BLUE, weight=HEAVY),
                        Text("HasCabin", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)

        self.play(table1.create())
        self.wait(1)
        self.play(ReplacementTransform(table1, table2))
        self.wait(1)
        self.play(ReplacementTransform(table2, table3))
        self.wait(1)
        
        
class Embarked(Scene):
    def construct(self):
        table1 = Table(
            [["...", "NaN", "..."],
            ["...", "Q", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("Embarked", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)
        
        table2 = Table(
            [["...", "S", "..."],
            ["...", "Q", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("Embarked", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)
        
        table3 = Table(
            [["...", "Southampton", "..."],
            ["...", "Queenstown", "..."]],
            col_labels=[Text("...", color=BLUE, weight=HEAVY),
                        Text("Embarked", color=BLUE, weight=HEAVY),
                        Text("...", color=BLUE, weight=HEAVY)],
            include_outer_lines=False).scale(0.6)

        self.play(table1.create())
        self.wait(1)
        self.play(ReplacementTransform(table1, table2))
        self.wait(1)
        self.play(ReplacementTransform(table2, table3))
        self.wait(1)
        
        
class PclassSexSurvived(Scene):
    def construct(self):
        table1 = Table(
            [["1", "female", "0.968085"],
            ["1", "male", "0.368852"],
            ["2", "female", "0.921053"],
            ["2", "male", "0.157407"],
            ["3", "female", "0.500000"],
            ["3", "male", "0.135447"],],
            col_labels=[Text("Pclass", color=BLUE, weight=HEAVY),
                        Text("Sex", color=BLUE, weight=HEAVY),
                        Text("SurvivalRate", color=BLUE, weight=HEAVY)],
            include_outer_lines=True).scale(0.6)


        self.play(table1.create())
        self.wait(1)