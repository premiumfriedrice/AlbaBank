import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from src import db
import mysql.connector
import random
import yaml
with open("env.yaml", "r") as f:
    config = yaml.safe_load(f)

ctk.set_appearance_mode("dark")
        
dbconn = mysql.connector.connect(host=config["HOST"], user=config["USERNAME"], password=config["PASSWORD"], database=config["DB_NAME"])

cur=dbconn.cursor()

id = 0

class SignUpWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry("500x500")
        self.title("Sign Up")
        
        self.TitleLabel = ctk.CTkLabel(self, justify=ctk.LEFT, text="Sign Up", font=("IBMPlexSerif", 20), text_color="white").grid(row=0, column=0, pady=10, padx=10)
        self.emailEntry = ctk.CTkEntry(self, placeholder_text="Email")
        self.emailEntry.grid(row=1, column=0, pady=10, padx=10)
        self.birthdayEntry = ctk.CTkEntry(self, placeholder_text="YYYY-MM-DD")
        self.birthdayEntry.grid(row=2, column=0, pady=10, padx=10)
        self.userEntry = ctk.CTkEntry(self, placeholder_text="Username")
        self.userEntry.grid(row=3, column=0, pady=10, padx=10)
        self.newPasswordEntry = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.newPasswordEntry.grid(row=4, column=0, pady=10, padx=10)
        self.confirmPasswordEntry = ctk.CTkEntry(self, placeholder_text="Confirm Password", show="*")
        self.confirmPasswordEntry.grid(row=5, column=0, pady=10, padx=10)
        self.confirmSignUp = ctk.CTkButton(self, text="Sign Up", command=self.signUp)
        self.confirmSignUp.grid(row=6, column=0, pady=10, padx=10)
        
    def signUp(self):
        if self.newPasswordEntry.get() == self.confirmPasswordEntry.get():
            db.addUser(0, self.userEntry.get(), self.newPasswordEntry.get(), self.birthdayEntry, self.emailEntry.get(), 0, 0)
            self.destroy()
        else:
            messagebox.showwarning(title="Error", message="Please confirm your new password.")
        
