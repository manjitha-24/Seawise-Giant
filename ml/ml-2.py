import numpy as np 

# data processing
import pandas as pd 



# Algorithms
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.naive_bayes import GaussianNB
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
import pandas as pd
import tkinter as tk
from tkinter.font import Font
from sklearn.ensemble import RandomForestClassifier

test_df = pd.read_csv("C:\\Users\\mudiy\\OneDrive\\Desktop\\ml\\test.csv")
train_df = pd.read_csv("C:\\Users\\mudiy\\OneDrive\\Desktop\\ml\\train.csv")

total = train_df.isnull().sum().sort_values(ascending=False)
percent_1 = train_df.isnull().sum()/train_df.isnull().count()*100
percent_2 = (round(percent_1, 1)).sort_values(ascending=False)
missing_data = pd.concat([total, percent_2], axis=1, keys=['Total', '%'])

survived = 'survived'
not_survived = 'not survived'

women = train_df[train_df['Sex']=='female']
men = train_df[train_df['Sex']=='male']


data = [train_df, test_df]
for dataset in data:
    dataset['relatives'] = dataset['SibSp'] + dataset['Parch']
    dataset.loc[dataset['relatives'] > 0, 'not_alone'] = 0
    dataset.loc[dataset['relatives'] == 0, 'not_alone'] = 1
    dataset['not_alone'] = dataset['not_alone'].astype(int)

import re
deck = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "U": 8}
data = [train_df, test_df]

for dataset in data:
    dataset['Cabin'] = dataset['Cabin'].fillna("U0")
    dataset['Deck'] = dataset['Cabin'].map(lambda x: re.compile("([a-zA-Z]+)").search(x).group())
    dataset['Deck'] = dataset['Deck'].map(deck)
    dataset['Deck'] = dataset['Deck'].fillna(0)
    dataset['Deck'] = dataset['Deck'].astype(int)
# we can now drop the cabin feature
train_df = train_df.drop(['Cabin'], axis=1)
test_df = test_df.drop(['Cabin'], axis=1)

data = [train_df, test_df]

for dataset in data:
    mean = train_df["Age"].mean()
    std = test_df["Age"].std()
    is_null = dataset["Age"].isnull().sum()
    # compute random numbers between the mean, std and is_null
    rand_age = np.random.randint(mean - std, mean + std, size = is_null)
    # fill NaN values in Age column with random values generated
    age_slice = dataset["Age"].copy()
    age_slice[np.isnan(age_slice)] = rand_age
    dataset["Age"] = age_slice
    dataset["Age"] = train_df["Age"].astype(int)
train_df["Age"].isnull().sum()

common_value = 'S'
data = [train_df, test_df]

for dataset in data:
    dataset['Embarked'] = dataset['Embarked'].fillna(common_value)

    data = [train_df, test_df]

for dataset in data:
    dataset['Fare'] = dataset['Fare'].fillna(0)
    dataset['Fare'] = dataset['Fare'].astype(int)

    data = [train_df, test_df]
titles = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}

for dataset in data:
    # extract titles
    dataset['Title'] = dataset.Name.str.extract(' ([A-Za-z]+)\.', expand=False)
    # replace titles with a more common title or as Rare
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess','Capt', 'Col','Don', 'Dr',\
                                            'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')
    # convert titles into numbers
    dataset['Title'] = dataset['Title'].map(titles)
    # filling NaN with 0, to get safe
    dataset['Title'] = dataset['Title'].fillna(0)
train_df = train_df.drop(['Name'], axis=1)
test_df = test_df.drop(['Name'], axis=1)

genders = {"male": 0, "female": 1}
data = [train_df, test_df]

for dataset in data:
    dataset['Sex'] = dataset['Sex'].map(genders)

train_df = train_df.drop(['Ticket'], axis=1)
test_df = test_df.drop(['Ticket'], axis=1)

ports = {"S": 0, "C": 1, "Q": 2}
data = [train_df, test_df]

for dataset in data:
    dataset['Embarked'] = dataset['Embarked'].map(ports)

