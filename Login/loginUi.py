import customtkinter
from Login.loginBackend import validate_account # imported to

def create_loginUI (parentwindow): 
    parentwindow.title("Log In")
    parentwindow.geometry('285x285')

    # =============================================
    #                  LOG IN FRAME
    # =============================================
    loginframe = customtkinter.CTkFrame(parentwindow) # contains all UI related to LogIn
    loginframe.pack()


    # ==================== LOG IN AND PASSWORD =====================
    pagetitle = customtkinter.CTkLabel(loginframe, text = "LOG IN", font = ("Times New Roman", 25, "bold"))
    pagetitle.grid(row = 0, columnspan = 3, pady = (30, 40))
    
    lbl_login = customtkinter.CTkLabel(loginframe, text = "Username:", width = 10, height = 2)
    lbl_login.grid(row = 1, column = 0, padx = (30, 10))

    entry_login = customtkinter.CTkEntry(loginframe)
    entry_login.grid(row = 1, column = 1, padx = (5, 50))

    lbl_password = customtkinter.CTkLabel(loginframe, text = "Password:", width = 10, height = 2)
    lbl_password.grid(row = 2, column = 0, padx = (30, 10))

    entry_password = customtkinter.CTkEntry(loginframe, show = "*")
    entry_password.grid(row = 2, column = 1, padx = (5,50), pady = 30)


    # ======================= LOG IN BUTTON ========================
    btn_login = customtkinter.CTkButton(loginframe, text = "Log-in", command = lambda: validate_account(entry_login.get(), entry_password.get(), loginframe)) # pass inputted username, password to determine if the account is valid and the whole login ui to destroy it if account is valid.
    btn_login.grid(row = 3, columnspan = 3, pady = (0, 40))

    return loginframe # return the frame that contains log-in UI to the parentwindow