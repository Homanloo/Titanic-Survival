from manim import *


# Defining the default code block with desired values
class DefaultCode(Code):
    def __init__(self, file_name = None, code = None, tab_width = 3, line_spacing = 0.8, font_size = 18, font = "Monospace", 
                 stroke_width = 0, margin = 0.3, indentation_chars = "    ", background = "window", 
                 background_stroke_width = 1, background_stroke_color = WHITE, corner_radius = 0.2, insert_line_no = True, 
                 line_no_from = 1, line_no_buff = 0.4, style = "native", language = "python", generate_html_file = False, 
                 warn_missing_font = True, **kwargs):
        
        super().__init__(file_name, code, tab_width, line_spacing, font_size, font, stroke_width, margin, indentation_chars, 
                         background, background_stroke_width, background_stroke_color, corner_radius, insert_line_no, 
                         line_no_from, line_no_buff, style, language, generate_html_file, warn_missing_font, **kwargs)



class LoadData(Scene):
    def construct(self):
        code1 = DefaultCode(
            code="""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Data/train.csv")
df.head()
""")
        self.play(Write(code1))
        self.wait(1)



class FeatureEngineering(Scene):
    def construct(self):
        code1 = DefaultCode(
            code="""
# --- Name --- #

# Extracting the title
df["Title"] = df["Name"].apply(lambda x: x.split(", ")[1].split(".")[0])
df.drop(columns=["Name"], inplace=True)
""")
        self.play(Write(code1))
        self.wait(2)

        code2 = DefaultCode(
            code="""
# --- Name --- #

common_titles = ["Mr", "Miss", "Mrs", "Master"]
# If title is not among the list above, change it to rare
df['Title'] = df['Title'].apply(lambda x: x if x in common_titles else "Rare")
# Check if a person holds a rare title or not
df['IsTitleRare'] = df['Title'].apply(lambda x: 1 if x=="Rare" else 0)
""")
        self.play(ReplacementTransform(code1, code2))
        self.wait(2)
        
        code3 = DefaultCode(
            code="""
# --- Age --- #

# Replacing missing age values with the average
df["Age"].fillna(int(df["Age"].median()), inplace=True)

# Defining a new feature - age group
age_bins = [0, 3, 12, 20, 60, 200]
age_labels = ["toddler", "child", "teen", "adult", "senior"]
df["AgeGroup"] = pd.cut(df["Age"], bins=age_bins, labels=age_labels)
""")
        self.play(ReplacementTransform(code2, code3))
        self.wait(2)

        code4 = DefaultCode(
            code="""
# --- SibSp & Parch --- #

# Introducing a new and more meaningful feature
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Defining new feature: If a persons is traveling alone or not
df['IsAlone'] = df['FamilySize'].apply(lambda x: 1 if x==1 else 0)
""")
        self.play(ReplacementTransform(code3, code4))
        self.wait(2)
        
        code5 = DefaultCode(
            code="""
# --- Ticket & Fare --- #

# Adding the number of times a ticket was repeated to the dataframe
ticket_count = df["Ticket"].value_counts()
df["TicketCount"] = df["Ticket"].map(ticket_count)

# Adjusting the ticket price
df["AdjustedFare"] = round(df["Fare"] / df["TicketCount"], 4)
""")
        self.play(ReplacementTransform(code4, code5))
        self.wait(2)
        
        code6 = DefaultCode(
            code="""
# --- Ticket & Fare --- #

# Spliting the passengers to 4 groups based on their wealth
q25, q50, q75 = list(df['AdjustedFare'].quantile([.25, .5, .75]))
print(f"25% Quantile: {q25}")
print(f"50% Quantile: {q50}")
print(f"75% Quantile: {q75}")

fare_bins = [0, q25, q50, q75, df['AdjustedFare'].max()]
fare_labels = ["VeryLow", "Low", "Medium", "High"]
df["Wealth"] = pd.cut(df["AdjustedFare"], bins=fare_bins, labels=fare_labels)
""")
        self.play(ReplacementTransform(code5, code6))
        self.wait(2)
        
        code7 = DefaultCode(
            code="""
# --- Ticket & Fare --- #

df['AdjustedFare'].replace(0, df['AdjustedFare'].median(), inplace=True)
df['LogFare'] = np.log(df['AdjustedFare'])
""")
        self.play(ReplacementTransform(code6, code7))
        self.wait(2)
        
        code8 = DefaultCode(
            code="""
# --- Cabin --- #

# Extracting deck of residance for each passanger - N/A for NaN
df["Deck"] = df["Cabin"].str[0]
df["Deck"].fillna("N/A", inplace=True)

# Defining new feature: If a persons cabin is available or not
df['HasCabin'] = df['Deck'].apply(lambda x: 0 if x=="N/A" else 1)
""")
        self.play(ReplacementTransform(code7, code8))
        self.wait(2)
        
        code9 = DefaultCode(
            code="""
# --- Embarked --- #

# Replacing the missing embarked locations with the most frequent one
df["Embarked"].fillna(df["Embarked"].value_counts(ascending=False).index[0],
                      inplace=True)

# Replacing embarked locations with their full name
location_dict = {"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"}
df["Embarked"].replace(location_dict, inplace=True)
""")
        self.play(ReplacementTransform(code8, code9))
        self.wait(2)