from manim import *


# Defining the default code block with desired values
class DefaultCode(Code):
    def __init__(self, code_file = None, code_string = None, language = "python", formatter_style = "native",
                 tab_width = 4, add_line_numbers = True, line_numbers_from = 1, background = "window",
                 background_config = None, paragraph_config = None):
        super().__init__(code_file, code_string, language, formatter_style, tab_width, add_line_numbers,
                         line_numbers_from, background, background_config, paragraph_config)



class LoadData(Scene):
    def construct(self):
        code = DefaultCode(
            code_string="""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Data/train.csv")
df.head()
""")
        self.play(Write(code))
        self.wait(1)
        
        
        
class Aquarel(Scene):
    def construct(self):
        code = DefaultCode(
            code_string="""
from aquarel import load_theme

# Using the Aquarel library with some customization for the plots
theme = load_theme("boxy_dark")
theme.set_color(figure_background_color="#181818",
                plot_background_color="#242424")
theme.set_font(family="monospace", size=9)
theme.apply_transforms()
theme.apply()
""")
        self.play(Write(code))
        self.wait(1)



class FeatureEngineering(Scene):
    def construct(self):
        code1 = DefaultCode(
            code_string="""
# --- Name --- #

# Extracting the title
df["Title"] = df["Name"].apply(lambda x: x.split(", ")[1].split(".")[0])
df.drop(columns=["Name"], inplace=True)
""")
        self.play(Write(code1))
        self.wait(2)

        code2 = DefaultCode(
            code_string="""
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
            code_string="""
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
            code_string="""
# --- SibSp & Parch --- #

# Introducing a new and more meaningful feature
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Defining new feature: If a persons is traveling alone or not
df['IsAlone'] = df['FamilySize'].apply(lambda x: 1 if x==1 else 0)
""")
        self.play(ReplacementTransform(code3, code4))
        self.wait(2)
        
        code5 = DefaultCode(
            code_string="""
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
            code_string="""
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
            code_string="""
# --- Ticket & Fare --- #

df['AdjustedFare'].replace(0, df['AdjustedFare'].median(), inplace=True)
df['LogFare'] = np.log(df['AdjustedFare'])
""")
        self.play(ReplacementTransform(code6, code7))
        self.wait(2)
        
        code8 = DefaultCode(
            code_string="""
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
            code_string="""
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
        
        
class OHEAndCorrMat(Scene):
    def construct(self):
        code1 = DefaultCode(
            code_string="""
def custome_ohe(df:pd.DataFrame, column:str, drop_original:bool=False):
    
    try:
        target_column = df[column]
        target_values = list(target_column.unique())
        for val in target_values:
            feature_title = f"{column}_{val}"
            df[feature_title] = df[column].map(
                lambda x: 1 if x == val else 0
            )
        if drop_original == True:
            df.drop(columns=[column], inplace=True, errors="ignore")
    except:
        if column not in df.columns:
            print(f"Column {column} does not exist in the dataframe.")
        else:
            print("The function is unable to one-hot-encode the column.")
""")
        self.play(Write(code1))
        self.wait(1)

        code2 =DefaultCode(
            code_string="""
ohe_columns = ['Pclass', 'Sex', 'Embarked',
               'Deck', 'AgeGroup', 'Title',
               'Wealth']

for col in ohe_columns:
    custome_ohe(df=df, column=col, drop_original=True)        
""")
        self.play(ReplacementTransform(code1, code2))
        self.wait(1)
        
        code3 =DefaultCode(
            code_string="""
df_corr = df.corr()

fig, ax = plt.subplots(figsize=(15, 15), dpi=300)
corr_mat = ax.imshow(df_corr, cmap='Blues')
plt.colorbar(corr_mat)
features = [x for x in df_corr.columns]
plt.xticks(range(len(df_corr)), features, rotation=90, ha='right')
plt.yticks(range(len(df_corr)), features)
plt.tick_params(labeltop=True)
plt.suptitle("Correlation Matrix")

plt.tight_layout()
plt.show(fig)       
""")
        self.play(ReplacementTransform(code2, code3))
        self.wait(1)
        self.play(FadeOut(code3))
        
        
class GroupPlot(Scene):
    def construct(self):
        code = DefaultCode(
            code_string="""
# A function to plot the survival rate based on the given column values
def group_plot(df=df, column="Sex", plot_type="bar"):
    
    grouped_attribute = df.groupby(column, observed=False)['Survived']
    attribute_survival_rate = grouped_attribute.mean()
    
    if plot_type == "bar":
        grouped_plot = attribute_survival_rate.plot(
            kind="bar",
            ylabel="Chance of Survival",
            xlabel=str(column),
            title=str(column),
            rot=0)
        
    elif plot_type == "barh":
        grouped_plot = attribute_survival_rate.plot(
            kind="barh",
            xlabel="Chance of Survival",
            ylabel=str(column),
            title=str(column),
            rot=0)
    else:
        return "Invalid"
    
    return plt.show(grouped_plot)
""").scale(0.6)
        self.play(Write(code))
        self.wait(1)
        
        
class DoubleGroupExample(Scene):
    def construct(self):
        code = DefaultCode(
            code_string="""
# Survival based on class and gender
grouped_pclass_sex_survived = pd.DataFrame(df.groupby(['Pclass', 'Sex'])['Survived'].mean())
""").scale(0.6)
        self.play(Write(code))
        self.wait(1)