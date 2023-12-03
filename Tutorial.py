import os
import openai
import customtkinter as ctk

root = ctk.CTk()
root.geometry("750x550")
root.title("appThing")

ctk.set_appearance_mode("dark")

title_label = ctk.CTkLabel(root, text="HealthApp",
                           font = ctk.CTkFont(size=30,weight="bold"))
title_label.pack(padx=10,pady=(40,20))

frame = ctk.CTkFrame(root)
frame.pack(fill="x",padx=100)

language_frame = ctk.CTkFrame(frame)
language_frame.pack(padx=100,pady=(20,5),fill="both")

root.mainloop()