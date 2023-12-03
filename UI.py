import os
import openai
import customtkinter as ctk
import tkinter as tk

from data_handling import handling

def create_table(d):
    table_frame = tk.Toplevel(root)
    table_frame.title("Meal Plan")

    # Headers

    '''headers = [("Day " + str(i)) for i in range(1,len(d[0])+1)] '''
    headers = ["Meal Type", "Main Dish / amount", "Side Dish / amount",  "Side Dish (Drink) / amount"]
    for col, header in enumerate(headers):
        header_label = tk.Label(table_frame, text=header, font=("bold", 10), padx=50, pady=25, relief="solid")
        header_label.grid(row=0, column=col, sticky="nsew")

    dishType =["Breakfast", "Lunch", "Dinner"]
    # Data
    dishNum=0
    data = d
    for i in data:

        i.insert(0,dishType[dishNum])
        dishNum+=1

    for row, row_data in enumerate(data, 1):
        for col, cell_data in enumerate(row_data):
            cell_label = tk.Label(table_frame, text=str(cell_data), padx=50, pady=25, relief="solid")
            cell_label.grid(row=row, column=col, sticky="nsew")

    # Make columns expandable
    for col in range(len(headers)):
        table_frame.grid_columnconfigure(col, weight=1)

    # Make rows expandable
    for row in range(len(data) + 1):
        table_frame.grid_rowconfigure(row, weight=1)