data = [train_df, test_df]
for dataset in data:
    #dataset['Age'] = dataset['Age'].astype(int)
    dataset.loc[ dataset['Age'] <= 11, 'Age'] = 0
    dataset.loc[(dataset['Age'] > 11) & (dataset['Age'] <= 18), 'Age'] = 1
    dataset.loc[(dataset['Age'] > 18) & (dataset['Age'] <= 22), 'Age'] = 2
    dataset.loc[(dataset['Age'] > 22) & (dataset['Age'] <= 27), 'Age'] = 3
    dataset.loc[(dataset['Age'] > 27) & (dataset['Age'] <= 33), 'Age'] = 4
    dataset.loc[(dataset['Age'] > 33) & (dataset['Age'] <= 40), 'Age'] = 5
    dataset.loc[(dataset['Age'] > 40) & (dataset['Age'] <= 66), 'Age'] = 6
    dataset.loc[ dataset['Age'] > 66, 'Age'] = 6


data = [train_df, test_df]

for dataset in data:
    dataset.loc[ dataset['Fare'] <= 7.91, 'Fare'] = 0
    dataset.loc[(dataset['Fare'] > 7.91) & (dataset['Fare'] <= 14.454), 'Fare'] = 1
    dataset.loc[(dataset['Fare'] > 14.454) & (dataset['Fare'] <= 31), 'Fare']   = 2
    dataset.loc[(dataset['Fare'] > 31) & (dataset['Fare'] <= 99), 'Fare']   = 3
    dataset.loc[(dataset['Fare'] > 99) & (dataset['Fare'] <= 250), 'Fare']   = 4
    dataset.loc[ dataset['Fare'] > 250, 'Fare'] = 5
    dataset['Fare'] = dataset['Fare'].astype(int)

data = [train_df, test_df]
for dataset in data:
    dataset['Age_Class']= dataset['Age']* dataset['Pclass']

    for dataset in data:
        dataset['Fare_Per_Person'] = dataset['Fare']/(dataset['relatives']+1)
        dataset['Fare_Per_Person'] = dataset['Fare_Per_Person'].astype(int)

X_train = train_df.drop("Survived", axis=1)
Y_train = train_df["Survived"]
X_test  = test_df.drop("PassengerId", axis=1).copy()


model = RandomForestClassifier(n_estimators=100, max_depth=5)
model.fit(X_train,Y_train)


importances = pd.DataFrame({'feature':X_train.columns,'importance':np.round(model.feature_importances_,3)})
importances = importances.sort_values('importance',ascending=False).set_index('feature')

train_df  = train_df.drop("not_alone", axis=1)
test_df  = test_df.drop("not_alone", axis=1)

train_df  = train_df.drop("Parch", axis=1)
test_df  = test_df.drop("Parch", axis=1)




root = tk.Tk()
root.title('Titanic Survival Predictor')

# Define the widgets
class_label = tk.Label(root, text='Passenger Class (1-3):')
class_entry = tk.Entry(root)

sex_label = tk.Label(root, text='Passenger Sex (0=male, 1=female):')
sex_entry = tk.Entry(root)

age_label = tk.Label(root, text='Passenger Age:')
age_entry = tk.Entry(root)

sibsp_label = tk.Label(root, text='Number of Siblings/Spouses:')
sibsp_entry = tk.Entry(root)

parch_label = tk.Label(root, text='Number of Parents/Children:')
parch_entry = tk.Entry(root)

fare_label = tk.Label(root, text='Passenger Fare:')
fare_entry = tk.Entry(root)

output_label = tk.Label(root, text='')




def predict_survival():
    passenger = [[int(class_entry.get()), int(sex_entry.get()), float(age_entry.get()),
                  int(sibsp_entry.get()), int(parch_entry.get()), float(fare_entry.get())]]
    
    df = pd.DataFrame.from_dict(
        {
            "Pclass": [class_entry + 1],
            "Sex": [0 if sex_entry else 1],
            "Age": [age_entry],
            "Fare": [fare_entry],
           
            "Company": [
                (1 if "Sibling" in sibsp_entry else 0) + (2 if "Child" in parch_entry else 0)
            ]
        }
    )
   
    prediction = model.predict(passenger)[0]
    if prediction == 0:
        output_label.config(text='The passenger did not survive.')
    else:
        output_label.config(text='The passenger survived!')




# Define the submit button
submit_button = tk.Button(root, text='Predict Survival', command=predict_survival)

# Pack the widgets
class_label.pack()
class_entry.pack()

sex_label.pack()
sex_entry.pack()

age_label.pack()
age_entry.pack()

sibsp_label.pack()
sibsp_entry.pack()

parch_label.pack()
parch_entry.pack()

fare_label.pack()
fare_entry.pack()

submit_button.pack()

output_label.pack()

root.mainloop()