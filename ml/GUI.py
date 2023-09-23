# This program consists of clean and polished Graphical User Interface (GUI) that interacts with 8 Machine Learning models and data visualization tools through the use of different Python libraries. 
# The user can interact with the GUI through selecting which model to run on the testing data on, which then takes them to a screen displaying the prediction results of the testing data as well as the general model accuracy. 
# The screen also includes various buttons that, when selected, display complex and attractive data visualizations on the testing data.
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import dataPreprocessing
import machineLearningModels
import pandas as pd

class root(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1500x600+0+0")
        self.title("Seawise giant Disaster Platform")
        container = tk.Frame(self)
       # container.geometry("500x500")
        
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 3)
        container.grid_columnconfigure(0, weight = 3)
        
       # container.place(x = 500, y = 1500)
        self.frames = {}

        for F in (StartPage, Page1, Page2, Page3, Page4):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "snew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        load1 = Image.open('C:\\Users\\mudiy\\OneDrive\\Desktop\\ml\\titanic-image.png')
        render1 = ImageTk.PhotoImage(load1)
        img1 = tk.Label(self, image = render1)
        img1.image = render1
        img1.place(x = 0, y = 0)
        
        load2 = Image.open('C:\\Users\\mudiy\\OneDrive\\Desktop\\ml\\titanic-image.png')
        render2 = ImageTk.PhotoImage(load2)
        img2 = tk.Label(self, image = render2)
        img2.image = render2
        img2.place(x = 65, y = 25)

        load3 = Image.open('C:\\Users\\mudiy\\OneDrive\\Desktop\\ml\\titanic-image.png')
        render3 = ImageTk.PhotoImage(load3)
        img3 = tk.Label(self, image = render3)
        img3.image = render3
        img3.place(x = 1175, y = 25)

        labelA = tk.Label(self, text= "These three buttons will help you understand\nand visualize the type of people that were on the Titanic\n by showing graphs of some interesting correlations\n that occur with survival/death rates\nand other passenger attributes.")
        labelA.place(x = 500, y = 500)


        buttonA = tk.Button(self, text = "Train Distribution", command = lambda: machineLearningModels.trainclassDistr(machineLearningModels.train_df))
        buttonA.place(x = 800, y = 650)

        buttonB = tk.Button(self, text = "Mean Fare Survival", command = lambda: machineLearningModels.trainMeanFareSurvival(machineLearningModels.train_df))
        buttonB.place(x = 400, y = 650)

        buttonC = tk.Button(self, text = "Class Survival", command = lambda: machineLearningModels.trainClassSurvival(machineLearningModels.train_df))
        buttonC.place(x = 600, y = 650)

        label = tk.Label(self , text= "Welcome to the SEAWISE GIANT DATA ANALYSIS PLATFORM!\n\n Here you can run algorithms and see data on the disaster that occurred in 1912 based on real passenger data.\n")
        label.place(x = 400, y = 150)
       
      
        button = tk.Button(self, text = "Log Regression", command = lambda: controller.show_frame(Page1))
        button.place(x = 500, y = 300)
        
        
        button2 = tk.Button(self, text = "K Nearest Neighbor", command = lambda: controller.show_frame(Page2))
        button2.place(x = 700, y = 300)
        

        button3 = tk.Button(self, text = "Random Forest", command = lambda: controller.show_frame(Page3))
        button3.place(x = 700, y = 400)

        button4 = tk.Button(self, text = "Decision Tree", command = lambda: controller.show_frame(Page4))
        button4.place(x = 500, y = 400)


       
class Page1(tk.Frame):        
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                
                load1 = Image.open('C:\\Users\\mudiy\\OneDrive\\Desktop\\ml\\titanic-image.png')
                render1 = ImageTk.PhotoImage(load1)
                img1 = tk.Label(self, image = render1)
                img1.image = render1
                img1.place(x = 0, y = 0)

                #load2 = Image.open('C:\\Users\\mudiy\\OneDrive\\Desktop\\ml\\titanic-image.png')
                #load2 = load2.resize((450, 450))
                #render2 = ImageTk.PhotoImage(load2)
                #img2 = tk.Label(self, image = render2)
                #img2.image = render2
                #img2.place(x = 950, y = 75)
		
                

                labelSum = tk.Label(self, text = "Logistic regression is a classification algorithm.\nIt predicts the probability of an input belonging to a certain set by \nseparating data into two regions. Logistic regression is used when the response \nvariable will be binary, for example, pass/fail.")
                labelSum.place(x =100, y= 200)

             #   label = tk.Label(self, text= machineLearningModels.logRegression(machineLearningModels.train1, machineLearningModels.train2, machineLearningModels.test))
            #label.place(x = 700,y = 100)

                textArea = tk.Text(self, height = 20, width = 15, wrap = tk.WORD)
                textArea.insert(tk.END, machineLearningModels.logRegression(machineLearningModels.train1, machineLearningModels.train2, machineLearningModels.test))
                textArea.configure(font=("Arial",12))

                scroller = tk.Scrollbar(self, orient= tk.VERTICAL)
                scroller.config(command = textArea.yview)
                textArea.configure(yscrollcommand= scroller.set)
                scroller.pack(side = tk.RIGHT, fill = tk.Y)
                textArea.place(x = 700, y = 20)

                labelScroll = tk.Label(self, text = "Hover over the predicition box and scroll\n down to see the model accuracy")
                labelScroll.place(x = 660, y= 410)

                button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
                button1.place(x = 725, y = 500)

                buttonZ = tk.Button(self, text="Prediction Graph", command=lambda: machineLearningModels.groupPlot(machineLearningModels.predLog))
                buttonZ.place(x = 275, y = 400)