def generate():
    prompt=[]
    gender=gender_dropdown.get()
    
    height = height_entry.get()
    
    weight = weight_entry.get()
    
    age = age_entry.get()
    
    restrictions = []
    if (checkbox1.get):
        restrictions.append("Kosher")
    if (checkbox2.get):
        restrictions.append("Halal")
    if (checkbox3.get):
        restrictions.append("Jain")
    if (checkbox4.get):
        restrictions.append("Vegan")
    if (checkbox5.get):
        restrictions.append("Vegetarian")
    
    
    def calorie_calculator(height, weight, age, gender):
        if gender == "male" or gender == "Male":
            return round(664.7 + (13.75 * weight) + (500.3 * height) - (6.755 * age))
        elif gender == "female" or gender == "Female":
            return round(655.1 + (9.563 * weight) + (185.0 * height) - (4.676 * age))
        elif gender == "other" or gender == "Other":
            return round(((664.7 + (13.75 * weight) + (500.3 * height) - (6.755 * age)) + (655.1 + (9.563 * weight) + (185.0 * height) - (4.676 * age))) // 2)
        else:
            raise Exception("Gender must be one of the following: male/female/other")
    
    
    
    comment = input_entry.get()

    calories_intake = calorie_calculator(float(height), float(weight), float(age), gender)
    
    plan = handling(height, age, gender, weight, restrictions, calories_intake,comment)
    
    #print(plan)
    data=[[plan[0][0] + " / " + plan[0][1] + " (" + plan[0][2] + " calories)",plan[1][0] + " / " + plan[1][1] + " (" + plan[1][2] + " calories)",plan[2][0] + " / " + plan[2][1] + " (" + plan[2][2] + " calories)"],[plan[3][0] + " / " + plan[3][1] + " (" + plan[3][2] + " calories)",plan[4][0] + " / " + plan[4][1] + " (" + plan[4][2] + " calories)",plan[5][0] + " / " + plan[5][1] + " (" + plan[5][2] + " calories)"],[plan[6][0] + " / " + plan[6][1] + " (" + plan[6][2] + " calories)",plan[7][0] + " / " + plan[7][1] + " (" + plan[7][2] + " calories)",plan[8][0] + " / " + plan[8][1] + " (" + plan[0][2] + " calories)"]]
    # Create a button to open the table
    create_table(data)
    
    
    
    
    
    

root = ctk.CTk()
root.geometry("1250x850")
root.title("HackNYU - NutriGuide")

ctk.set_appearance_mode("dark-blue")

title_label = ctk.CTkLabel(root, text="NutriGuide",
                           font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(30, 30))

frame = ctk.CTkScrollableFrame(root, orientation="vertical", height=550)
frame.pack(fill="x", padx=100)

gender_frame = ctk.CTkFrame(frame)
gender_frame.pack(padx=100, pady=(30, 5), fill="both")
gender_label = ctk.CTkLabel(
    gender_frame, text="Gender", font=ctk.CTkFont(weight="bold", size = 24)
)
gender_label.pack()
gender_dropdown = ctk.CTkComboBox(
    gender_frame, values=["Male", "Female", "Other"]
)
gender_dropdown.pack(pady=10)

age_frame = ctk.CTkFrame(frame)
age_frame.pack(padx=100, pady=(30, 5), fill="both")
# Add the Height Label
age_label = ctk.CTkLabel(
    age_frame, text="Age (Years)(Numbers Only)", font=ctk.CTkFont(weight="bold", size = 24)
)
age_label.pack()
# Use the Entry widget for height input
age_entry = ctk.CTkEntry(age_frame)
age_entry.pack(pady=10)

height_frame = ctk.CTkFrame(frame)
height_frame.pack(padx=100, pady=(30, 5), fill="both")
# Add the Height Label
height_label = ctk.CTkLabel(
    height_frame, text="Height (Meters)(Numbers Only)", font=ctk.CTkFont(weight="bold", size = 24)
)
height_label.pack()
# Use the Entry widget for height input
height_entry = ctk.CTkEntry(height_frame)
height_entry.pack(pady=10)

weight_frame = ctk.CTkFrame(frame)
weight_frame.pack(padx=100, pady=(30, 5), fill="both")
# Add the Height Label
weight_label = ctk.CTkLabel(
    weight_frame, text="Weight (Kilograms)(Numbers Only)", font=ctk.CTkFont(weight="bold",size = 24)
)
weight_label.pack()
# Use the Entry widget for height input
weight_entry = ctk.CTkEntry(weight_frame)
weight_entry.pack(pady=10)

preference_frame = ctk.CTkFrame(frame)
preference_frame.pack(padx=100, pady=(30, 5), fill="both")
preference_label = ctk.CTkLabel(preference_frame, text="Dietary Restrictions", font=ctk.CTkFont(weight="bold", size = 24))
preference_label.pack(pady=10)
checkbox1 = ctk.CTkCheckBox(preference_frame, text="Kosher")
checkbox1.pack(padx=50, pady=10)
checkbox2 = ctk.CTkCheckBox(preference_frame, text="Halal")
checkbox2.pack(padx=50, pady=10)
checkbox3 = ctk.CTkCheckBox(preference_frame, text="Jain")
checkbox3.pack(padx=50, pady=10)
checkbox4 = ctk.CTkCheckBox(preference_frame, text="Vegan")
checkbox4.pack(padx=50, pady=10)
checkbox5 = ctk.CTkCheckBox(preference_frame, text="Vegetarian")
checkbox5.pack(padx=50, pady=10)
button = ctk.CTkButton(frame, text="Generate Meal Plan", command=generate)
button.pack(padx=100, fill="x", pady=(5, 20))

input_frame = ctk.CTkFrame(frame, height=200, width=400)
input_frame.pack(padx=100, pady=(40, 20), fill="both")
# Add the Height Label
input_label = ctk.CTkLabel(
    input_frame, text="Any concerns about the meal plan?", font=ctk.CTkFont(weight="bold", size = 24)
)
input_label.pack()
# Use the Entry widget for height input
input_entry = ctk.CTkEntry(input_frame)
input_entry.pack(padx=50, pady=50)
button2 = ctk.CTkButton(frame, text="Regenerate Meal Plan", command=generate)
button2.pack(padx=100, fill="x", pady=(5, 20))


root.mainloop()