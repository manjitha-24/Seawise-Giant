import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib
matplotlib.use('Agg')
import tkinter as tk
from tkinter.font import Font
from tkinter import*
from PIL import ImageTk,Image

# Load the Titanic dataset

titanic_df = pd.read_csv("C:\\Users\\mudiy\\OneDrive\\Desktop\\ml\\train.csv")

# Define the features and target
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
target = 'Survived'

#preprocess the data
titanic_df['Sex'] = titanic_df['Sex'].map({'female': 1, 'male': 0})
titanic_df = titanic_df.dropna()

# Train the model
X = titanic_df[features]
y = titanic_df[target]
model = RandomForestClassifier(n_estimators=100, max_depth=5)
model.fit(X, y)

# Define the GUI
root = tk.Tk()
root.title('Titanic Survival Predictor')

image = Image.open("C:\\Users\\mudiy\\OneDrive\\Desktop\\ml\\titanic-image.png")
background_image = ImageTk.PhotoImage(image)
# Create a label and add the image to it
label = Label(root, image=background_image)
label.place(x=0, y=0, relwidth=1, relheight=1)
registration_frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
registration_frame.pack(padx=400, pady=100)
input_frame = tk.Frame(root, borderwidth=5, relief="ridge")
input_frame.place(relx=0.5, rely=0.15, relwidth=0.3, relheight=0.8, anchor="n")
# Define the widgets
class_label = tk.Label(root, text='Passenger Class (1-3):')
class_entry = tk.Entry(root)
font = Font(size=15)
class_label.config(font=font)
class_entry.config(font=font)
sex_label = tk.Label(root, text='Passenger Sex (0=male, 1=female):')
sex_entry = tk.Entry(root)
font = Font(size=15)
sex_label.config(font=font)
sex_entry.config(font=font)

age_label = tk.Label(root, text='Passenger Age:')
age_entry = tk.Entry(root)
font = Font(size=15)
age_label.config(font=font)
age_entry.config(font=font)
sibsp_label = tk.Label(root, text='Number of Siblings/Spouses:')
sibsp_entry = tk.Entry(root)
font = Font(size=15)
sibsp_label.config(font=font)
sibsp_entry.config(font=font)
parch_label = tk.Label(root, text='Number of Parents/Children:')
parch_entry = tk.Entry(root)
font = Font(size=15)
parch_label.config(font=font)
parch_entry.config(font=font)
fare_label = tk.Label(root, text='Passenger Fare:')
fare_entry = tk.Entry(root)
font = Font(size=15)
fare_label.config(font=font)
fare_entry.config(font=font)
output_label = tk.Label(root, text='')
font = Font(size=15)
output_label.config(font=font)
# Define the predict function
def predict_survival():
    passenger = [[int(class_entry.get()), int(sex_entry.get()), float(age_entry.get()),
                  int(sibsp_entry.get()), int(parch_entry.get()), float(fare_entry.get())]]
    prediction = model.predict(passenger)[0]
    if prediction == 0:
        output_label.config(text='The passenger did not survive.')
    else:
        output_label.config(text='The passenger survived!')

# Define the submit button
submit_button = tk.Button(root, text='Predict Survival', command=predict_survival,width=20, height=3)

# Pack the widgets
class_label.pack(padx = 5,pady=5)
class_entry.pack(padx =5,pady=5)

sex_label.pack(padx = 5,pady=5)
sex_entry.pack(padx = 5,pady=5)

age_label.pack(padx = 5,pady=5)
age_entry.pack(padx = 5,pady=5)

sibsp_label.pack(padx = 5,pady=5)
sibsp_entry.pack(padx = 5,pady=5)

parch_label.pack(padx = 5,pady=5)
parch_entry.pack(padx = 5,pady=5)

fare_label.pack(padx = 5,pady=5)
fare_entry.pack(padx = 5,pady=5)

submit_button.pack(padx = 5,pady=5)

output_label.pack(padx = 5,pady=5)

root.mainloop()