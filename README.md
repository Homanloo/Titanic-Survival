


# Titanic Survival Prediction with ML
A simple study of the Titanic dataset, which is considered as the Hello World of Machine Learning projects.
The project consists of two parts:

 1. Data Analysis and Visualization
 2. Model Selection and Performance Measurement

## Data Analysis
In this section, the overall structure of the dataset is examined. The process consisted of the following steps:

 - Understanding the meaning of each attribute and their types of data.
 - Filling the missing values with the best approach, considering their type and nature.
 - Creating new feature by combining existing ones.
 - Extracting categorical features from numerical features, such as age and fare.
 - Evaluating survival rate for different categories.
 - Visualizing the results using bar charts.

Below is an example for the survival rate based on age:

## Model Selection
In this section, several different models are selected, trained, and their performance is measured using cross validation and training curves.
Below is a list of the models:

 - Logistic Regression
 - Logistic Regression with Cross Validation
 - Stochastic Gradient Descent Classifier
 - Support Vector Classifier
 - Decision Tree
 - Random Forest
 - Voting Classifier
 - Gradient Boosting Classifier

For each model, learning curve is plotted. A few of the models are then selected to be fine-tunned, using Randomized Search and Grid Search for certain hyperparameters.

This is the performance of the selected models:

For the final measurement, all 4 models are used to predict the test set. Overall, Random Forest had the best performance in the test data set. However, the numbers may vary because of the random behavior in data splitting and model training.
## Sources & Useful Tools

 - The data used in this project is originally from the [Titanic Kaggle Competition](https://www.kaggle.com/c/titanic/data). Make sure to check out and participate.
 - Many useful information, maps, and data can be found in the [Encyclopedia Titanica Website](https://www.encyclopedia-titanica.org/titanic-deckplans/d-deck.html).
 - I used [Aquarel](https://github.com/lgienapp/aquarel) to make the default matplotlib plots way more attractive in the Jupyter Notebook.
 - I used [Manim](https://www.manim.community/) to make the animations.