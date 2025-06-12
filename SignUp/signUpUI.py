import customtkinter
from SignUp.signUpLogic import confirm_account

def create_signupUI (parentwindow):
    parentwindow.title("Sign Up")
    parentwindow.geometry('285x285')

    # =============================================
    #                  SIGN UP FRAME
    # =============================================
    signupframe = customtkinter.CTkFrame(parentwindow) # contains all UI related to SignUp
    signupframe.pack()


    # ==================== SIGN UP FORMS =====================
    pagetitle = customtkinter.CTkLabel(signupframe, text = "SIGN UP", font = ("Times New Roman", 25, "bold"))
    pagetitle.grid(row = 0, columnspan = 3, pady = (30, 40))

    lbl_username = customtkinter.CTkLabel(signupframe, text = "Username")
    lbl_username.grid(row = 1, column = 0, padx = (30, 10))

    entry_username = customtkinter.CTkEntry(signupframe)
    entry_username.grid(row = 1, column = 1, padx = (5, 50))

    lbl_password1 = customtkinter.CTkLabel(signupframe, text = "Password:", width = 10, height = 2)
    lbl_password1.grid(row = 2, column = 0, padx = (30, 10))

    entry_password1 = customtkinter.CTkEntry(signupframe, show = "*")
    entry_password1.grid(row = 2, column = 1, padx = (5,50), pady = 30)

    lbl_password2 = customtkinter.CTkLabel(signupframe, text = "Confirm Password:", width = 10, height = 2)
    lbl_password2.grid(row = 3, column = 0, padx = (30, 10))

    entry_password2 = customtkinter.CTkEntry(signupframe, show = "*")
    entry_password2.grid(row = 3, column = 1, padx = (5,50), pady = 30)

    btn_signup = customtkinter.CTkButton(signupframe, text = "Log-in", command = lambda: confirm_account(entry_username.get(), entry_password1.get(), entry_password2.get(), signupframe)) # pass inputted username, password to determine if the account is valid and the whole login ui to destroy it if account is valid.
    btn_signup.grid(row = 4, columnspan = 3, pady = (0, 40))
