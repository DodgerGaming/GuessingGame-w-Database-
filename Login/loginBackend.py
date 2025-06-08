from tkinter import messagebox
import sqlite3

def validate_account (username, password, loginframe):

    conn = sqlite3.connect("System.db")
    
    cursor = conn.execute("SELECT * FROM player WHERE USERNAME = ?", (username,)) # sql command to find if theres a record that have the same username as the inputted username

    player = cursor.fetchone() # istore ang nakuhang record mula sa database para magamit sa validation ng username at password

    cursor.close()
    conn.close()

    if player[2] == password:
        messagebox.showinfo(message = "Log in successfully")
        loginframe.destroy() # destroy the whole login UI
        
    else:
        messagebox.showerror(message  = "Invalid password!")
    