class Page2(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                
                load1 = Image.open('C:\\Users\\mudiy\\OneDrive\\Desktop\\ml\\titanic-image.png')
                render1 = ImageTk.PhotoImage(load1)
                img1 = tk.Label(self, image = render1)
                img1.image = render1
                img1.place(x = 0, y = 0)

                

                labelSum = tk.Label(self, text = "K-Nearest Neighbors is an algorithm that can be used for both classification and regression. \nIt works by taking in training data and then seeing which data points are close to a data point\n and then classifying that data point as part of the same class as the majority of the k-nearest \ndata points. An advantage of k-nearest neighbors is that it is usually pretty accurate and \nworks well for non-linear data. A disadvantage is that it has to store all the training\n data which can lead to memory and runtime issues.")
                labelSum.place(x =100, y= 200)

                

                textArea = tk.Text(self, height = 20, width = 15, wrap = tk.WORD)
                textArea.insert(tk.END, machineLearningModels.KNN(machineLearningModels.train1, machineLearningModels.train2, machineLearningModels.test))
                textArea.configure(font=("Arial",12))

                scroller = tk.Scrollbar(self, orient= tk.VERTICAL)
                scroller.config(command = textArea.yview)
                textArea.configure(yscrollcommand= scroller.set)
                scroller.pack(side = tk.RIGHT, fill = tk.Y)
                textArea.place(x = 700, y = 20)

                labelScroll = tk.Label(self, text = "Hover over the predicition box and scroll\n down to see the model accuracy")
                labelScroll.place(x = 660, y= 410)

                button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
                button1.place(x = 725, y = 500)

                buttonZ = tk.Button(self, text="Prediction Graph", command=lambda: machineLearningModels.groupPlot(machineLearningModels.predK))
                buttonZ.place(x = 275, y = 400)


class Page3(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                
                load1 = Image.open('C:\\Users\\mudiy\\OneDrive\\Desktop\\ml\\titanic-image.png')
                render1 = ImageTk.PhotoImage(load1)
                img1 = tk.Label(self, image = render1)
                img1.image = render1
                img1.place(x = 0, y = 0)


                

                labelSum = tk.Label(self, text = "Decision trees that grow deep might lead to some incorrect results, random forests are a way to \ndeal with this. Random forests work by building a number of decision trees and merging them together\n and taking the averages of the test variables. One advantage of random forests is that it reduces\n the variance of using decision trees. A disadvantage is that making multiple decision \ntrees and merging them together might be run slow in some cases.")
                labelSum.place(x =75, y= 200)


                textArea = tk.Text(self, height = 20, width = 15, wrap = tk.WORD)
                textArea.insert(tk.END, machineLearningModels.rForest(machineLearningModels.train1, machineLearningModels.train2, machineLearningModels.test))
                textArea.configure(font=("Arial",12))

                scroller = tk.Scrollbar(self, orient= tk.VERTICAL)
                scroller.config(command = textArea.yview)
                textArea.configure(yscrollcommand= scroller.set)
                scroller.pack(side = tk.RIGHT, fill = tk.Y)
                textArea.place(x = 700, y = 20)

                labelScroll = tk.Label(self, text = "Hover over the predicition box and scroll\n down to see the model accuracy")
                labelScroll.place(x = 660, y= 410)

                button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
                button1.place(x = 725, y = 500)

                buttonZ = tk.Button(self, text="Prediction Graph", command=lambda: machineLearningModels.groupPlot(machineLearningModels.predForest))
                buttonZ.place(x = 275, y = 400)

class Page4(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                
                load1 = Image.open('C:\\Users\\mudiy\\OneDrive\\Desktop\\ml\\titanic-image.png')
                render1 = ImageTk.PhotoImage(load1)
                img1 = tk.Label(self, image = render1)
                img1.image = render1
                img1.place(x = 0, y = 0)

                

                labelSum = tk.Label(self, text = "A decision tree is a structure that is used to predict the value of a target value based on certain input variables.\n Each node of the tree represents a decision that will affect the outcome of the target value. \nOne advantage of using a decision tree to predict behavior is that decision trees are easy to understand and follow.\n It is easy to follow the conditional logic that decision trees use.")
                labelSum.place(x =50, y= 200)


                textArea = tk.Text(self, height = 20, width = 15, wrap = tk.WORD)
                textArea.insert(tk.END, machineLearningModels.dTree(machineLearningModels.train1, machineLearningModels.train2, machineLearningModels.test))
                textArea.configure(font=("Arial",12))

                scroller = tk.Scrollbar(self, orient= tk.VERTICAL)
                scroller.config(command = textArea.yview)
                textArea.configure(yscrollcommand= scroller.set)
                scroller.pack(side = tk.RIGHT, fill = tk.Y)
                textArea.place(x = 700, y = 20)

                labelScroll = tk.Label(self, text = "Hover over the predicition box and scroll\n down to see the model accuracy")
                labelScroll.place(x = 660, y= 410)

                button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
                button1.place(x = 725, y = 500)

                buttonZ = tk.Button(self, text="Prediction Graph", command=lambda: machineLearningModels.groupPlot(machineLearningModels.predTree))
                buttonZ.place(x = 275, y = 400)

                
display = root()
display.mainloop()