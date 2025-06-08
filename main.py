import customtkinter
import sqlite3  
from Login.loginUi import create_loginUI

# === MAIN FUNCTION ===
window = customtkinter.CTk()
window.title('Main Window')

create_loginUI(window) 

window.mainloop()