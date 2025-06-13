import customtkinter
from tkinter import messagebox
import sqlite3

def confirm_account(username, password1, password2):
    # validating if the user input something in text fields
    if username == "" or password1 == "" or password2 == "":
        messagebox.showerror(message = "Please input all text fields!")
    else:
        is_existing(username) 

def is_existing(username): # checks if the inputted username is already existing in database
    connect = sqlite3.connect("System.db")
    
    cursor = connect.execute("SELECT USERNAME FROM PLAYER WHERE USERNAME = ?", (username))

    # TODO: Implementation of checking if the inputted name of user is already on database 
    


def create_account():
    pass