class MainMenu(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.configure(segmented_button_selected_color="#5B9A8E", segmented_button_selected_hover_color="#37675E")        
        
        global id
        
        self.userid = ctk.IntVar(value=1)
        self.checkingAmount = ctk.DoubleVar(value=db.getChecking(self.userid.get()))
        self.savingsAmount = ctk.DoubleVar(value=db.getSavings(self.userid.get()))
        
        self.add("Balance")
        self.add("Pay and Transfer")
        self.add("Account")
        
        
        self.checkingBalanceFrame = ctk.CTkFrame(self.tab("Balance"))
        self.checkingBalanceFrame.pack(side=ctk.LEFT, padx=10, pady=10, ipadx=10, ipady=10, fill="both", expand=True)
        self.checkingBalanceLabel = ctk.CTkLabel(self.checkingBalanceFrame, text="Checking", font=("IBMPlexSerif", 20), justify=ctk.CENTER)
        self.checkingAmountLabel = ctk.CTkLabel(self.checkingBalanceFrame, textvariable=self.checkingAmount, font=("IBMPlexSerif", 40), justify=ctk.CENTER)
        self.ckdepositLabel = ctk.CTkLabel(self.checkingBalanceFrame, text="Deposit", font=("IBMPlexSerif", 15), justify=ctk.CENTER)
        self.checkDeposit = ctk.StringVar()
        self.checkingDepositEntry = ctk.CTkEntry(self.checkingBalanceFrame, placeholder_text="Deposit", textvariable=self.checkDeposit)
        self.checkingBalanceLabel.pack(side=ctk.TOP, padx=20, pady=10)
        self.checkingAmountLabel.pack(padx=30, pady=30)
        self.ckdepositLabel.pack(padx=30, pady=30)
        self.checkingDepositEntry.pack(padx=10, pady=10)
        
        self.savingsBalanceFrame = ctk.CTkFrame(self.tab("Balance"))
        self.savingsBalanceFrame.pack(side=ctk.RIGHT, padx=10, pady=10, ipadx=10, ipady=10, fill="both", expand=True)
        self.savingsBalanceLabel = ctk.CTkLabel(self.savingsBalanceFrame, text="Savings", font=("IBMPlexSerif", 20), justify=ctk.LEFT)
        self.savingsAmountLabel = ctk.CTkLabel(self.savingsBalanceFrame, textvariable=self.savingsAmount, font=("IBMPlexSerif", 40))
        self.savdepositLabel = ctk.CTkLabel(self.savingsBalanceFrame, text="Deposit", font=("IBMPlexSerif", 15), justify=ctk.CENTER)
        self.savDeposit = ctk.StringVar()
        self.savingsDepositEntry = ctk.CTkEntry(self.savingsBalanceFrame, placeholder_text="Deposit", textvariable=self.savDeposit)
        self.savingsBalanceLabel.pack(side=ctk.TOP, padx=20, pady=10)
        self.savingsAmountLabel.pack(padx=30, pady=30)
        self.savdepositLabel.pack(padx=30, pady=30)
        self.savingsDepositEntry.pack(padx=10, pady=10)
        
        self.transferFrame = ctk.CTkFrame(master=self.tab("Pay and Transfer"))
        self.transferFrame.pack(padx=20, pady=20, ipadx=20, ipady=20, fill="both", expand=True, anchor=ctk.CENTER)
        self.fromLabel = ctk.CTkLabel(self.transferFrame, text="From:")
        self.fromAccountChoice = ctk.CTkOptionMenu(self.transferFrame, values=["Checking", "Savings"])
        self.toLabel = ctk.CTkLabel(self.transferFrame, text="To:")
        self.toAccountChoice = ctk.CTkOptionMenu(self.transferFrame, values=["Checking", "Savings"])
        self.amountLabel = ctk.CTkLabel(self.transferFrame, text="Amount:")
        self.amountEntry = ctk.CTkEntry(self.transferFrame, placeholder_text="0.00", width=200, height=40).grid(column=1, row=2, padx=60, pady=20)
        self.fromLabel.grid(column=0, row=0, padx=20, pady=20)
        self.fromAccountChoice.grid(column=1, row=0, padx=20, pady=20)
        self.toLabel.grid(column=0, row=1, padx=20, pady=20)
        self.toAccountChoice.grid(column=1, row=1, padx=20, pady=20)  
        self.amountLabel.grid(column=0, row=2, padx=20, pady=20)
        
        self.accountFrame = ctk.CTkFrame(master=self.tab("Account"))
        self.transferFrame.pack(padx=20, pady=20, ipadx=20, ipady=20, fill="both", expand=True, anchor=ctk.CENTER)
        
        
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.geometry("900x600")
        self.title("AlbaBank_2023")
        
        self.loginFrame = ctk.CTkFrame(self)
        self.loginFrame.pack(pady=20, padx=60, fill="both", expand=True)
        self.titleLabel = ctk.CTkLabel(self.loginFrame, justify=ctk.LEFT, text="Alba Bank", font=("IBMPlexSerif", 20), text_color="white")
        self.titleLabel.pack(pady=30, padx=50)
        self.usernameEntry = ctk.CTkEntry(self.loginFrame, placeholder_text="Username")
        self.usernameEntry.pack(pady=10, padx=10)
        self.passwordEntry = ctk.CTkEntry(self.loginFrame, placeholder_text="Password", show="*")
        self.passwordEntry.pack(pady=10, padx=10)
        self.login_button = ctk.CTkButton(self.loginFrame, text="Login", command=self.login)
        self.login_button.pack(pady=10, padx=10)
        self.signup_button = ctk.CTkButton(self.loginFrame, command=self.open_signUp, text="Sign Up")
        self.signup_button.pack(pady=0, padx=10)
    
    global id
    
    def login(self):
        global id
        valsql = f"SELECT id FROM users WHERE username = %s AND password = %s"
        cur.execute(valsql, (self.usernameEntry.get(), self.passwordEntry.get()))
        if cur.fetchall():
            for num in cur.fetchall():
                id = num
                print(id)
            self.openMainMenu()
        else:
            messagebox.showwarning(title="Error", message="Invalid username or password.")

    def open_signUp(self):
        signUpwindow = SignUpWindow(self)
        signUpwindow.grab_set()
        
    def openMainMenu(self):
        self.loginFrame.destroy()
        self.tab_view = MainMenu(self)
        self.tab_view.pack(padx=20, pady=20, fill="both", expand=True)
        self.grid_columnconfigure(1, weight=1)

    
app = App()
app.mainloop()